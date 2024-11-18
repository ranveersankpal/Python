# user_validation/forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'age']

    # Custom validation for the 'name' field (ensure it's at least 3 characters)
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('Name must be at least 3 characters long.')
        return name

    # Custom validation for the 'age' field (ensure it's a positive integer)
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age <= 0:
            raise forms.ValidationError('Age must be a positive number.')
        return age

    # Custom validation for the 'email' field (ensure it's unique)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserProfile.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email
