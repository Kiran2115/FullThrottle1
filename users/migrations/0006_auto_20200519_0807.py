# Generated by Django 3.0.6 on 2020-05-19 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200519_0542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='activity',
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]