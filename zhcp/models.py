from django.db import models

# Create your models here.


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
"""


class Users(models.Model):
    student_id = models.CharField(max_length=12)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    identity = models.CharField(max_length=20, default="student",)
    score_sum = models.IntegerField(default=0, editable=False)

    @classmethod
    def add_user(cls, student_id, password, name, ):
        user = cls(student_id=student_id, password=password, name=name)
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
    detail = models.TextField(max_length=300, blank=True)
    status = models.BooleanField(default=False)
    captain_id = models.CharField(max_length=12, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

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
    student_id = models.ManyToManyField(Users, blank=True)
    name = models.CharField(max_length=20)
    score = models.IntegerField()
    detail = models.TextField(max_length=300, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Activity"
        ordering = ['id']  # 以id为标准升序

