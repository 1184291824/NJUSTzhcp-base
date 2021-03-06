# Generated by Django 2.1.3 on 2019-03-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhcp', '0006_auto_20190227_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='detail',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='student_id',
            field=models.ManyToManyField(blank=True, null=True, to='zhcp.Users'),
        ),
        migrations.AlterField(
            model_name='application',
            name='captain_id',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='detail',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
