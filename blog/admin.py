from django.contrib import admin
from .models import Blog
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'created_time', 'last_updated_time','create_month')
