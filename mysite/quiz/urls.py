from django.contrib import admin
from django.urls import path

from quiz.forms import AnswerForm
from quiz.views import category_list, TicketsWizard

urlpatterns = [
    path('', category_list, name='category_list'),
    # path('ticket/<int:pk>/', TicketsWizard.as_view([AnswerForm, AnswerForm]), name='ticket'),
    path('ticket/<int:pk>/', TicketsWizard.as_view(), name='ticket'),

]