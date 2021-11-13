from django.contrib import admin

from .models import Question


# 검색창 만들기
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# Register your models here.
admin.site.register(Question, QuestionAdmin)