# Generated by Django 5.1.2 on 2024-11-01 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='actor_image',
            field=models.ImageField(blank=True, null=True, upload_to='actor_images/'),
        ),
        migrations.AlterField(
            model_name='director',
            name='director_image',
            field=models.ImageField(blank=True, null=True, upload_to='director_images/'),
        ),
        migrations.AlterField(
            model_name='moments',
            name='movie_moments',
            field=models.ImageField(blank=True, null=True, upload_to='movie_moment/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_image',
            field=models.ImageField(blank=True, null=True, upload_to='movie_image/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_trailer',
            field=models.FileField(blank=True, null=True, upload_to='movie_trailer/'),
        ),
        migrations.AlterField(
            model_name='movielanguages',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='vid/'),
        ),
    ]
