from django.contrib import admin

from .models import Category, Question, Answer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'possible_ticket_numbers', 'get_questions']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'text', 'correct', 'category', 'get_answers',]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'content', 'correct', 'question',]
