# Generated by Django 3.1.4 on 2021-01-08 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lessons.profile'),
            preserve_default=False,
        ),
    ]