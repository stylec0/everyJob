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
from .forms import JobPostForm, JobPostUpdateForm


def home(request):
    jobTitle = JobTitle.objects.all()
    return render(request, 'home.html', {
        'jobTitle': jobTitle
    })


# this is a test comment
# wrote view function because we needed to associate
# both the user and the JobTitle with the job post being created
def JobPostCreate(request, job_title_id):
    title = JobTitle.objects.filter(pk=job_title_id)
    job_form = JobPostForm(request.POST)

    if job_form.is_valid():
        new_job_post = job_form.save(commit=False)
        new_job_post.user_id = request.user.id
        # save every time new_job_post gets manipulated
        new_job_post.save()
        new_job_post.job_title.set(title)
        new_job_post.save()
        # return to detail of selected Job Title
        # ('detail' path in urls.py)
        # this first job_title_id is taking the parameter
        # and reassigning it
        # (re-passing the parameter so we can use it on the page)
    return redirect('detail', job_title_id=job_title_id)


def GetJobPostForm(request, job_title_id):
    # assigning the JobTitle we made the request from
    # to this variable
    jobtitle = JobTitle.objects.get(pk=job_title_id)
    # render the form (jobpost_form.html)
    jobform = JobPostForm()
    return render(request, 'main_app/jobpost_form.html', {
        'JobTitle': jobtitle,
        'JobForm': jobform
    })

@login_required
def GetJobPostUpdate(request, job_title_id):
    jobtitle = JobTitle.objects.get(pk=job_title_id)
    jobupdateform = JobPostUpdateForm()
    return render(request, 'main_app/jobpost_update.html', {
        'JobTitle': jobtitle,
        'JobUpdateForm': jobupdateform
    })

@login_required
def UpdateJobPost(request, job_title_id, job_post_id):
    title = JobTitle.objects.filter(pk=job_title_id)
    # job_post value needs to be the job post we are trying to edit specifically
    job_post = JobPost.objects.filter(id=job_post_id)
    job_form = JobPostUpdateForm(request.POST)
    print(job_post, "<---this is the job_post")
    #print(job_post_id, "<---this is the job_post_id")
    if job_form.is_valid():
        update_job_post = job_form.save(commit=False)
        update_job_post.user_id = request.user.id
        # save every time new_job_post gets manipulated
        update_job_post.save()
        update_job_post.job_title.set(title)
        update_job_post.save()
        # return to detail of selected Job Title
        # ('detail' path in urls.py)
        # this first job_title_id is taking the parameter
        # and reassigning it
        # (re-passing the parameter so we can use it on the page)
    return redirect('detail', job_title_id=job_title_id)

class JobTitleCreate(LoginRequiredMixin, CreateView):
    model = JobTitle
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
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


def job_title_detail(request, job_title_id):
    details = JobPost.objects.filter(job_title=job_title_id)
    # allows us to access the jobTitle name for the detail page
    job_title = JobTitle.objects.get(id=job_title_id)
    return render(request, 'everyJobs/detail.html', {
        'jobPost': details,
        'job_title': job_title
    })
