# Generated by Django 4.1.7 on 2023-04-05 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ddlkdl', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
