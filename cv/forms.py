from django import forms
from .models import Candidate

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['cv_file']
        labels = {
            'cv_file': 'Upload Resumes',
        }
