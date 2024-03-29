from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from .views import CustomLoginView, LoginRecovery, processar_formulario


urlpatterns = [
    path('', include('app.urls')),
    # path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='custom-login'),
    path('login/pass-recovery', LoginRecovery.as_view(), name='login-recovery'),
    path('processar-formulario/', processar_formulario, name='processar_formulario'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
