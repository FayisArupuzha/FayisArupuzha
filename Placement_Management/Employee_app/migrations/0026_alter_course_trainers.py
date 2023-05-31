# Generated by Django 4.2.1 on 2023-05-21 14:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee_app', '0025_alter_course_trainers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='trainers',
            field=models.ManyToManyField(blank=True, limit_choices_to={'groups__name': 'Faculty', 'is_active': True}, related_name='trainer_courses', to=settings.AUTH_USER_MODEL),
        ),
    ]
