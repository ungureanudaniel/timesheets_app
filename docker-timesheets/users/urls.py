from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from users.views import register, profile, CustomLoginView, profile_edit_view, user_change_view, password_change_view
from django.utils.translation import gettext_lazy as _

urlpatterns = [
        path('register/', register, name='register'),
        path('profile/<str:username>/', profile, name='profile'),
        path('profile/<str:username>/edit/', profile_edit_view, name='profile_edit'),
        path('profile/<str:username>/change_username/', user_change_view, name='credentials_change'),
        path('password/<str:username>/change_password/', password_change_view, name='password_change'),
        path('inactive-profile/', profile, name='awaiting-approval'),
        path('login/', CustomLoginView.as_view(), name='login'),  # Custom LoginView
        path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
        ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)