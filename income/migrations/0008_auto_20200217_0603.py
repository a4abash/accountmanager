# Generated by Django 2.1 on 2020-02-17 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0007_auto_20200215_1724'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='incomecategory',
            unique_together={('title', 'slug')},
        ),
    ]
