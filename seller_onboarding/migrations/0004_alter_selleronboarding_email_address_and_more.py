# Generated by Django 4.2 on 2023-05-01 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_onboarding', '0003_alter_selleronboarding_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selleronboarding',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='selleronboarding',
            name='store_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
