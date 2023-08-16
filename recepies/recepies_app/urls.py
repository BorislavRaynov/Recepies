from django.urls import path
from .models import Recepie
from .views import home_page, create_recepie, edit_recepie, recepie_details, delete_recepie

urlpatterns = [
    path('', home_page, name='home-page'),
    path('create/', create_recepie, name='create-recepie'),
    path('edit/<int:recepie_id>', edit_recepie, name='edit-recepie'),
    path('details/<int:recepie_id>', recepie_details, name='recepie-details'),
    path('delete/<int:recepie_id>', delete_recepie, name='delete-recepie')
]