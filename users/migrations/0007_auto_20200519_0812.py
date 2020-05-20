# Generated by Django 3.0.6 on 2020-05-19 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200519_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='users.Activity'),
        ),
    ]