# Generated by Django 2.1.3 on 2019-02-27 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zhcp', '0005_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='score_sum',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application', to='zhcp.Users'),
        ),
    ]
