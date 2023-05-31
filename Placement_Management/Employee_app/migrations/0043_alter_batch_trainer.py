# Generated by Django 4.2.1 on 2023-05-26 05:53

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee_app', '0042_alter_batch_trainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='trainer',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='course', chained_model_field='Faculty', limit_choices_to={'groups__name': 'Faculty', 'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_group', to=settings.AUTH_USER_MODEL, verbose_name='Trainer'),
        ),
    ]
