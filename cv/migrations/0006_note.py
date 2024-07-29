# Generated by Django 5.0.7 on 2024-07-27 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_tag_candidate_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('text', models.TextField(max_length=400)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='cv.candidate')),
            ],
        ),
    ]
