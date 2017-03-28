from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('category', 'company_name', 'contact_person', 'phone_number', 'country', 'city',)
