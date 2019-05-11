from django.urls import path
from . import views, VerificationCode

app_name = "zhcp"

urlpatterns = [
    # path('test/', views.test, name='test'),
    path('refresh/', views.refresh_score_sum, name='refresh'),

    path('login/', views.login, name='login'),
    path('login/check/', views.login_check, name='loginCheck'),

    path('register/', views.register, name='register'),
    path('register/check/', views.register_check, name='registerCheck'),
    path('register/mCheck/', views.mobile_register_check, name='mobileRegisterCheck'),
    path('verificationCode/', VerificationCode.verification_code, name='verificationCode'),
    path('register/verificationCode/check/', views.verification_code_check, name='verificationCodeCheck'),

    path('index/', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),

    path('myScore/', views.my_score, name='myScore'),
    path('submitApplication/', views.submit_application, name='submitApplication'),
    path('verificationCode/check/', views.verification_code_check_application, ),
    path('submitApplication/add/', views.submit_application_add, name='submitApplicationAdd'),
    path('submitApplication/success/', views.submit_application_success, name='submitApplicationSuccess'),
    path('myApplication/', views.my_application, name='myApplication'),
    path('myActivity/', views.my_activity, name='myActivity'),
    path('reviewApplication/', views.review_application, name='reviewApplication'),
    path('reviewApplication/detail/', views.review_application_detail, name='reviewApplicationDetail'),
    path('reviewApplication/submit/', views.review_application_submit, name='reviewApplicationSubmit'),
    path('submitActivity/', views.submit_activity, name='submitActivity'),
    path('submitActivity/add', views.submit_activity_add, name='submitActivityAdd'),
    path('submitActivity/success/', views.submit_activity_success, name='submitActivitySuccess'),
    path('developer/', views.developer, name="developer"),
    path('piano/', views.piano, name="piano"),
    path('visitNumber/', views.visit_number, name="visitNumber"),

    path('refresh_visit_number/', views.refresh_visit_number, name="refreshVisitNumber"),

    path('mqj/', views.mqj, name="mqj"),

]
