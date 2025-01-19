from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.shortcuts import redirect

handler404 = lambda request, exception: redirect('home')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('restaurants/', include('restaurants.urls')),
    path('wines/', include('wines.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', user_views.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 