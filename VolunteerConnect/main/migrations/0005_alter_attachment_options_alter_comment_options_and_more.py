# Generated by Django 5.1.2 on 2024-12-12 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_event_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'default_permissions': ()},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'default_permissions': ()},
        ),
        migrations.AlterModelOptions(
            name='participation',
            options={'default_permissions': ()},
        ),
    ]