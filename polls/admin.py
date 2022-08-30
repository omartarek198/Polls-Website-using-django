from django.contrib import admin
from .models import Choice, Question


# admin.site.register(Question)

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields': ['question']})]
    inlines = [ChoiceInLine]


admin.site.register(Question,QuestionAdmin)


# Register your models here.
