from django.urls import path
from socmapp import views

urlpatterns = [
    path('about/', views.about),
    path('contact/', views.contact),
    path('wedding/', views.wedding),
    path('glamour/', views.glamour),
    path('hairstyle/', views.hairstyle),
    path('work/', views.work),
]
