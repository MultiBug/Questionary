from django.contrib import admin
from django.urls import path, include
from Participants.views import *


app_name = 'Participants'
urlpatterns = [
    path('participants/create/', ParticipantsCreateView.as_view()),
    path('all/', ParticipantsListView.as_view()),
    path('participants/detail/<int:pk>/', ParticipantsDetailView.as_view()),
]
