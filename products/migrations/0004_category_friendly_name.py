# Generated by Django 3.2.25 on 2025-03-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20250312_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
