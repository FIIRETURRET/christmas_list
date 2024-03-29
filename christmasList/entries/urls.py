from django.urls import path

from . import views

app_name = 'entries'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:gift_id>/', views.detail, name='detail'),
    path('all/', views.indexAll, name='indexAll'),
]