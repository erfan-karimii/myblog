# Generated by Django 4.0.4 on 2022-07-01 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_show'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='last_update',
            new_name='create_date',
        ),
    ]
