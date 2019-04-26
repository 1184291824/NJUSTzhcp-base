from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):

    list_display = [
        'pk',
        'student_id',
        'name',
        'class_id',
        'identity',
        'score_sum',
    ]
    search_fields = ['name']  # 搜索字段


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = [
        'pk',
        'student_id',
        'name',
        'score',
        'status',
        'captain_id',
        'create_time',
    ]

    search_fields = ['name']  # 搜索字段


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):

    list_display = [
        'pk',
        'name',
        'score',
        'create_time',
    ]

    search_fields = ['name']  # 搜索字段


@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):

    list_display = [
        'pk',
        'class_id'
    ]

    search_fields = ['classes_id']  # 搜索字段


@admin.register(UserIP)
class UserIPAdmin(admin.ModelAdmin):

    list_display = [
        'pk',
        'student_id',
        'ip',
        'time',
        'equipment_model',
    ]

    search_fields = ['ip']  # 搜索字段


@admin.register(VisitNumber)
class VisitNumberAdmin(admin.ModelAdmin):

    list_display = [
        'pk',
        'count',
    ]

    search_fields = ['pk']  # 搜索字段


@admin.register(DayNumber)
class DayNumberAdmin(admin.ModelAdmin):

    list_display = [
        'pk',
        'day',
        'count',
    ]

    search_fields = ['day']  # 搜索字段
