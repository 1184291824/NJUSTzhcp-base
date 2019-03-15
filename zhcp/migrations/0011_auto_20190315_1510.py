# Generated by Django 2.1.3 on 2019-03-15 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zhcp', '0010_application_change_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Classes',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='users',
            name='class_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zhcp.Classes'),
        ),
    ]