from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from team_member import views

urlpatterns = [
    path('team_member/', include('team_member.urls')),
    path('admin/', admin.site.urls),
    path('', views.list),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
