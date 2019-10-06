from django import forms
from . import models

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = [
            'first_name',
            'last_name',
            'email',
            'date_of_birth',
            'bio',
            'avatar',
        ]
