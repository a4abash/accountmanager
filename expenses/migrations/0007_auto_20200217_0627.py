# Generated by Django 2.1 on 2020-02-17 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0006_auto_20200215_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expensescategory',
            old_name='user',
            new_name='user_id',
        ),
    ]
