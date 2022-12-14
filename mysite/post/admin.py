from django.contrib import admin
from .models import Post, Comment, Dessert
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', )
    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Dessert)

