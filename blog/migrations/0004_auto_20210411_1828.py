# Generated by Django 3.1.4 on 2021-04-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210411_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='images',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=True, upload_to='', verbose_name='Rasm'),
            preserve_default=False,
        ),
    ]
