from django.urls import path
from . import views

app_name = "zhcp"

urlpatterns = [
    path('test/', views.refresh_score_sum, name='test'),
    path('login/', views.login, name='login'),
    path('login/check/', views.login_check, name='loginCheck'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),

]