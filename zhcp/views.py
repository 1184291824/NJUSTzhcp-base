from django.shortcuts import render, HttpResponse, redirect
from .models import Users, Activity, Application, Classes
from django.contrib.auth import logout

# Create your views here.


# 测试
def test(request):
    return render(request, 'mobile/login.html')


# 获取设备类型
def device(request):
    """
    获取设备类型
    :param request:
    :return:
        False:手机
        True:PC
    """
    agent = request.META['HTTP_USER_AGENT'].lower()
    mobile = ['iphone', 'android', 'symbianos', 'windows phone']

    if any([agent.find(name) + 1 for name in mobile]):
        return False
    else:
        return True


# 更新总分
def refresh_score_sum(user):
    """更新总分
    :param user: 用户对象
    :return: HttpResponse
    """
    # login_status = request.session.get('login_status', 0)

    # if login_status == 1:
    #     student_id = request.GET.get("id")  # 使用GET方法取到用户的id,后期应改成POST
    # user = Users.objects.filter(student_id__exact=student_id)[0]  # 取到id对应的users对象user
    application_list = Application.objects.filter(status=True, student_id__exact=user)  # 取到该对象申请的，且已经审核过的，申请列表
    activity_list = Activity.objects.filter(student_id__exact=user)  # 取到包含该对象的活动列表
    user.score_sum = 0  # 令该对象的总分归零，然后求和
    for application in application_list:
        user.score_sum += application.score
    for activity in activity_list:
        user.score_sum += activity.score

    user.save()  # 保存这个对象

    # return redirect('zhcp:myScore')  # 返回
    # else:
    #     return redirect('zhcp:login')


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
        refresh_score_sum(user=user)  # 更新总分
        name = user.name
        identity = user.identity
        score_sum = user.score_sum
        if device(request) is True:
            html_str = 'index.html'
        else:
            html_str = 'mobile/index.html'
        return render(request, html_str, {
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
        if device(request) is True:
            return render(request, 'login.html')
        else:
            return render(request, 'mobile/login.html')
    else:
        return redirect('zhcp:index')


def register(request):
    """注册
    :param request: 网站请求
    :return:注册界面
    """
    # return render(request, 'register.html', )
    login_status = request.session.get('login_status', 0)
    if login_status == 0:
        if device(request) is True:
            return render(request, 'register.html')
        else:
            return render(request, 'mobile/register.html')
    else:
        return redirect('zhcp:index')


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
        request.session['class_id'] = request.POST.get('class_id')
        student_id = request.session['student_id']
        password = request.session['password']
        name = request.session['name']
        class_id_str = request.session['class_id']
        try:
            class_id = Classes.objects.get(class_id__exact=class_id_str)
        except Classes.DoesNotExist:
            return HttpResponse('DoesNotExist')
        new_user = Users.add_user(student_id=student_id, password=password, name=name, class_id=class_id)
        new_user.save()
        return HttpResponse('true')
    else:
        return HttpResponse('false')


def mobile_register_check(request):
    """
    移动端检测注册是否成功，如果成功则添加用户
    :param request:
    :return:
    """
    student_id = request.POST.get('student_id')
    code = request.POST.get('code', '1')
    right_code = request.session['verification_code']

    if code.upper() == right_code.upper():  # 大小写不计，所以都改成大写
        try:
            Users.objects.get(student_id__exact=student_id)
            return HttpResponse('StudentExist')
        except Users.DoesNotExist:
            class_id_str = request.POST.get('class_id')
            try:
                class_id = Classes.objects.get(class_id__exact=class_id_str)
            except Classes.DoesNotExist:
                return HttpResponse('ClassesDoesNotExist')

            name = request.POST.get('name')
            password = request.POST.get('password')
            new_user = Users.add_user(student_id=student_id, password=password, name=name, class_id=class_id)
            new_user.save()

            return HttpResponse("true")
    else:
        return HttpResponse('false')


def verification_code_check_application(request):
    """
    检查输入的验证码是否正确，是除register页面之外的页面的验证码检测
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
        refresh_score_sum(user=user)  # 更新总分
        application_list = Application.objects.filter(student_id__exact=user, status__exact=True)
        activity_list = Activity.objects.filter(
            student_id__exact=user,
        )
        if device(request) is True:
            html_str = 'myScore.html'
        else:
            html_str = 'mobile/myScore.html'
        return render(request, html_str, {
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
        if device(request) is True:
            html_str = 'submitApplication.html'
        else:
            html_str = 'mobile/submitApplication.html'
        return render(request, html_str, {
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
    login_status = request.session.get('login_status', 0)

    if login_status == 1:
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
            if device(request) is True:
                url_str = 'zhcp:submitApplicationSuccess'
            else:
                url_str = 'zhcp:index'
            return redirect(url_str)
        else:
            return redirect('zhcp:index')
    else:
        return redirect('zhcp:login')


def submit_application_success(request):
    """
    当提交表单成功后，会重定向到这个函数，返回成功的HTML
    :param request:
    :return:
    """
    login_status = request.session.get('login_status', 0)

    if login_status == 1:
        student_id = request.session.get('student_id')
        user = Users.objects.get(student_id__exact=student_id)
        return render(request, 'submitApplicationSuccess.html', {
            'user': user,
        })
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
        if device(request) is True:
            html_str = 'myApplication2.html'
        else:
            html_str = 'mobile/myApplication.html'
        return render(request, html_str, {
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
        if device(request) is True:
            html_str = 'myActivity.html'
        else:
            html_str = 'mobile/myActivity.html'
        return render(request, html_str, {
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
        user_class = user.class_id
        if user.identity == 'student':
            return redirect('zhcp:index')
        application_list_without_apply = Application.objects.filter(
            captain_id__isnull=True,
            student_id__class_id=user_class,  # 只让班长看到自己班的学生
        )
        application_list_applied = Application.objects.filter(
            captain_id__exact=student_id,
            student_id__class_id=user_class,  # 只让班长看到自己班的学生
        ).order_by('-change_time')
        if device(request) is True:
            html_str = 'reviewApplication.html'
        else:
            html_str = 'mobile/reviewApplication.html'
        return render(request, html_str, {
            'user': user,
            'application_list_without_apply': application_list_without_apply,
            'application_list_applied': application_list_applied,
        })
    else:
        return redirect('zhcp:login')


def review_application_detail(request):
    """
    返回申请详情界面
    :param request:
    :return:
    """
    login_status = request.session.get('login_status', 0)

    if login_status == 1:
        student_id = request.session.get('student_id', 'None')
        application_pk = request.GET.get('pk')
        user = Users.objects.get(student_id__exact=student_id)
        if user.identity == 'student':
            return redirect('zhcp:index')
        try:
            application = Application.objects.get(
                pk=int(application_pk)
            )
        except Application.DoesNotExist:
            return redirect('zhcp:reviewApplication')
        return render(request, 'reviewApplicationDetail.html', {
            'user': user,
            'application': application,
        })
    else:
        return redirect('zhcp:login')


def review_application_submit(request):
    """
    审核结果的提交
    :param request:
    :return:
    """
    login_status = request.session.get('login_status', 0)

    if login_status == 1:
        if request.method == 'POST':
            pk = request.POST.get('pk')
            status = request.POST.get('status')
            application = Application.objects.get(pk=int(pk))
            if status == 'True':
                application.status = True
            else:
                application.status = False
            application.captain_id = request.session.get('student_id')
            application.save()
            return HttpResponse('success')
        else:
            return redirect('zhcp:index')
    else:
        return redirect('zhcp:login')


def submit_activity(request):
    """
    返回“提交活动界面”
    :param request:
    :return:
    """
    login_status = request.session.get('login_status', 0)

    if login_status == 1:
        student_id = request.session.get('student_id', 'None')
        user = Users.objects.get(student_id__exact=student_id)
        user_list = Users.objects.all()
        if user.identity != 'teacher':
            return redirect('zhcp:index')
        return render(request, 'submitActivity.html', {
            'user': user,
            'user_list': user_list,
        })
    else:
        return redirect('zhcp:login')


def submit_activity_add(request):
    """
    提交表单成功，增加一个Application的对象
    :param request:
    :return:
    """
    login_status = request.session.get('login_status', 0)

    if login_status == 1:
        if request.method == 'POST':
            stu_id = request.session['student_id']
            create_by = Users.objects.get(student_id__exact=stu_id)
            name = request.POST.get('application-name')
            score = request.POST.get('score')
            detail = request.POST.get('detail')
            value = request.POST.getlist('users')
            student_list = []
            for v in value:
                student_list.append(Users.objects.get(pk=v))
            active = Activity.objects.create(name=name, score=score, detail=detail)
            active.student_id.add(*student_list)
            active.create_by.add(create_by)

            return redirect('zhcp:submitActivitySuccess')
        else:
            return redirect('zhcp:index')
    else:
        return redirect('zhcp:login')


def submit_activity_success(request):
    """
    当提交表单成功后，会重定向到这个函数，返回成功的HTML
    :param request:
    :return:
    """
    login_status = request.session.get('login_status', 0)

    if login_status == 1:
        student_id = request.session.get('student_id')
        user = Users.objects.get(student_id__exact=student_id)
        return render(request, 'submitActivitySuccess.html', {
            'user': user,
        })
    else:
        return redirect('zhcp:login')


def developer(request):
    """
    返回开发者信息页面
    :param request:
    :return:
    """
    login_status = request.session.get('login_status', 0)

    if login_status == 1:
        return render(request, 'mobile/Developer.html', )
    else:
        return redirect('zhcp:login')


def piano(request):
    """
    返回钢琴游戏页面
    :param request:
    :return:
    """
    login_status = request.session.get('login_status', 0)

    if login_status == 1:
        return render(request, 'mobile/piano.html', )
    else:
        return redirect('zhcp:login')
