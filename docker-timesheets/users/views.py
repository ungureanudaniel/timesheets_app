from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from .forms import UsernameEmailChangeForm
from django.urls import reverse
from .forms import ProfileChangeForm
# ,CustomSignupForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib import messages
from .models import *
from django.contrib.auth import update_session_auth_hash
from django.views.generic import View
from django.db import transaction
from allauth.account.views import SignupView
from django.contrib.auth.models import Group


# ==============user registration view============
class CustomSignupView(SignupView):
    template = 'account/signup.html'

    def form_valid(self, form):
        # Call the original form_valid method
        response = super().form_valid(form)

        # Get the user and assign them to a default group
        user = form.save(self.request)
        group = Group.objects.get(name='REPORTER')
        user.groups.add(group)
        user.save()

        return response


# def register(request):
#     if request.method == 'POST':
#         form = CustomSignupForm(request.POST)  # access the registration form
#         try:
#             if form.is_valid():
#                 # fetch username and email from form
#                 username = form.cleaned_data['username']
#                 email = form.cleaned_data['email']
#                 # Check if user already exists
#                 try:
#                     if User.objects.filter(username=username).exists():
#                         messages.error(request, 'Username already exists. Please choose a different username.')
#                     elif User.objects.filter(email=email).exists():
#                         messages.error(request, 'Email address already exists. Please use a different email.')
#                     else:
#                         # If the username and email are unique, save the user and create a profile
#                         with transaction.atomic():
#                             user = form.save(commit=False)
#                             user.is_active = False  # to keep the account inactive until approved manually by admins
#                             user.save()

#                         # Notify admins and supervisors via email
#                         subject = 'New User Access Request'
#                         html_message = render_to_string('registration/registration_notice_email.html', {
#                             'username': user.username,
#                             'email': user.email,
#                         })
#                         plain_message = strip_tags(html_message)
#                         admins = User.objects.filter(groups__name='ADMIN').values_list('email', flat=True)
#                         supervisors = User.objects.filter(groups__name='SUPERVISOR').values_list('email', flat=True)

#                         recipients = list(admins) + list(supervisors)

#                         send_mail(
#                             subject,
#                             plain_message,
#                             settings.EMAIL_HOST_USER,  # Sender's email address
#                             recipients,
#                             html_message=html_message,
#                         )

#                         # success message
#                         messages.warning(request, 'Registration successful. Your account is pending admin approval.')

#                         # redirect the user to login into the profile page with newly created credentials, but with an inactive account
#                         return render(request, 'registration/profile.html')
#                 except Exception as e:
#                     print(f'Error: {e}')
#             else:
#                 # If form is invalid, print form errors to the console (optional) and display messages
#                 for field, errors in form.errors.items():
#                     for error in errors:
#                         messages.error(request, f"{field}: {error}")
#         except Exception as e:
#             messages.error(request, e)
#     else:
#         form = CustomSignupForm()

#     return render(request, 'registration/register.html', {'form': form})


# ==============user login view==============
class CustomLoginView(LoginView):
    template_name = 'account/login.html'  # The path to your custom login template
    authentication_form = AuthenticationForm  # Use Django's default AuthenticationForm
    redirect_authenticated_user = True  # Redirect user if already authenticated
    success_url = reverse_lazy('timesheets:dashboard')  # Redirect after login

    def form_valid(self, form):
        # If you want to add any additional logic before the form is validated, you can do it here.
        return super().form_valid(form)


# ==============user profile view============
class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'registration/profile.html'
    context_object_name = 'user'

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(CustomUser, username=username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()

        # Check if the user's email is confirmed
        email_address = EmailAddress.objects.filter(user=user, primary=True).first()
        if email_address and not email_address.verified:
            # If email is not confirmed, limit the information displayed
            context['show_limited_info'] = True
        else:
            context['show_limited_info'] = False

        return context


# ============user profile editing====================
# @login_required
# def profile_edit_view(request, username):
#     template_name = 'registration/profile_updater.html'
#     # Fetch the user instance
#     user = get_object_or_404(User, username=username)

#     # Fetch or create UserProfile instance for the user

#     user_profile, created = CustomUser.objects.get_or_create(user=user)

#     if request.method == 'POST':
#         form = ProfileChangeForm(request.POST, request.FILES, instance=user_profile)
#         if form.is_valid():
#             # form.save(commit=False)
#             form.save()
#             return redirect('profile', username=username)
#     else:
#         form = ProfileChangeForm(instance=user_profile)

#     context = {
#         'user':user,
#         'avatar_url': user_profile.avatar.url if user_profile.avatar else None,
#         'form': form,}

#     return render(request, template_name, context)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileChangeForm
    template_name = 'registration/profile_updater.html'

    def get_success_url(self):
        # Redirect to the profile page of the current user after successful update
        return reverse('profile', kwargs={'username': self.request.user.username})

    def get_object(self):
        # Retrieve the current user object
        return self.request.user


# ==============user credentials change view=====================
@login_required
def user_change_view(request, username):
    # Fetch the user instance
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        user_form = UsernameEmailChangeForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your credentials have been successfully updated.')
            return redirect('profile', username=request.user.username)
    else:
        user_form = UsernameEmailChangeForm(instance=request.user)

    return render(request, 'registration/credentials_change.html', {'form': user_form, 'user': user})


@login_required
def password_change_view(request, username):
    # Fetch the user instance
    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        password_form = PasswordChangeForm(user=request.user, data=request.POST)

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important for keeping the user logged in

            messages.success(request, 'Your password has been successfully updated.')
            return redirect('profile', username=request.user.username)
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'registration/password_change.html', {'form': form, 'user': user})
