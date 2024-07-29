from django import forms
from .models import Candidate, Note, Invitation

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['cv_file']
        labels = {
            'cv_file': 'Upload Resumes',
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['candidate', 'created_at']
        labels = {
            'text': 'Add a note',
            'user': 'Your name',
        }

class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['interview_date', 'position']
        widgets = {
            'interview_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
        }
        



