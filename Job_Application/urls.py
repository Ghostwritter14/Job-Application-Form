from django.urls import path
from . import views

# call url for the landing page
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('Contact/', views.contact, name='contact')
]