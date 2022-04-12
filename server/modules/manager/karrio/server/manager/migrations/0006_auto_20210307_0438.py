# Generated by Django 3.1.7 on 2021-03-07 04:38

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20210216_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='validate_location',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='validation',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]