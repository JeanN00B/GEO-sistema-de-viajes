from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_visualize, name='clients'), #TODO HTML base for clients
    path('new-client/', views.clients_create, name='new_client'), #TODO create form -> clients
        # - search engine of clients
    #TODO update form -> clients

]