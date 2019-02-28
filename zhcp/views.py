from django.shortcuts import render, HttpResponse, redirect
from .models import Users, Activity, Application

# Create your views here.


# 测试
def test(request):
    return HttpResponse('success')


# 更新总分
def refresh_score_sum(request):
    """更新总分
    :param request: 网站请求
    :return: HttpResponse
    """
    student_id = request.GET.get("id")  # 使用GET方法取到用户的id,后期应改成POST
    user = Users.objects.filter(student_id__exact=student_id)[0]  # 取到id对应的users对象user
    application_list = Application.objects.filter(status=True, student_id__exact=user)  # 取到该对象申请的，且已经审核过的，申请列表
    activity_list = Activity.objects.filter(student_id__exact=user)  # 取到包含该对象的活动列表
    user.score_sum = 0  # 令该对象的总分归零，然后求和
    for application in application_list:
        user.score_sum += application.score
    for activity in activity_list:
        user.score_sum += activity.score

    user.save()  # 保存这个对象

    return HttpResponse(user.score_sum)  # 返回


def index(request):
    """
    主页
    :param request:
    :return:
    """
    login_status = request.session.get('login_status', 0)
    if login_status == 1:
        request.session['login_status'] = 0  # 为了测试将登录状态置0
        return render(request, 'index.html')
    else:
        return redirect('zhcp:login')


def login(request):
    """登录
    :param request: 网站请求
    :return:登录界面
    """
    login_status = request.session.get('login_status', 0)
    if login_status == 0:
        return render(request, 'login.html')
    else:
        return redirect('zhcp:index')


def register(request):
    """注册
    :param request: 网站请求
    :return:注册界面
    """
    return render(request, 'register.html')


def login_check(request):
    """
    登录检测用户名是否存在，以及用户名密码是否正确
    :param request:
    :return:
    """
    student_id_input = request.POST.get("student_id")
    password_input = request.POST.get("password")
    try:
        student = Users.objects.get(student_id__exact=student_id_input)
        password = student.password
        if password_input == password:
            request.session['login_status'] = 1
            return HttpResponse("true")
        else:
            return HttpResponse("passwordWrong")
    except Users.DoesNotExist:
        return HttpResponse("idDoesNotExist")


def register_check(request):
    """
    检查注册的用户id是否已经存在
    :param request:
    :return:
    """
    student_id_input = request.POST.get('student_id')
    try:
        Users.objects.get(student_id__exact=student_id_input)
        return HttpResponse('false')
    except Users.DoesNotExist:
        request.session['student_id'] = student_id_input
        request.session['password'] = request.POST.get('password')
        return HttpResponse("true")


def verification_code_check(request):
    """
    检查输入的验证码是否正确，如果正确就增加一个新用户
    :param request:
    :return:
    """
    code = request.POST.get('code', '1')
    right_code = request.session['verification_code']

    if code.upper() == right_code.upper():  # 大小写不计，所以都改成大写
        request.session['name'] = request.POST.get('name')
        student_id = request.session['student_id']
        password = request.session['password']
        name = request.session['name']
        new_user = Users.add_user(student_id, password, name)
        new_user.save()
        return HttpResponse('true')
    else:
        return HttpResponse('false')



