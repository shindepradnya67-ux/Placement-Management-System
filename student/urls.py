from django.urls import path
from . import views

urlpatterns = [

    # ================= Home =================
    path('', views.home, name='home'),

    # ================= Student =================
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('students/', views.student_list, name='student_list'),
    path('eligible-jobs/', views.eligible_jobs, name='eligible_jobs'),

    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),

    # Opt Out
    path('opt-out/<int:id>/', views.opt_out, name='opt_out'),

    # ================= Company =================
    path('company/register/', views.company_register, name='company_register'),
    path('companies/', views.company_list, name='company_list'),
    path('company/edit/<int:id>/', views.edit_company, name='edit_company'),
    path('company/delete/<int:id>/', views.delete_company, name='delete_company'),

    # ================= Job =================
    path('job/register/', views.job_register, name='job_register'),
    path('jobs/', views.job_list, name='job_list'),
    path('job/edit/<int:id>/', views.edit_job, name='edit_job'),
    path('job/delete/<int:id>/', views.delete_job, name='delete_job'),

    # ================= Job Application =================
    path('apply/', views.apply_job, name='apply_job'),
    path('applications/', views.application_list, name='application_list'),
    path(
        'application/edit/<int:id>/',
        views.edit_application_status,
        name='edit_application_status'
    ),
]