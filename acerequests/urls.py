from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from .decorators import aircraft_permission_required, freight_permission_required


urlpatterns = [
	# Create #
    url(r'^create-aircraft-availability/$', login_required(views.AircraftCreateView.as_view()), name='create_aircraft'),
    url(r'^create-freight-availability/$', login_required(views.FreightCreateView.as_view()), name='create_freight'),
    # Edit #
    url(r'^edit-aircraft-availability/(?P<pk>\d+)/$', aircraft_permission_required(views.AircraftUpdateView.as_view()), name='update_aircraft'),
    url(r'^edit-freight-availability/(?P<pk>\d+)/$', freight_permission_required(views.FreightUpdateView.as_view()), name='update_freight'),
    # Delete #
    url(r'^delete-aircraft-availability/(?P<pk>\d+)/$', aircraft_permission_required(views.AircraftDeleteView.as_view()), name='delete_aircraft'),
    url(r'^delete-freight-availability/(?P<pk>\d+)/$', freight_permission_required(views.FreightDeleteView.as_view()), name='delete_freight'),
    # View Data #
    url(r'^my-profile/$', login_required(views.profile_list_view), name="profile_list_view"),
    # Dashboard #
    url(r'^dashboard-external/$', views.dashboard_view_external, name="dashboard_external"),
    url(r'^dashboard/$', login_required(views.dashboard_view_users), name="dashboard_users"),
    url(r'^aircraft-detail/(?P<pk>\d+)/$', login_required(views.aircraft_detail_view), name="aircraft_detail"),
    url(r'^freight-detail/(?P<pk>\d+)/$', login_required(views.freight_detail_view), name="freight_detail"),
]
