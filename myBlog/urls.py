from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as user_views


urlpatterns = [
    # Ckeditor Urls link
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # Admin Urls link
    path('admin/', admin.site.urls),
    # Users Urls
    path('register/', user_views.register, name='register'),
    path("login/", user_views.loginPage, name="login"),
    path("logout/", user_views.logoutUser, name="logout"),
    path('profile/', user_views.profile, name='profile'),
    path('profile-update/', user_views.profile_update, name='profile-update'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    # Post Urls link
    path('', include('post.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    