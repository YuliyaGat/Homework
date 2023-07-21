from django.contrib import admin
from django.urls import include, path
from users import views as user_views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('media/', include('media.urls', 'users.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #path( '', include('gsheets.urls')),
    # path('', RedirectView.as_view(url='/media/platform_usage/', permanent=True)),
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]

