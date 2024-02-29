from django.contrib import admin
from django.urls import path, include
from core.views import index
from django.contrib.auth import views

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/clients/', include('clients.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.LoginView.as_view(template_name='sysuserprofile/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
