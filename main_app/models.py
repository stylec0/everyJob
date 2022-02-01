from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django import forms


# To be edited/added later
INDUSTRIES = (
    ('H', 'Healthcare'),
    ('IT', 'Information Technology'),
    ('RE', 'Real Estate and Development'),
    ('R', 'Retail'),
    ('EDU', 'Education'),
    ('G', 'Government'),
    ('E', 'Engineering'),
    ('D', 'Design'),
    ('A', 'Art'),
    ('S', 'Science'),
)


class JobTitle(models.Model):
    job_title = models.CharField(max_length=50)

    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'job_title_id': self.id})


class JobPost(models.Model):
    job_title = models.ManyToManyField(JobTitle)
    industry = models.CharField(
        max_length=3,
        choices=INDUSTRIES,
        default=INDUSTRIES[0][0]
    )
    details = models.TextField(max_length=2000)
    years_experience = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.job_title})
