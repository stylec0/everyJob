from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

INDUSTRIES = (
        ('H', 'Healthcare'),
        ('I', 'Information Technology'),
        ('Re', 'Real Estate and Development'),
        ('R', 'Retail'),
        ('Edu', 'Education'),
        ('G', 'Government'),
        ('E', 'Engineering'),
        ('D', 'Design'),
        ('A', 'Art'),
        ('S', 'Science'),
)

class jobTitle(models.Model):
    jobtitle = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse('title_detail', kwargs={'pk': self.id})

class jobPost(models.Model):
    jobtitle = models.ManyToManyField(jobTitle)
    industry = models.CharField(
        max_length=50,
        choices=INDUSTRIES,
    )
    details = models.TextField(max_lenght=2000)
    years_experience = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse('post_detail', kwargs={'pk': self.id})