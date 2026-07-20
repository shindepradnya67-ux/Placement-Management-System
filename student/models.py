from django.db import models


class Student(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Opt Out', 'Opt Out'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    qualification = models.CharField(max_length=100)
    skills = models.TextField()

    # Profile Completion
    experience = models.CharField(max_length=100, blank=True)
    domain = models.CharField(max_length=100, blank=True)
    hobbies = models.TextField(blank=True)
    certification = models.TextField(blank=True)
    projects = models.TextField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)

    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    # Opt Out
    placement_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Active'
    )

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.company_name


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    package = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contract_type = models.CharField(max_length=100)
    skills = models.TextField()
    experience = models.CharField(max_length=100)

    def __str__(self):
        return self.position


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Applied'
    )

    def __str__(self):
        return f"{self.student.name} - {self.job.position}"