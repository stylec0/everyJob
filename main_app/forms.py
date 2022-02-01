
from django.forms import ModelForm
from .models import JobPost


class JobPostForm(ModelForm):
    class Meta:
        model = JobPost
        fields = ['industry', 'details', 'years_experience']

class JobPostUpdateForm(ModelForm):
    class Meta:
        model = JobPost
        fields = ['industry', 'details', 'years_experience']
