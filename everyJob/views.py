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