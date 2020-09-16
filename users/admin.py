from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
   list_display = ['get_user', 'created', 'updated']
   
   def get_user(self, obj):
      return obj.user.username
   
admin.site.register(Profile, ProfileAdmin)
