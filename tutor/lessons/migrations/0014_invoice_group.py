# Generated by Django 3.1.5 on 2021-01-12 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0013_profile_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lessons.group'),
            preserve_default=False,
        ),
    ]