from django.db import models 
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
   title = models.CharField(max_length=150, null=True, blank=True, verbose_name="Title")
   slug = models.SlugField(max_length=160, null=True)
   created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
   updated = models.DateTimeField(auto_now=True, null=True, blank=True)
   

   class Meta:
      verbose_name = "Category"
      verbose_name_plural = "Categories"
      ordering = ['title']

   def __str__(self):
      return self.title
   
   def get_absolute_url(self):
      return reverse('post-category', kwargs={'pk': self.pk, 'slug': self.slug})

class Tag(models.Model):
   name = models.CharField(max_length=30)
   
   def __str__(self):
      return self.name
   
   
class Post(models.Model):
   STATUS_CHOICES = {
      ('draft', 'Draft'),
      ('published', 'Published'),
   }
   author = models.CharField(max_length=50, null=True, blank=True)
   title = models.CharField(max_length=150)
   slug = models.SlugField(max_length=160, null=True)
   category = models.ForeignKey(Category, null=True, blank=True, related_name='category', on_delete=models.CASCADE)
   content = RichTextUploadingField()
   like = models.PositiveIntegerField(default=0)
   image = models.ImageField(default='default.png', upload_to='post_img')
   tags = models.ManyToManyField(Tag)
   is_featured = models.BooleanField(default=False, verbose_name="Is Featured?")
   created = models.DateTimeField(default=timezone.now)
   updated = models.DateTimeField(auto_now=True)
   status = models.CharField(max_length=10, choices= STATUS_CHOICES, default='draft')

   def __str__(self):
      return self.title
   
   def publish(self):
      self.is_published = True
      self.published_at = timezone.now()
      self.save()
   
   def get_absolute_url(self):
      return reverse('post-detail', kwargs={'slug': self.slug}) 
   
   def get_related_posts_by_tags(self):
      return Post.objects.filter(tags__in=self.tags.all())
   
   
class Comment(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
   body = models.TextField()
   active = models.BooleanField(default=True)
   parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
   created = models.DateTimeField(default=timezone.now)
   updated = models.DateTimeField(auto_now=True)
   
   class Meta:
      verbose_name = "Comment"
      verbose_name_plural = "Comments"
      ordering = ['created']
   
   def __str__(self):
      return self.post.title
   

class UserPreference(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE)
   post= models.ForeignKey(Post, on_delete=models.CASCADE, related_name='preference')
   value= models.IntegerField()
   created = models.DateTimeField(default=timezone.now)
   
   def __str__(self):
      return str(self.user) + ':' + str(self.post) +':' + str(self.value)

   class Meta:
      unique_together = ("user", "post", "value")
   

   
   
   
   
   