# Generated by Django 4.0.5 on 2022-06-24 20:23

from django.db import migrations, models
import blog.utils


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail1',
            field=models.ImageField(default='', upload_to=blog.utils.upload_picture),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail2',
            field=models.ImageField(default='', upload_to=blog.utils.upload_picture),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail3',
            field=models.ImageField(default='', upload_to=blog.utils.upload_picture),
        ),
    ]
