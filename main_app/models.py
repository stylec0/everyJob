from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


INDUSTRIES = (
    ('AERO', 'Aerospace'),
    ('A', 'Art'),
    ('AUTO', 'Automotive'),
    ('D', 'Design'),
    ('EDU', 'Education'),
    ('E', 'Engineering'),
    ('F', 'Finance'),
    ('G', 'Government'),
    ('H', 'Healthcare'),
    ('IT', 'Information Technology'),
    ('M', 'Media & Entertainment'),
    ('SCI', 'Science'),
    ('S', 'Service Industry'),
    ('RE', 'Real Estate & Development'),
    ('R', 'Retail'),
)


class JobTitle(models.Model):
    job_title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'job_title_id': self.id})


class JobPost(models.Model):
    job_title = models.ManyToManyField(JobTitle)
    industry = models.CharField(
        max_length=10,
        choices=INDUSTRIES,
        default=INDUSTRIES[0][0]
    )
    details = models.TextField(max_length=2000)
    years_experience = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.job_title, 'job_post_id': self.id})
