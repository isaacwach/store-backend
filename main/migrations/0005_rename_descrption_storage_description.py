# Generated by Django 4.0.3 on 2022-04-28 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_admin_email_alter_admin_username_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storage',
            old_name='descrption',
            new_name='description',
        ),
    ]
