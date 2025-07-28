from django.urls import path
from . import views

urlpatterns = [
    path('', views.static_page, name='home'),
    path('about/', views.static_page, name='about'),
    path('catalog/', views.static_page, name='catalog'),
    path('contacts/', views.static_page, name='contacts'),
    path('about/team/', views.static_page, name='team'),
    path('about/team/about/', views.static_page, name='team_about_team'),
    path('offices/', views.static_page, name='offices')
]
