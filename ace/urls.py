
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='home'),
    url(r'^$', views.IndexView.as_view(), name="home"),
    url(r'^accounts/activate/complete/', views.update_profile, name='profile_update'),
    url(r'^accounts/', include('registration.backends.default.urls')),
]
