# Generated by Django 4.2.11 on 2024-06-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_upload_images_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_images',
            name='category',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]