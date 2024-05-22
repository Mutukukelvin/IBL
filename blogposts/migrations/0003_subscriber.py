# Generated by Django 5.0.6 on 2024-05-20 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0002_posts_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogposts.posts')),
            ],
        ),
    ]
