# Generated by Django 2.1.3 on 2019-03-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhcp', '0008_auto_20190303_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='create_by',
            field=models.ManyToManyField(related_name='Activity_create_by', to='zhcp.Users'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='student_id',
            field=models.ManyToManyField(blank=True, related_name='Activity_student_id', to='zhcp.Users'),
        ),
    ]
