# Generated by Django 4.0.4 on 2022-07-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
