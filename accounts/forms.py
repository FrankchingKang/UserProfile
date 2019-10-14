from django import forms
from . import models
import re

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
    def clean_date_of_birth(self):
        date_of_birth = str(self.cleaned_data.get('date_of_birth'))
        if re.match(r'\d{4}-\d{2}-\d{2}',date_of_birth) != None or \
            re.match(r'\d{2}\/\d{2}\/\d{4}',date_of_birth) !=None or \
            re.match(r'\d{2}\/\d{2}\/\d{2}',date_of_birth) !=None:
            return date_of_birth
        raise forms.ValidationError("""
            date format should be YYYY-MM-DD, MM/DD/YYYY, or MM/DD/Y """)
    def clean_email(self):
        email = str(self.cleaned_data.get('email'))
        if re.match(r'[-\w\d+.]+@[-\w\d.]+', email) != None:
            return email
        raise forms.ValidationError("""
            email is not valida
            """)
