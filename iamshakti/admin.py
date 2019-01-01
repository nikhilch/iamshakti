from django.contrib import admin
from .models import Story

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author', 'cwarning', 'tags', 'text')
    prepopulated_fields = {'slug' : ('title',)}

