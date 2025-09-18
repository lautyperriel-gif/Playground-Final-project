from django.urls import path
from . import views

app_name = 'messenger'

urlpatterns = [
    path('', views.inbox_view, name='inbox'),
    path('send/', views.send_view, name='send'),
]
