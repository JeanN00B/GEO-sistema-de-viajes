from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_visualize, name='clients'), #TODO HTML base for clients
    path('new-client/', views.clients_create, name='new_client'), #TODO create form -> clients
    path('search/', views.search_name, name='search_name'),    # - search engine of clients
    path('<pk>/', views.clients_read_update, name='clients_read_update'),#TODO update form -> clients
    ]