from django.urls import path
# import all the functions in the views folder (controller functions)
# and attach them as methods to the views object
from . import views  # views is the name of the file

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('everyjob/create/', views.JobTitleCreate.as_view(),
         name='job_title_create'),
    path('accounts/signup/', views.signup, name='signup'),
    # on JobTitle detail, when you click add JobPost
    path('everyjob/<int:job_title_id>/add_job_post/',
         views.GetJobPostForm, name='add_job_post'),
    # on AddJobPost Form page, when you click submit
    path('everyjob/<int:job_title_id>/post_job/',
         views.JobPostCreate, name='post_job'),
    # This route gets the update job post form
    path('post/<int:job_post_id>/get_job_post_update/',
         views.GetJobPostUpdate, name='get_job_post_update'),
    # This route posts the update job post data
    path('post/<int:job_post_id>/update_job_post/',
         views.UpdateJobPost, name='update_job_post'),
    path('post/<int:job_post_id>/job_post_delete/', views.delete, name='job_post_delete'),
    path('everyjob/create/', views.JobTitleCreate.as_view(),
         name='job_title_create'),
    path('everyjob/<int:job_title_id>/',
         views.job_title_detail, name='detail'),
]
