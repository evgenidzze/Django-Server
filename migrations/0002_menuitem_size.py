# Generated by Django 4.2.4 on 2023-09-09 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
