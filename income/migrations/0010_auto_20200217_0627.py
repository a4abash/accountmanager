# Generated by Django 2.1 on 2020-02-17 06:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('income', '0009_auto_20200217_0603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incomecategory',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AlterUniqueTogether(
            name='incomecategory',
            unique_together={('title', 'user_id')},
        ),
    ]
