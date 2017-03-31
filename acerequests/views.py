from django import forms
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse_lazy
from .forms import ContactForm
from django.http import Http404, HttpResponseRedirect
from .mixins import AirportDataMixin
from .models import AircraftAvailability, FreightAvailability
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import (CreateView,
                                  UpdateView,
                                  DeleteView,
                                  ListView,
                                  DetailView)
from datetimewidget.widgets import DateWidget

### Forms ###
class AircraftRequestForm(forms.ModelForm):
    class Meta:
        model = AircraftAvailability
        fields = ('from_airport',
                  'to_airport',
                  'aircraft_type',
                  'date_required',
                  'max_payload',
                  'max_volume',
                  'door_size',
                  'max_pallets',
                  'comments')
        widgets = {'date_required': DateWidget(attrs={'id': "id_date_required"}, usel10n=True),
                   'from_airport': forms.TextInput(attrs={'placeholder': 'Type name or IATA code'}),
                   'to_airport': forms.TextInput(attrs={'placeholder': 'Type name or IATA code'}),
                   'may_payload': forms.TextInput(attrs={'placeholder': 'in KGs'}),
                   'max_volume': forms.TextInput(attrs={'placeholder': 'in CBM    e.g. 700 cbm'}),
                   'door_size': forms.TextInput(attrs={'placeholder': 'W X H (CM)  e.g. 340cm x 312cm'}),
                   'max_pallets': forms.TextInput(attrs={'placeholder': 'L X W X H (CM)  e.g. 1150cm x 220cm x 175cm'}),

                   }
        labels = {
            'from_airport': 'Origin Airport *',
            'to_airport': 'Destination Airport *',
            'aircraft_type': 'Aircraft Type *',
            'date_required': 'Date Required *',
            'max_payload': 'Max Payload (in KGs)',
            'max_volume': 'Max Volume',
            'door_size': 'Door Size',
            'max_pallets': 'Max Pallets',
        }
        help_texts = {
            'comments': '* Required Fields'}


class FreightRequestForm(forms.ModelForm):
    class Meta:
        model = FreightAvailability
        fields = ('cargo_type',
                  'cargo_nature',
                  'from_airport',
                  'to_airport',
                  'aircraft_type',
                  'date_required',
                  'max_payload',
                  'max_volume',
                  'number_pallets',
                  'comments')
        widgets = {'date_required': DateWidget(attrs={'id': "id_date_required"}, usel10n=True),
                   'from_airport': forms.TextInput(attrs={'placeholder': 'Type name or IATA code'}),
                   'to_airport': forms.TextInput(attrs={'placeholder': 'Type name or IATA code'}),
                   'may_payload': forms.TextInput(attrs={'placeholder': 'in KGs'}),
                   'max_volume': forms.TextInput(attrs={'placeholder': 'in CBM    e.g. 700 cbm'}),
                   'number_pallets': forms.TextInput(attrs={'placeholder': 'Number of PCS/SKIDS/PALLETS'}),

                   }
        labels = {
            'from_airport': 'Origin Airport *',
            'to_airport': 'Destination Airport *',
            'aircraft_type': 'Aircraft Type *',
            'date_required': 'Date Required *',
            'max_payload': 'Max Payload (in KGs)',
            'max_volume': 'Max Volume',
            'cargo_type': 'Cargo Type *',
            'cargo_nature': 'Cargo Nature',
            'max_pallets': 'No. of Pallets',
        }
        help_texts = {
            'comments': '* Required Fields'}


### Create ###

class AircraftCreateView(AirportDataMixin, CreateView):
    form_class = AircraftRequestForm
    model = AircraftAvailability

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            aircraft_request = form.save(commit=False)
            aircraft_request.user = request.user
            aircraft_request.save()
            return redirect('profile_list_view')
        else:
            return self.form_invalid(form)


