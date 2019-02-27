from django.contrib import admin

# Register your models here.

from .models import Users, Application, Activity


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):

    list_display = [
        'pk',
        'student_id',
        'name',
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
