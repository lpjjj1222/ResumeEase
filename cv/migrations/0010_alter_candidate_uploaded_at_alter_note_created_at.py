# Generated by Django 5.0.7 on 2024-07-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0009_candidate_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
