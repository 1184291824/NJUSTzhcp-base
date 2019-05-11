# Generated by Django 2.1.3 on 2019-04-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhcp', '0012_auto_20190315_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(auto_now_add=True)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'DayNumber',
            },
        ),
        migrations.CreateModel(
            name='UserIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('equipment_model', models.CharField(default='未知机型', max_length=30)),
            ],
            options={
                'db_table': 'UserIP',
            },
        ),
        migrations.CreateModel(
            name='VisitNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'VisitNumber',
            },
        ),
    ]