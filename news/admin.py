
# Register your models here.
from django.contrib import admin
from .models import Category, Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('name_post', 'date_post')
	list_filter = ('date_post',)
	search_fields = ('name_post',)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)