# Generated by Django 4.2 on 2023-05-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_job_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='mypersonal/static/images/'),
        ),
    ]
