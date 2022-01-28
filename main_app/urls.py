from django.urls import path
# import all the functions in the views folder (controller functions)
# and attach them as methods to the views object
from . import views  # views is the name of the file

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    # path('about/', views.about, name='about'),
]