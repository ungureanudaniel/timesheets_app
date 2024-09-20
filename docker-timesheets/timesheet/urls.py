from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import timesheet_list
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import cache_page


urlpatterns = [
    # path('create_timesheet/', create_timesheet, name='create_timesheet'),
    path('', cache_page(60 * 15)(timesheet_list), name="timesheet_list"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
