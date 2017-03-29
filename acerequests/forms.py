from django import forms
from django_countries import countries

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)
    company_name = forms.CharField(required=True)
    country = forms.ChoiceField(countries)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )