# Generated by Django 5.1.1 on 2024-10-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('regular', 'Regular'), ('admin', 'Admin'), ('manager', 'Manager'), ('supervisor', 'Supervisor'), ('employee', 'Employee')], default='regular', max_length=40),
        ),
    ]
