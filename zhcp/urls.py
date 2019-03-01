from django.urls import path
from . import views, VerificationCode

app_name = "zhcp"

urlpatterns = [
    path('test/', views.test, name='test'),

    path('login/', views.login, name='login'),
    path('login/check/', views.login_check, name='loginCheck'),

    path('register/', views.register, name='register'),
    path('register/check/', views.register_check, name='registerCheck'),
    path('register/verificationCode/', VerificationCode.verification_code, name='verificationCode'),
    path('register/verificationCode/check/', views.verification_code_check, name='verificationCodeCheck'),

    path('index/', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),

    path('myScore/', views.my_score, name='myScore'),

]