# Generated by Django 4.2.1 on 2023-05-21 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_app', '0012_remove_cource_trainers'),
        ('Student', '0008_alter_student_course'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cource',
        ),
    ]
