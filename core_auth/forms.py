from django import forms

from django.contrib.auth import password_validation

from . import models

class SignUp(forms.ModelForm):
    password = forms.CharField(required=True, validators=[password_validation.CommonPasswordValidator, password_validation.MinimumLengthValidator(8), password_validation.MinimumLengthValidator(16),], max_length=16, widget=forms.PasswordInput(attrs={'class': 'bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(required=True, max_length=16, widget=forms.PasswordInput(attrs={'class': 'bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = models.User
        fields = ("email", "first_name", 'last_name', 'username', 'age', 'profile_pic')

    def __init__(self, *args, **kwargs):
        super(SignUp, self).__init__(*args, **kwargs)

        self.fields['email'].widget = forms.TextInput(attrs={
            'id': 'email_input',
            'class': 'bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4',
            'placeholder': 'Email'
        })
        self.fields['first_name'].widget = forms.TextInput(attrs={
            'id': 'first_name_input',
            'class': 'bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4',
            'placeholder': 'First Name'
        })
        self.fields['last_name'].widget = forms.TextInput(attrs={
            'id': 'last_name_input',
            'class': 'bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4',
            'placeholder': 'Last Name'
        })
        self.fields['username'].widget = forms.TextInput(attrs={
            'id': 'username_input',
            'class': 'bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4',
            'placeholder': 'Username'
        })

        self.fields['username'].required = False

        self.fields['age'].widget = forms.TextInput(attrs={
            'id': 'age_input',
            'class': 'bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4',
            'placeholder': 'Age'
        })
        self.fields['profile_pic'].widget = forms.FileInput(attrs={
            'id': 'profile_pic_input',
            'class': 'bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4',
            'placeholder': 'Profile Pic'
        })
        self.fields['profile_pic'].label = 'Profile Pic'

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
            'id': 'email_input',
            'class': 'flex-grow w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mr-4 mb-4 sm:mb-0',
            'placeholder': 'Email'
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'id': 'pass_input',
            'class': 'flex-grow w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mr-4 mb-4 sm:mb-0',
            'placeholder': 'Password'
        }))
