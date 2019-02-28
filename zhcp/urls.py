from django.urls import path
from . import views, VerificationCode

app_name = "zhcp"

urlpatterns = [
    path('test/', views.refresh_score_sum, name='test'),

    path('login/', views.login, name='login'),
    path('login/check/', views.login_check, name='loginCheck'),

    path('register/', views.register, name='register'),
    path('register/check/', views.register_check, name='registerCheck'),
    path('register/verificationCode/', VerificationCode.verification_code, name='verificationCode'),
    path('register/verificationCode/check/', views.verification_code_check, name='verificationCodeCheck'),

    path('index/', views.index, name='index'),

]