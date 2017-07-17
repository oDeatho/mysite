from django.contrib import admin

# Register your models here.
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):  
    list_display = ('title', 'timestamp')


admin.site.register(BlogPost, BlogPostAdmin)
