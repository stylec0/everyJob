from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.http import HttpResponse
# import our model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import JobTitle, JobPost


def home(request):
    return render(request, 'home.html')


class JobPostCreate(CreateView):
    model = JobPost
    fields = '__all__'

    def form_valid(self, form):
        # form.instance is the jobpost being created
        form.instance.user = self.request.user
        # this lets the CreateView do it's job
        return super().form_valid(form)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid signup - try again!'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def job_title_detail(request):
    return render(request, 'everyjobs/detail.html')
