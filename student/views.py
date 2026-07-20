from django.shortcuts import render, redirect
from .models import Student, Company, Job, JobApplication
from .forms import (
    StudentForm,
    CompanyForm,
    JobForm,
    JobApplicationForm,
    ApplicationStatusForm,
    LoginForm
)


# ===========================
# Home Dashboard
# ===========================

def home(request):

    context = {
        'student_count': Student.objects.count(),
        'company_count': Company.objects.count(),
        'job_count': Job.objects.count(),
        'application_count': JobApplication.objects.count(),
    }

    return render(request, 'home.html', context)


# ===========================
# Student Module
# ===========================

def register(request):

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = StudentForm()

    return render(request, "register.html", {"form": form})


def student_list(request):

    search = request.GET.get("search")

    if search:
        students = Student.objects.filter(name__icontains=search)
    else:
        students = Student.objects.all()

    return render(
        request,
        "student_list.html",
        {"students": students}
    )


def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "register.html",
        {"form": form}
    )


def delete_student(request, id):

    student = Student.objects.get(id=id)
    student.delete()

    return redirect("student_list")


def opt_out(request, id):

    student = Student.objects.get(id=id)
    student.placement_status = "Opt Out"
    student.save()

    return redirect("student_list")


# ===========================
# Company Module
# ===========================

def company_register(request):

    if request.method == "POST":

        form = CompanyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("company_list")

    else:
        form = CompanyForm()

    return render(
        request,
        "company_register.html",
        {"form": form}
    )


def company_list(request):

    companies = Company.objects.all()

    return render(
        request,
        "company_list.html",
        {"companies": companies}
    )


def edit_company(request, id):

    company = Company.objects.get(id=id)

    if request.method == "POST":

        form = CompanyForm(
            request.POST,
            instance=company
        )

        if form.is_valid():
            form.save()
            return redirect("company_list")

    else:
        form = CompanyForm(instance=company)

    return render(
        request,
        "company_register.html",
        {"form": form}
    )


def delete_company(request, id):

    company = Company.objects.get(id=id)
    company.delete()

    return redirect("company_list")


# ===========================
# Job Module
# ===========================

def job_register(request):

    if request.method == "POST":

        form = JobForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("job_list")

    else:
        form = JobForm()

    return render(
        request,
        "job_register.html",
        {"form": form}
    )


def job_list(request):

    jobs = Job.objects.all()

    return render(
        request,
        "job_list.html",
        {"jobs": jobs}
    )


def edit_job(request, id):

    job = Job.objects.get(id=id)

    if request.method == "POST":

        form = JobForm(
            request.POST,
            instance=job
        )

        if form.is_valid():
            form.save()
            return redirect("job_list")

    else:
        form = JobForm(instance=job)

    return render(
        request,
        "job_register.html",
        {"form": form}
    )


def delete_job(request, id):

    job = Job.objects.get(id=id)
    job.delete()

    return redirect("job_list")


# ===========================
# Job Application Module
# ===========================

def apply_job(request):

    if request.method == "POST":

        form = JobApplicationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("application_list")

    else:
        form = JobApplicationForm()

    return render(
        request,
        "apply_job.html",
        {"form": form}
    )


def application_list(request):

    applications = JobApplication.objects.all()

    return render(
        request,
        "application_list.html",
        {"applications": applications}
    )


# ===========================
# Application Status
# ===========================

def edit_application_status(request, id):

    application = JobApplication.objects.get(id=id)

    if request.method == "POST":

        form = ApplicationStatusForm(
            request.POST,
            instance=application
        )

        if form.is_valid():
            form.save()
            return redirect("application_list")

    else:
        form = ApplicationStatusForm(instance=application)

    return render(
        request,
        "application_status.html",
        {"form": form}
    )


# ===========================
# Login Module
# ===========================

def login(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                Student.objects.get(
                    email=email,
                    password=password
                )

                return redirect("home")

            except Student.DoesNotExist:

                return render(
                    request,
                    "login.html",
                    {
                        "form": form,
                        "error": "Invalid Email or Password"
                    }
                )

    else:
        form = LoginForm()

    return render(
        request,
        "login.html",
        {"form": form}
    )


# ===========================
# Eligible Jobs
# ===========================

def eligible_jobs(request):

    jobs = Job.objects.all()

    return render(
        request,
        "eligible_jobs.html",
        {"jobs": jobs}
    )