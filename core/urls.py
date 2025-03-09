




from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('summarize/<int:audio_id>/', views.summarize_audio, name='summarize_audio'),
]
