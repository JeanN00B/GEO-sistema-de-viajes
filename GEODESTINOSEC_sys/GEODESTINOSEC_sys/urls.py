from django.contrib import admin
from django.urls import path, include
from core.views import index
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path("select2/", include("django_select2.urls")),
    path('', views.LoginView.as_view(template_name='sysuserprofile/login.html'), name='index'),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/clients/', include('clients.urls')),
    path('dashboard/analytics/', include('analytics.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(template_name='sysuserprofile/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)