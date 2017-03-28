from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class AircraftAvailability(models.Model):
    REQ_AIRCRAFT = (
    ('A300', 'Airbus A300'),
    ('A310', 'Airbus A310'),
    ('A320', 'Airbus A320'),
    ('A330', 'Airbus A330'),
    ('AN12', 'Antonov AN12'),
    ('AN26', 'Antonov AN26'),
    ('AN32', 'Antonov AN32'),
    ('AN124', 'Antonov AN124'),
    ('AN225', 'Antonov AN225'),
    ('B727', 'Boeing 727'),
    ('B737', 'Boeing 737'),
    ('B747', 'Boeing 747'),
    ('B747-8', 'Boeing 747-8'),
    ('B757', 'Boeing 757'),
    ('B767', 'Boeing 767'),
    ('B777', 'Boeing 777'),
    ('Dash8', 'Bombardier Dash-8'),
    ('BAE146QT', 'British Aerospace 146QT'),
    ('BAEATPF', 'British Aerospace ATPF'),
    ('DC3', 'Douglas DC-3'),
    ('DC8', 'Douglas DC-8'),
    ('DC9', 'Douglas DC-9'),
    ('IL76', 'Ilyushin IL76'),
    ('IL96', 'Ilyushin IL96'),
    ('L100', 'Lockheed L100'),
    ('DC10', 'McDonnell Douglas DC10'),
    ('DC11', 'McDonnell Douglas DC11'),
    ('TU204', 'Tupolev TU204'),
    ('C208', 'Cessna Caravan'),
    ('LET410', 'LET 410'),
    ('SD330', 'Short 300'),
    ('ATR42', 'ATR 42'),
    ('ATR72', 'ATR 72'),
    ('Other', 'Other'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    from_airport = models.CharField(max_length=50, blank=False)
    to_airport = models.CharField(max_length=50, blank=False)
    aircraft_type = models.CharField(choices=REQ_AIRCRAFT, max_length=26, blank=False)
    max_payload = models.IntegerField(validators=[MaxValueValidator(200000), MinValueValidator(1)], null=True)
    max_volume = models.CharField(max_length=50, blank=True)
    date_required = models.DateField(blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    door_size = models.CharField(max_length=22, blank=True)
    max_pallets = models.CharField(max_length=22, blank=True)
    comments = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return self.aircraft_type

    def get_absolute_url(self):
        return reverse('profile_list_view')

    class Meta:
        verbose_name_plural = "Aircraft Availabilities"


class FreightAvailability(models.Model):
    REQ_AIRCRAFT = (
    ('no_pref', 'No Preference'),
    ('A300', 'Airbus A300'),
    ('A310', 'Airbus A310'),
    ('A320', 'Airbus A320'),
    ('A330', 'Airbus A330'),
    ('AN12', 'Antonov AN12'),
    ('AN26', 'Antonov AN26'),
    ('AN32', 'Antonov AN32'),
    ('AN124', 'Antonov AN124'),
    ('AN225', 'Antonov AN225'),
    ('B727', 'Boeing 727'),
    ('B737', 'Boeing 737'),
    ('B747', 'Boeing 747'),
    ('B747-8', 'Boeing 747-8'),
    ('B757', 'Boeing 757'),
    ('B767', 'Boeing 767'),
    ('B777', 'Boeing 777'),
    ('Dash8', 'Bombardier Dash-8'),
    ('BAE146QT', 'British Aerospace 146QT'),
    ('BAEATPF', 'British Aerospace ATPF'),
    ('DC3', 'Douglas DC-3'),
    ('DC8', 'Douglas DC-8'),
    ('DC9', 'Douglas DC-9'),
    ('IL76', 'Ilyushin IL76'),
    ('IL96', 'Ilyushin IL96'),
    ('L100', 'Lockheed L100'),
    ('DC10', 'McDonnell Douglas DC10'),
    ('DC11', 'McDonnell Douglas DC11'),
    ('TU204', 'Tupolev TU204'),
    ('C208', 'Cessna Caravan'),
    ('LET410', 'LET 410'),
    ('SD330', 'Short 300'),
    ('ATR42', 'ATR 42'),
    ('ATR72', 'ATR 72'),
    ('Other', 'Other'),
    )
    CARGO_TYPE = (
    ('auto_parts', 'Automotive & Aeronautical Spare Parts'),
    ('election_materials', 'Election Materials'),
    ('general', 'General Cargo'),
    ('hazardous', 'Hazardous Materials'),
    ('humanitarian', 'Humanitarian & Relief Cargo'),
    ('live_stock', 'Live Stock'),
    ('luxury', 'Luxury Goods'),
    ('military', 'Military Support Equipment'),
    ('musical_band', 'Musical Band Tours'),
    ('oil_gas', 'Oil & Gas Industry Equipment'),
    ('perishable', 'Perishable Goods'),
    ('security_sensitive', 'Security Sensitive Monetary Cargo'),
    ('telecom_equipment', 'Telecommunications Equipment'),
    ('other', 'Other'),
    )
    CARGO_NATURE = (
    ('normal', 'Normal'),
    ('over_weight', 'Over Weight'),
    ('time_sensitive', 'Time Sensitive'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    from_airport = models.CharField(max_length=50, blank=False)
    to_airport = models.CharField(max_length=50, blank=False)
    aircraft_type = models.CharField(choices=REQ_AIRCRAFT, max_length=26, blank=False)
    max_payload = models.IntegerField(validators=[MaxValueValidator(200000), MinValueValidator(1)], null=True)
    max_volume = models.CharField(max_length=50, blank=True)
    date_required = models.DateField(blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    cargo_type = models.CharField(choices=CARGO_TYPE, max_length=26, blank=False)
    cargo_nature = models.CharField(choices=CARGO_NATURE, max_length=26, blank=True)
    number_pallets = models.IntegerField(validators=[MaxValueValidator(200), MinValueValidator(1)], null=True)
    comments = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return self.aircraft_type

    def get_absolute_url(self):
        return reverse('profile_list_view')

    class Meta:
        verbose_name_plural = "Freight Availabilities"















