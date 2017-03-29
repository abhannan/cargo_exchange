from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyUserManager(BaseUserManager):

	    def _create_user(self, email, password, **extra_fields):
	    	if not email:
	    		raise ValueError('The Email must be set')
	    	email = self.normalize_email(email)
	    	user = self.model(email=email, **extra_fields)
	    	user.set_password(password)
	    	user.save()
	    	return user

	    def create_superuser(self, email, password, **extra_fields):
	    	extra_fields.setdefault('is_staff', True)
	    	extra_fields.setdefault('is_superuser', True)
	    	extra_fields.setdefault('is_active', True)

	    	if extra_fields.get('is_staff') is not True:
	    		raise ValueError('Superuser must have is_staff=True.')
	    	if extra_fields.get('is_superuser') is not True:
	    		raise ValueError('Superuser must have is_superuser=True.')

	    	return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True, null=True)
    date_joined = models.DateTimeField(default=datetime.now)

    is_staff = models.BooleanField(
    	_('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email'

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class UserProfile(models.Model):
    
    CLIENT_CATEGORY = (
    ('Airline', 'Airline'),
    ('Broker', 'Broker / Freight Forwarder'),)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.CharField(choices=CLIENT_CATEGORY, max_length=26)
    company_name = models.CharField(max_length=500)
    contact_person = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    country = CountryField()
    city = models.CharField(max_length=500)

    def __str__(self):
        return self.company_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
