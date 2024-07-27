from django.db import models




# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=30,null=False)
    email = models.EmailField(max_length=40,null=True)
    phone = models.CharField(max_length=20,null=True)
    cv_file = models.FileField(upload_to="cv",null=False)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name
    




# class UploadSuccessView(FormView):
#     template_name = 'upload_success.html'
#     form_class = CandidateForm
#     success_url = 'upload/'

