from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.db.models import Count
from .forms import CommentForm
from django.db.models import Q
from post.models import Post, Tag, Category, Comment



def home(request):
   category = Category.objects.all()
   feature = Post.objects.filter(is_featured=True).order_by('-created')
   post = Post.objects.filter(status='published').order_by('-created')
   context = {
      'post': post,
      'feature': feature,
      'category': category,
   }
   return render(request, 'post/home.html', context)


def post_detail_view(request, slug):
   post = get_object_or_404(Post, slug=slug)
   post_tags_ids = Tag.objects.all().values_list('id', flat=True)
   related_posts = Post.objects.filter(status='same_tags').filter(tags__in=post_tags_ids).exclude(slug=post.slug)
   related_posts = related_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-created')[:4]
   comments = post.comments.filter(active=True).order_by('-created')
   category = Category.objects.all()
   feature = Post.objects.filter(is_featured=True).order_by('-created')
   
   if request.method == "POST":
      form = CommentForm(request.POST)
      
      if form.is_valid():
         body = form.cleaned_data.get('body')
         
         new_comment = Comment(
            body = body,
            user = request.user,
         )
         new_comment.post = post
         new_comment.save()
         return redirect('post-detail', slug=post.slug)
   else:
      form = CommentForm()
      
   context = {
      'post': post,
      'related_posts':related_posts,
      'feature': feature,
      'category': category,
      'form': form,
      'comments': comments,
   }
   return render(request, 'post/detail_page.html', context)

   
def category_list(request, pk, slug):
   #category = Category.objects.all()
   category = Category.objects.all().annotate(post_count=Count('category'))
   feature = Post.objects.filter(is_featured=True).order_by('-created')
   post_category = Post.objects.filter(category__id=pk)
   
   context = {
      'post_category': post_category,
      'feature': feature,
      'category': category,
   }
   return render(request, 'post/category_list.html', context)


#@login_required
def comment_approve(request, pk):
   comment = get_object_or_404(Comment, pk=pk)
   comment.approve()
   return redirect('post_detail', pk=comment.post.pk)

#@login_required
def comment_remove(request, pk):
   comment = get_object_or_404(Comment, pk=pk)
   comment.delete()
   return redirect('post_detail', pk=comment.post.pk)

def about(request):
   return render(request, 'post/about.html')

def contact(request):
   return render(request, 'post/about.html', {'title': 'Contact'})
