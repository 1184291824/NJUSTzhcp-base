from django.shortcuts import render, HttpResponse, redirect
from .models import Users, Activity, Application
from django.contrib.auth import logout

# Create your views here.


# 测试
def test(request):
    user = Users.objects.get(pk=1)
    return HttpResponse(user.pk)


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
        # request.session['login_status'] = 0  # 为了测试将登录状态置0
        student_id = request.session.get('student_id', 'None')
        user = Users.objects.get(student_id__exact=student_id)
        name = user.name
        identity = user.identity
        score_sum = user.score_sum
        return render(request, 'index.html', {
            'name': name,
            'student_id': student_id,
            'identity': identity,
            'score_sum': score_sum,
        })
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
            request.session['student_id'] = student.student_id
            request.session['password'] = password
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


def verification_code_check_application(request):
    """
    检查输入的验证码是否正确
    :param request:
    :return:
    """
    code = request.POST.get('code', '1')
    right_code = request.session['verification_code']

    if code.upper() == right_code.upper():  # 大小写不计，所以都改成大写
        return HttpResponse('true')
    else:
        return HttpResponse('false')


def logout_view(request):
    logout(request)
    return redirect('zhcp:index')


def my_score(request):
    """
    返回“我的加分”页面
    :param request:
    :return: {  'user': user,
                'application_list': application_list,
                'activity_list': activity_list,
            }
    """
    login_status = request.session.get('login_status', 0)

    if login_status == 1:
        student_id = request.session.get('student_id', 'None')
        user = Users.objects.get(student_id__exact=student_id)
        application_list = Application.objects.filter(student_id__exact=user, status__exact=True)
        activity_list = Activity.objects.filter(
            student_id__exact=user,
        )
        return render(request, 'myScore.html', {
            'user': user,
            'application_list': application_list,
            'activity_list': activity_list,
        })
    else:
        return redirect('zhcp:login')


def submit_application(request):
    """
    返回“提交申请界面”
    :param request:
    :return:
    """
    login_status = request.session.get('login_status', 0)

    if login_status == 1:
        student_id = request.session.get('student_id', 'None')
        user = Users.objects.get(student_id__exact=student_id)
        return render(request, 'submitApplication.html', {
            'user': user,
        })
    else:
        return redirect('zhcp:login')


def submit_application_add(request):
    """
    提交表单成功，增加一个Application的对象
    :param request:
    :return:
    """
    if request.method == 'POST':
        stu_id = request.session['student_id']
        student_id = Users.objects.get(student_id__exact=stu_id)
        name = request.POST.get('application-name')
        score = request.POST.get('score')
        detail = request.POST.get('detail')
        new_application = Application.add_application(
            student_id=student_id,
            name=name,
            score=score,
            detail=detail,
        )
        new_application.save()
        return redirect('zhcp:submitApplicationSuccess')
    else:
        return redirect('zhcp:index')


def submit_application_success(request):
    """
    当提交表单成功后，会重定向到这个函数，返回成功的HTML
    :param request:
    :return:
    """
    login_status = request.session.get('login_status', 0)

    if login_status == 1:
        return render(request, 'submitApplicationSuccess.html')
    else:
        return redirect('zhcp:login')


def my_application(request):
    """
    返回“我的申请”界面，分为
        :without_apply: 未审核
        :success: 审核通过
        :fail: 审核未通过

    :param request:
    :return:
    """
    login_status = request.session.get('login_status', 0)
    if login_status == 1:
        student_id = request.session['student_id']
        user = Users.objects.get(student_id__exact=student_id)
        without_apply = Application.objects.filter(student_id__student_id__exact=student_id, captain_id__isnull=True)
        success = Application.objects.filter(student_id__student_id__exact=student_id, status__exact=True)
        fail = Application.objects.filter(
            student_id__student_id__exact=student_id,
            status__exact=False,
            captain_id__isnull=False,
        )
        return render(request, 'myApplication.html', {
            'user': user,
            'without_apply': without_apply,
            'success': success,
            'fail': fail,
        })
    else:
        return redirect('zhcp:login')


def my_activity(request):
    """
    返回我的活动界面
    :param request:
    :return:
    """
    login_status = request.session.get('login_status', 0)

    if login_status == 1:
        student_id = request.session.get('student_id', 'None')
        user = Users.objects.get(student_id__exact=student_id)
        activity_list = Activity.objects.filter(
            student_id__exact=user,
        )
        return render(request, 'myActivity.html', {
            'user': user,
            'activity_list': activity_list,
        })
    else:
        return redirect('zhcp:login')


def review_application(request):
    """
    返回申请审核界面
    :param request:
    :return:
    """
    login_status = request.session.get('login_status', 0)

    if login_status == 1:
        student_id = request.session.get('student_id', 'None')
        user = Users.objects.get(student_id__exact=student_id)
        if user.identity == 'student':
            return redirect('zhcp:index')
        application_list_without_apply = Application.objects.filter(
            captain_id__isnull=True
        )
        application_list_applied = Application.objects.filter(
            captain_id__exact=student_id
        )
        return render(request, 'reviewApplication.html', {
            'user': user,
            'application_list_without_apply': application_list_without_apply,
            'application_list_applied': application_list_applied,
        })
    else:
        return redirect('zhcp:login')
