from django.contrib import admin
from. models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
   list_display = ['title', 'category', 'created', 'status', 'is_featured']
   list_editable = ['is_featured', 'status']
   prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
   list_display = ['title', 'created']
   prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category, CategoryAdmin)


''' class CommentAdmin(admin.ModelAdmin):
   list_display = ['user.username']
admin.site.register(Comment, CommentAdmin) '''


admin.site.register(Tag)
admin.site.register(Comment)

