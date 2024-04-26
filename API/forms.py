from django.forms import ModelForm
from .models import User, Task
from django import forms

class UserRegisterForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'username', 'email']  # Exclude 'password' and 'password1' fields

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password and password1 and password != password1:
            raise forms.ValidationError("Passwords do not match")
        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','name']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
