# Generated by Django 5.1.2 on 2024-11-10 22:03

import ptn_project.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptn_project', '0003_remove_project_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussionimage',
            name='image',
            field=models.ImageField(default='KakaoTalk_Photo_2024-10-31-14-56-43.png', null=True, upload_to=ptn_project.models.discussion_image_upload_path),
        ),
        migrations.AlterField(
            model_name='feedbackimage',
            name='image',
            field=models.ImageField(default='KakaoTalk_Photo_2024-10-31-14-56-43.png', null=True, upload_to=ptn_project.models.feedback_image_upload_path),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_thumbnail',
            field=models.ImageField(default='KakaoTalk_Photo_2024-10-31-14-56-43.png', null=True, upload_to=ptn_project.models.thumbnail_upload_path),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(default='KakaoTalk_Photo_2024-10-31-14-56-43.png', null=True, upload_to=ptn_project.models.detail_image_upload_path),
        ),
    ]
