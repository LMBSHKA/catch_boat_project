# Generated by Django 4.2.11 on 2024-06-06 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_upload_images_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_images',
            name='user_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
