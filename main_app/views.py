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
from .forms import JobPostForm


def home(request):
    jobTitle = JobTitle.objects.all()
    return render(request, 'home.html', {
        'jobTitle': jobTitle
    })


# make a form for add job, like feeding_form
def JobPostCreate(request, job_title_id):
    title = JobTitle.objects.filter(pk=job_title_id)
    job_form = JobPostForm(request.POST)

    print(title, request, request.user,  "<-------- title, request")
    if job_form.is_valid():
        new_job_post = job_form.save(commit=False)
        new_job_post.user_id = request.user.id
        new_job_post.save()
        new_job_post.job_title.set(title)
        new_job_post.save()
        print(new_job_post, "<----- new job post")

    return redirect('detail', job_title_id=job_title_id)


def GetJobPostForm(request, job_title_id):
    # make sure we can find the job title in db
    jt = JobTitle.objects.get(pk=job_title_id)
    print(jt, "<--- job title")
    # render the form
    jobform = JobPostForm()
    return render(request, 'main_app/jobpost_form.html', {
        'JobTitle': jt,
        'JobForm': jobform
    })


# class JobPostCreate(LoginRequiredMixin, CreateView):
#    model = JobPost
#    fields = ['industry', 'details', 'years_experience']

#    def form_valid(self, form):
#        # form.instance is the jobpost being created
#        form.instance.user = self.request.user
#        # this lets the CreateView do it's job
#        return super().form_valid(form)

class JobTitleCreate(LoginRequiredMixin, CreateView):
    model = JobTitle
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# def JobPostCreate(request, job_title_id):
#     print(job_title_id, "id")
#     print(request, "request")


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


def job_title_detail(request, job_title_id):
    details = JobPost.objects.filter(job_title=job_title_id)
    job_title = JobTitle.objects.get(id=job_title_id)
    return render(request, 'everyJobs/detail.html', {
            'jobPost': details,
            'job_title': job_title
    })
