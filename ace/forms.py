from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('category', 'company_name', 'contact_person', 'phone_number', 'country', 'city',)
        widgets = {
        'phone_number': forms.TextInput(attrs={'placeholder': 'including international code e.g. +1 647 123 0000'})
        }