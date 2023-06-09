# Generated by Django 4.0 on 2023-04-26 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='projects')),
                ('link', models.URLField(max_length=128)),
            ],
        ),
    ]
