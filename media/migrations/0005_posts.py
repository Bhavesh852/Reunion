# Generated by Django 4.1.5 on 2023-03-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_following'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]