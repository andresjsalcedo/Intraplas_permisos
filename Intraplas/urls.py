from django.urls import path
from .views import registrointraplas, loginintraplas, logoutintraplas, adminpanel
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('registrointraplas', registrointraplas, name='registrointraplas'),
    path('', loginintraplas, name='loginintraplas'),
    path('logoutintraplas', logoutintraplas, name='logoutintraplas'),
    path('adminpanel', adminpanel, name='adminpanel'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)