class FreightCreateView(AirportDataMixin, CreateView):
    form_class = FreightRequestForm
    model = FreightAvailability

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            freight_request = form.save(commit=False)
            freight_request.user = request.user
            freight_request.save()
            return redirect('profile_list_view')
        else:
            return self.form_invalid(form)


### Edit ###
class AircraftUpdateView(AirportDataMixin, UpdateView):
    model = AircraftAvailability
    fields = ('from_airport',
              'to_airport',
              'aircraft_type',
              'date_required',
              'max_payload',
              'max_volume',
              'door_size',
              'max_pallets',
              'comments')


class FreightUpdateView(AirportDataMixin, UpdateView):
    model = FreightAvailability
    fields = ('from_airport',
              'to_airport',
              'aircraft_type',
              'date_required',
              'max_payload',
              'max_volume',
              'cargo_type',
              'cargo_nature',
              'number_pallets',
              'comments')


### Delete ###

class AircraftDeleteView(DeleteView):
    model = AircraftAvailability
    success_url = reverse_lazy("profile_list_view")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.success_url
        self.object.delete()
        return HttpResponseRedirect(success_url)


class FreightDeleteView(DeleteView):
    model = FreightAvailability
    success_url = reverse_lazy("profile_list_view")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.success_url
        self.object.delete()
        return HttpResponseRedirect(success_url)


### View Data ###

def profile_list_view(request):
    if request.user.is_authenticated:
        user = request.user
        user_aircraft_requests = AircraftAvailability.objects.filter(user=user).order_by("-date_posted")
        user_freight_requests = FreightAvailability.objects.filter(user=user).order_by("-date_posted")
    else:
        raise Http404

    return render(request, 'acerequests/profile_list_view.html', {
        'user_aircraft_requests': user_aircraft_requests, 'user_freight_requests': user_freight_requests})


### Dashboard ###

def dashboard_view_external(request):
    aircraft_requests = AircraftAvailability.objects.filter().order_by("-date_posted")[:3]
    freight_requests = FreightAvailability.objects.filter().order_by("-date_posted")[:3]

    return render(request, 'acerequests/dashboard_external.html', {
        'aircraft_requests': aircraft_requests,
        'freight_requests': freight_requests
    })


def dashboard_view_users(request):
    aircraft_requests = AircraftAvailability.objects.filter().order_by("-date_posted")
    freight_requests = FreightAvailability.objects.filter().order_by("-date_posted")

    return render(request, 'acerequests/dashboard_users.html', {
        'aircraft_requests': aircraft_requests,
        'freight_requests': freight_requests
    })


def aircraft_detail_view(request, pk):
    aircraft_detail = AircraftAvailability.objects.get(pk=pk)
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            name = request.POST.get(
                'name'
                , '')
            email = request.POST.get(
                'email'
                , '')
            phone = request.POST.get(
                'phone'
                , '')
            company_name = request.POST.get(
                'company_name'
                , '')
            country = request.POST.get(
                'country'
                , '')
            content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('acerequests/contact_user.txt')
            context = Context({
                'name': name,
                'email': email,
                'phone': phone,
                'company_name': company_name,
                'country': country,
                'content': content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Air Cargo Exchange" + '',
                ['youremail@gmail.com'],
                headers={'Reply-To': email}
            )
            email.send()
            return redirect('dashboard_users')
    return render(request, 'acerequests/dashboard_aircraft_detail.html',
                  {'aircraft_detail': aircraft_detail, 'form': form_class})


def freight_detail_view(request, pk):
    freight_detail = FreightAvailability.objects.get(pk=pk)
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            name = request.POST.get(
                'name'
                , '')
            email = request.POST.get(
                'email'
                , '')
            content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('acerequests/contact_user.txt')
            context = Context({
                'name': name,
                'email': email,
                'content': content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'],
                headers={'Reply-To': email}
            )
            email.send()
            return redirect('dashboard_users')
    return render(request, 'acerequests/dashboard_freight_detail.html',
                  {'freight_detail': freight_detail, 'form': form_class})
