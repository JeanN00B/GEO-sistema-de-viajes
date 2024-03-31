from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_visualize, name='clients'), #TODO HTML base for clients
    path('new-client/', views.clients_create, name='new_client'), #TODO create form -> clients
    path('search/', views.search_name, name='search_name'),    # - search engine of clients
    path('<pk>/', views.clients_read_update, name='clients_read_update'),#TODO update form -> clients

    path('visa/<pk>/', views.visa_create, name='visa_create'), #TODO create form -> visa
    path('visa-delete/<pk>/', views.visa_delete, name='visa_delete'), #TODO delete form -> visa
    path('visa-loading/<pk>/', views.visa_loading, name='visa_loading'), #TODO HTML base for visa
    path('passport/<pk>/', views.passport_create, name='passport_create'), #TODO create form -> passport
    path('passport-delete/<pk>/', views.passport_delete, name='passport_delete'), #TODO delete form -> passport
    path('passport-loading/<pk>/', views.passport_loading, name='passport_loading'), #TODO HTML base for passport
    ]