from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import CustomSignupView, CustomLoginView, user_change_view, password_change_view, ProfileView, ProfileEditView
from django.utils.translation import gettext_lazy as _

urlpatterns = [
        # path('register/', register, name='register'),
        path('accounts/signup/', CustomSignupView.as_view(), name='custom_signup'),
        path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
        path('profile/<str:username>/edit/', ProfileEditView.as_view(), name='profile_edit'),
        path('profile/<str:username>/change_username/', user_change_view, name='credentials_change'),
        path('password/<str:username>/change_password/', password_change_view, name='password_change'),
        # path('inactive-profile/', profile, name='awaiting-approval'),
        path('login/', CustomLoginView.as_view(), name='login'),  # Custom LoginView
        path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
        ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)