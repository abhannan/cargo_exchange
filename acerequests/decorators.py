from django.core.exceptions import PermissionDenied
from .models import AircraftAvailability, FreightAvailability

def aircraft_permission_required(function):
    def wrap(request, *args, **kwargs):
    	# freight_request = FreightAvailability.objects.get(pk=kwargs['pk'])
    	aircraft_request = AircraftAvailability.objects.get(pk=kwargs['pk'])
    	if aircraft_request.user == request.user:
    		return function(request, *args, **kwargs)
    	else:
        	raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def freight_permission_required(function):
    def wrap(request, *args, **kwargs):
    	freight_request = FreightAvailability.objects.get(pk=kwargs['pk'])
    	if freight_request.user == request.user:
    		return function(request, *args, **kwargs)
    	else:
        	raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
