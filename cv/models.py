from django.db import models
from django.utils import timezone




# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    
class Candidate(models.Model):
    STATUS_CHOICES = [
    ('selected', 'Selected'),
    ('pending', 'Pending'),
    ('rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=30,null=False)
    email = models.EmailField(max_length=40,null=True)
    phone = models.CharField(max_length=20,null=True)
    cv_file = models.FileField(upload_to="cv",null=False)
    slug = models.SlugField(unique=True, null=True, db_index=True)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    user = models.CharField(max_length=30)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="notes")
    text = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)


class Position(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Invitation(models.Model):
    interview_date = models.DateTimeField()
    position = models.ForeignKey("Position", on_delete=models.CASCADE, null=True, related_name="invitation")
    candidate = models.ForeignKey("Candidate", on_delete=models.CASCADE, null=True, related_name="invitation")

    def __str__(self):
        return f"Invitation:{self.candidate.name} - {self.position.title} - {self.interview_date}"

    


# class UploadSuccessView(FormView):
#     template_name = 'upload_success.html'
#     form_class = CandidateForm
#     success_url = 'upload/'

