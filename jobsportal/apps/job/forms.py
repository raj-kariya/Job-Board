from django import forms
from .models import Job

class AddJobForum(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'show_description', 'long_description']

    