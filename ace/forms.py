from django import forms
from .models import UserProfile
from django_countries import countries


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('category', 'company_name', 'contact_person', 'phone_number', 'country', 'city',)
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'including international code e.g. +1 647 123 0000'})
        }


class ContactUsForm(forms.Form):
    name = forms.CharField(required=True)
    company_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)
    country = forms.ChoiceField(countries)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
