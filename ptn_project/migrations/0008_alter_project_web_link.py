# Generated by Django 5.1.2 on 2024-11-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptn_project', '0007_remove_project_link_project_android_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='web_link',
            field=models.TextField(default='', null=True),
        ),
    ]
