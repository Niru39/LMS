# Generated by Django 5.0.1 on 2024-01-28 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Student', 'Student'), ('Librarian', 'Librarian'), ('Teacher', 'Teacher'), ('Owner', 'Owner')], max_length=10),
        ),
    ]
