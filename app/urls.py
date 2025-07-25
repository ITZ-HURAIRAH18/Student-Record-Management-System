from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('add', views.add, name='add'),
    path('validate', views.validate, name='validate'),
    path('del/<int:id>/', views.delete, name='del'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('accounts/logout/', views.logout_user, name='logout'),

]
