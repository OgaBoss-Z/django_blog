from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views.generic import (
   View,
   ListView,
   DetailView,
   CreateView,
   UpdateView,
   DeleteView
)
from .forms import CommentForm
from post.models import Post, Category, Comment

# Create your views here.
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


def post_detail(request, slug):
   category = Category.objects.all()
   feature = Post.objects.filter(is_featured=True).order_by('-created')
   post = Post.objects.get(slug=slug)
   #post = get_object_or_404(Post, slug=post.slug)
   form = CommentForm()
   
   if form.is_valid():
      print(form.cleaned_data)
   
   context = {
      'post': post,
      'feature': feature,
      'category': category,
      'form': form
   }
   return render(request, 'post/detail_page.html', context)





def post_detail_view(request, slug):
   post = get_object_or_404(Post, slug=slug)
   comments = post.comments.filter(active=True)
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
         
         ''' 
         new_comment = form.save(commit=False)
         new_comment.post = post
         new_comment.save() 
         return redirect('post-detail', slug=post.slug) '''
   else:
      form = CommentForm()
      
   context = {
      'post': post,
      'feature': feature,
      'category': category,
      'form': form,
      'comments': comments,
   }
   return render(request, 'post/detail_page.html', context)



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
