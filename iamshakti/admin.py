from django.contrib import admin
from .models import Story
from .models import JTMUser

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author', 'cwarning', 'tags', 'text')
    prepopulated_fields = {'slug' : ('title',)}

@admin.register(JTMUser)
class JTMUserAdmin(admin.ModelAdmin):
    search_fields = ('firstName', 'lastName', 'email', 'interests', 'memberType')
