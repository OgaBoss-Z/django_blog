from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignUpForm(UserCreationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
   first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
   last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
   email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}))
   password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
   password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

   class Meta(UserCreationForm.Meta):
      model = User
      # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
      fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)


class UserUpdateForm(forms.ModelForm):
   first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}))
   about = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

   class Meta:
      model = User
      fields = ['first_name', 'last_name', 'email', 'about']















class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']