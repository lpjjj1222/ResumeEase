from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from .models import Candidate
from django.views.generic.edit import FormView
from django.views import View
from django.shortcuts import redirect
from .forms import ResumeForm,NoteForm,InvitationForm
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
import fitz
import re
from .tags import all_tags_list
from .models import Tag
from django.urls import reverse
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

class CvLoginView(LoginView):
    template_name = 'cv/login.html'
    success_url = reverse_lazy('starting-page')

class CvLogoutView(LoginRequiredMixin,LogoutView):
    pass

class StartingPageView(LoginRequiredMixin,ListView):
    template_name = "cv/all_candidates.html"
    model = Candidate
    # ordering = ["-date"]
    context_object_name = "candidates"


class UploadCVView(LoginRequiredMixin,FormView):

    template_name = 'cv/upload.html'
    form_class = ResumeForm
    success_url = reverse_lazy('upload-cv')

    def extract_text_from_pdf(self, pdf_file):
        text = ""
        with fitz.open(stream=pdf_file.read(), filetype="pdf") as pdf:
            for page in pdf:
                text += page.get_text()
            return text
        
    def find_matching_tags(self, text, tags):
        pattern = re.compile('|'.join(re.escape(tag) for tag in tags), re.IGNORECASE)
        matching_tags = pattern.findall(text)
        return set(matching_tags)  # 使用 set 去重


    def form_valid(self, form):
        candidate = form.save(commit=False)
        # 提取文件名作为 name 字段，slugify 用于生成 slug 字段
        candidate.name = self.request.FILES['cv_file'].name.split('.')[0]
        candidate.slug = slugify(candidate.name)
        #提取pdf内容
        pdf_file = self.request.FILES['cv_file']
        pdf_content = self.extract_text_from_pdf(pdf_file)
        # 找邮箱
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        email = re.search(email_pattern, pdf_content)
        if email:
            email = email.group()
        else:
            email = None
        candidate.email = email
        # 找电话
        phone_pattern = r'(\+?\d{1,3}?[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}'
        phone = re.search(phone_pattern, pdf_content)
        if phone:
            phone = phone.group()
        else:
            phone = None
        candidate.phone = phone

        #先保存数据，让这个Candidate实例有一个id，才能对应上多对多关系，才能访问tags
        candidate.save()

        # 找tag
        matching_tags = self.find_matching_tags(pdf_content, all_tags_list)
        matching_tags_list = list(matching_tags)
        for matched_tag in matching_tags_list:
            try:
                tag = Tag.objects.get(caption__iexact=matched_tag)
                candidate.tags.add(tag)
            except Tag.DoesNotExist:
                pass
        
        #再保存一次数据，把tags存进去
        candidate.save()


        return super().form_valid(form)

class CandidateDetailView(LoginRequiredMixin,View):
    def get(self, request, slug):
        candidate = Candidate.objects.get(slug=slug)
        context = {
            "candidate": candidate,
            "tags": candidate.tags.all(),
            "notes": candidate.notes.all().order_by("-created_at"),
            "status": candidate.status,
            "note_form": NoteForm(),
            "invitation_form": InvitationForm(),
        }
        return render(request, "cv/cv_detail.html", context)
    
    def post(self, request, slug):
        if 'submit-note' in request.POST:
            return self.add_note_to_candidate(request, slug)
        elif 'cancel-invitation' in request.POST:
            candidate = Candidate.objects.get(slug=slug)
            candidate.status = 'pending'
            candidate.save()
            print('cancel-invitation')
        elif 'submit-invitation' in request.POST:
            print('submit-invitation')
            candidate = Candidate.objects.get(slug=slug)
            candidate.status = 'selected'
            candidate.save()
            return self.invite_candidate(request, slug)

        return HttpResponseRedirect(reverse('candidate-detail', args=[slug]))

    
    def invite_candidate(self, request, slug):
        print('进入invitation流程')
        form = InvitationForm(request.POST)
        candidate = Candidate.objects.get(slug=slug)
        if form.is_valid():
            invitation = form.save(commit=False)
            invitation.candidate = candidate
            invitation.save()
            send_mail(
                'Tencent PCG Interview Invitation',
                f'Dear Candidate, \n\nWe are pleased to inform you that you have been selected for an interview for the position of {invitation.position} at Tencent PCG. Your interview is scheduled for {invitation.interview_date}. We look forward to discussing how your skills and experiences align with our team.\n\nBest regards,\nTencent PCG Recruitment Team',
                'paigelin575@gmail',
                [candidate.email],
            )
            print('已发送邮件')
            return HttpResponseRedirect(reverse("candidate-detail", args=[slug]))
        context = {
            "candidate": candidate,
            "tags": candidate.tags.all(),
            "notes": candidate.notes.all().order_by("-created_at"),
            "status": candidate.status,
            "note_form": NoteForm(),
            "invitation_form": form,
        }
        return render(request, "cv/cv_detail.html", context)

    def add_note_to_candidate(self, request, slug):
        note_form = NoteForm(request.POST)
        candidate = Candidate.objects.get(slug=slug)

        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.candidate = candidate
            note.save()
            return HttpResponseRedirect(reverse('candidate-detail', args=[slug]))
        context = {
            "candidate": candidate,
            "tags": candidate.tags.all(),
            "notes": candidate.notes.all().order_by("-created_at"),
            "status": candidate.status,
            "note_form": note_form,
            "invitation_form": InvitationForm(),
        }
        return render(request, "cv/cv_detail.html", context)
    
class IntervieweeView(LoginRequiredMixin, View):
    def get(self, request):
        interviewee = Candidate.objects.filter(status='selected')
        context = {
            "interviewee": interviewee
        }
        return render(request, "cv/interviewee.html", context)

    def post(self, request):
        s = request.POST.get('candidate_slug')
        c = Candidate.objects.get(slug=s)
        if c.status == 'selected':
            c.status = 'pending'
            c.save()
        elif c.status == 'pending':
            c.status = 'selected'
            c.save()
        return HttpResponseRedirect(reverse("candidate-detail", args=[s]))

        
        
