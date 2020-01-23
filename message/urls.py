from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_list),
    path('<int:pk>/', views.detail_text),
]