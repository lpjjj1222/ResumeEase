from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, ListView
from .models import Candidate
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from .forms import ResumeForm
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
import fitz
import re

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
    login_url = reverse_lazy('login-page')
    

class UploadCVView(LoginRequiredMixin,FormView):
    template_name = 'cv/upload.html'
    form_class = ResumeForm
    success_url = reverse_lazy('upload-cv')
    login_url = reverse_lazy('login-page')

    def extract_text_from_pdf(self, pdf_file):
        text = ""
        with fitz.open(stream=pdf_file.read(), filetype="pdf") as pdf:
            for page in pdf:
                text += page.get_text()
            return text


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

        #保存数据
        candidate.save()
        return super().form_valid(form)


