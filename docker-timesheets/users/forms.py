from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser, UserProfile
from django.contrib.auth import get_user_model # why this here?
from django.utils.translation import gettext_lazy as _

User = get_user_model() # why this?

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            # Apply Bootstrap classes and custom styles to form fields
            self.fields['username'].widget.attrs.update({
                'class': 'form-control w-100',
                'placeholder': _('Enter username'),
            })
            self.fields['email'].widget.attrs.update({
                'class': 'form-control d-flex p-2 bd-highlight',
                'placeholder': _('Enter email'),
            })
            self.fields['password1'].widget.attrs.update({
                'class': 'form-control d-flex p-2 bd-highlight',
                'placeholder': _('Enter password'),
            })
            self.fields['password2'].widget.attrs.update({
                'class': 'form-control d-flex p-2 bd-highlight',
                'placeholder': _('Confirm password'),
            })

        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_approved = False  # Set new user as unapproved by default
            if commit:
                user.save()
                user.assign_initial_group()
            return user
#==============user update form=============
class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            # Apply Bootstrap classes and custom styles to form fields
            self.fields['first_name'].widget.attrs.update({
                'class': 'form-control w-100',
                'placeholder': _('Enter first name'),
            })
            self.fields['last_name'].widget.attrs.update({
                'class': 'form-control w-100',
                'placeholder': _('Enter last name'),
            })
            self.fields['email'].widget.attrs.update({
                'class': 'form-control d-flex p-2 bd-highlight',
                'placeholder': _('Enter email'),
            })
    def save(self, commit=True):
            user = super().save(commit=False)
            user.is_approved = False  # Set new user as unapproved by default
            if commit:
                user.save()
                user.assign_initial_group()
            return user
#==============password change form=============
class PasswordChangeForm(PasswordChangeForm):
    pass
#==============profile edit form=============
class ProfileChangeForm(forms.ModelForm):
   class Meta:
        model = UserProfile
        fields = ['bio', 'avatar', 'resume']
        
        def __init__(self, *args, **kwargs):
            user = kwargs.pop('user', None)
            super().__init__(*args, **kwargs)

            if user:
                self.fields['avatar'].initial = user.userprofile.avatar
                self.fields['bio'].initial = user.userprofile.bio
                self.fields['resume'].initial = user.userprofile.resume
            
            # Apply Bootstrap classes and custom styles to form fields
            self.fields['bio'].widget.attrs.update({
                'class': 'form-control d-flex p-2 bd-highlight',
                'placeholder': _('Attach resume'),
            })
            self.fields['avatar'].widget.attrs.update({
                'class': 'form-control d-flex p-2 bd-highlight',
                'placeholder': _('Attach picture of you'),
            })
            self.fields['resume'].widget.attrs.update({
                'class': 'form-control d-flex p-2 bd-highlight',
                'placeholder': _('Attach a new resume'),
            })

        def save(self, commit=True):
            user_profile = super().save(commit=False)
            if commit:
                user_profile.save()
            return user_profile