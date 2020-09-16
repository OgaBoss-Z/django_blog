from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   image = models.ImageField(default='default.jpg', upload_to='profile_pics')
   about = models.TextField(null=True, blank=True)
   created = models.DateTimeField(auto_now=False, auto_now_add=True)
   updated = models.DateTimeField(auto_now=True, auto_now_add=False)

   def __str__(self):
      return f'{self.user.username}'

   def save(self, *args, **kwargs):
      super(Profile, self).save(*args, **kwargs)
