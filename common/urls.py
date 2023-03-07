from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('domain/', views.domain, name='domain'),
    path('url/', views.url, name='url'),
    path('url/create/', views.url_create, name='url_create'),
    path('url/delete/<int:pk>', views.url_delete, name='url_delete')    
]
