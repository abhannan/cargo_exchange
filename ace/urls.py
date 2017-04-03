
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="home"),
    url(r'^accounts/activate/complete/', views.registration_complete, name='reg_complete'),
    url(r'^accounts/update-profile/', views.update_profile, name='profile_update'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^terms-of-service/', views.terms_of_service, name='terms'),
    url(r'^about/', views.about_us, name='about_us'),
]
