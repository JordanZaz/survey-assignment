# Generated by Django 4.2 on 2023-05-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_onboarding', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selleronboarding',
            name='email_address',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
