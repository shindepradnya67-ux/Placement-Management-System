from django import forms
from .models import Student, Company, Job, JobApplication


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'email',
            'password',
            'phone',
            'address',
            'qualification',
            'skills',
            'experience',
            'domain',
            'hobbies',
            'certification',
            'projects',
            'linkedin',
            'github',
            'portfolio',
            'photo',
            'resume',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'qualification': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
            'domain': forms.TextInput(attrs={'class': 'form-control'}),
            'hobbies': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'certification': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'projects': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'portfolio': forms.URLInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'company_name',
            'location',
            'email',
            'phone',
        ]

        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'company',
            'position',
            'domain',
            'qualification',
            'package',
            'location',
            'contract_type',
            'skills',
            'experience',
        ]

        widgets = {
            'company': forms.Select(attrs={'class': 'form-select'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'domain': forms.TextInput(attrs={'class': 'form-control'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control'}),
            'package': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'contract_type': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
        }


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'student',
            'job',
        ]

        widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'job': forms.Select(attrs={'class': 'form-select'}),
        }


class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'status',
        ]

        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
        }


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )