from django.urls import path
from . import views


urlpatterns = [
    path('<int:customer_id>/', views.home, name='home'),
    path('about/', views.about, name='about')
]