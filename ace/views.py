from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from registration.backends.default.views import RegistrationView
from django.views.generic import TemplateView

class IndexView(RegistrationView, TemplateView):
	template_name = "ace/index.html"

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context["game_today"] = 6
	# 	return context
# 	success_url = 'accounts/register/complete/'


@login_required
@transaction.atomic
def update_profile(request):
	if request.method == 'POST':
		profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
		if profile_form.is_valid():
			profile_form.save()
			messages.success(request, _('Your profile was successfully updated!'))
			return redirect('home')
		else:
			messages.error(request,_('Please correct the error'))
	else:
		profile_form = ProfileForm(instance=request.user.userprofile)

	return render(request, 'registration/activation_complete.html', {'profile_form': profile_form})

