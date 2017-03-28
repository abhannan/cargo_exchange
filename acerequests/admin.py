from django.contrib import admin
from .models import AircraftAvailability, FreightAvailability

class AircraftAvailabilityAdmin(admin.ModelAdmin):
    model = AircraftAvailability
    list_display = ('user', 'from_airport', 'to_airport', 'aircraft_type', 'max_payload', 'max_volume', 'date_required', 'date_posted', 'door_size', 'max_pallets', 'comments')

class FreightAvailabilityAdmin(admin.ModelAdmin):
    model = FreightAvailability
    list_display = ('user', 'from_airport', 'to_airport', 'aircraft_type', 'max_payload', 'max_volume', 'date_required', 'date_posted', 'cargo_type', 'cargo_nature', 'number_pallets', 'comments')

admin.site.register(AircraftAvailability, AircraftAvailabilityAdmin)
admin.site.register(FreightAvailability, FreightAvailabilityAdmin)