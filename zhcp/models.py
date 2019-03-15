from django.db import models

# Create your models here.


class Classes(models.Model):
    class_id = models.CharField(max_length=10)

    def __str__(self):
        return self.class_id

    class Meta:
        db_table = "Classes"
        ordering = ['id']  # 以id为标准升序


"""
模型名称：Users（用户）
属性：
    1. student_id 学号
    2. name 姓名
    3. password 密码
    4. identity 身份
    5. score_sum 总分
关联属性：
    1. activity 活动，多对多
    2. classes 班级，一对多
"""


class Users(models.Model):
    student_id = models.CharField(max_length=12)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    identity = models.CharField(max_length=20, default="student",)
    score_sum = models.IntegerField(default=0, editable=False)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE, )

    @classmethod
    def add_user(cls, student_id, password, name, class_id):
        """

        :param student_id: 用户id
        :param password: 用户密码
        :param name: 用户姓名
        :param class_id: 班级对象
        :return: user对象
        """
        user = cls(student_id=student_id, password=password, name=name, class_id=class_id)
        return user

    def __str__(self):
        return self.student_id

    class Meta:
        db_table = "Users"
        ordering = ['id']  # 以id为标准升序


"""
模型名称：Application（加分申请）
属性：
    1. student_id 学号，关联属性到Users，一个Users关联多个Application
    2. name 名称
    3. score 加分
    4. detail 详细情况
    5. status 审批状态
    6. captain_id 审批人
    7. create_time 提交时间
"""


class Application(models.Model):
    student_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="application")
    name = models.CharField(max_length=20)
    score = models.IntegerField()
    detail = models.TextField(max_length=300, blank=True, null=True)
    status = models.BooleanField(default=False)
    # status = models.NullBooleanField(default=None)
    captain_id = models.CharField(max_length=12, blank=True, null=True)
    # captain_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    change_time = models.DateTimeField(auto_now=True)

    @classmethod
    def add_application(cls, student_id, name, detail, score):
        application = cls(student_id=student_id, name=name, detail=detail, score=score)
        return application

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Application"
        ordering = ['id']  # 以id为标准升序


"""
模型名称：Activity（活动）
属性：
    1. student_id 学号，关联属性到Users，多对多
    2. name 名称
    3. score 加分
    4. detail 详细情况
    5. create_time 提交时间
"""


class Activity(models.Model):
    student_id = models.ManyToManyField(Users, blank=True, related_name='Activity_student_id')
    name = models.CharField(max_length=20)
    score = models.IntegerField()
    detail = models.TextField(max_length=300, blank=True, null=True)
    create_by = models.ManyToManyField(Users, related_name='Activity_create_by')
    create_time = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Activity"
        ordering = ['id']  # 以id为标准升序




