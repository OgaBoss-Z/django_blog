from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import  authenticate, login, logout
from post.models import Comment, Post



def register(request):
   if request.user.is_authenticated:
      return redirect('home-page')
   else:
      form = SignUpForm()
      if request.method == 'POST':
         form = SignUpForm(request.POST)
         if form.is_valid():
            form.save()
            # Get the username to display in the success message.
            user = form.cleaned_data.get('username')
            messages.success(request, 'Your Account has been successfully created, Please login to Your Account @'+ user)
            return redirect('login')
      return render(request, 'users/register.html', {'form': form})


def loginPage(request):
   if request.user.is_authenticated:
      return redirect('home-page')
   else:
      if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         
         user = authenticate(request, username=username, password=password)
         if user is not None:
            login(request, user)
            return redirect('home-page')
         else:
            messages.info(request, 'Username or Password is incorrect!')
      return render(request, 'users/login.html')


@login_required(login_url='login')
def logoutUser(request):
   if request.user.is_authenticated:
      logout(request)
      messages.info(request, 'You have been successfully logged Out')
      return redirect('home-page')
   else:
      return redirect('home-page')


@login_required(login_url='login')
def profile(request):
   current_user = request.user
   user_comments = Comment.objects.filter(user_id=current_user.id).order_by('-created')
   #post = get_object_or_404(Post, slug=slug)
   
   context = {
      'user_comments':user_comments,
   }
   
   return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def profile_update(request):
   if request.method == 'POST':
      u_form = UserUpdateForm(request.POST, instance=request.user)
      p_form = ProfileUpdateForm(request.POST,
                                 request.FILES,
                                 instance=request.user.profile)
      if u_form.is_valid() and p_form.is_valid():
         u_form.save()
         p_form.save()
         messages.success(request, f'Your profile has been updated successfully. ')
         return redirect('profile')

   else:
      u_form = UserUpdateForm(instance=request.user)
      p_form = ProfileUpdateForm(instance=request.user.profile)

   context = {
      'u_form': u_form,
      'p_form': p_form
   }

   return render(request, 'users/profile_update.html', context)