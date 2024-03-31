from django.urls import path
from . import views

urlpatterns = [
    path('', views.analytics_index, name='analytics'),
    path('filter/', views.analytics_filter, name='analytics-filter'),
    path('filter/save/', views.analytics_filter_save, name='analytics-filter-save'),
    path('filter/update/<pk>/', views.analytics_filter_update, name='analytics-filter-update'),
    path('filter/delete/<pk>/', views.analytics_filter_delete, name='analytics-filter-delete'),
]