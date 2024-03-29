# Generated by Django 4.2 on 2023-05-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellerOnboarding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_id', models.CharField(max_length=255, unique=True)),
                ('store_name', models.CharField(max_length=255)),
                ('gift_card_number', models.CharField(blank=True, max_length=255, null=True)),
                ('gift_card_pin', models.CharField(blank=True, max_length=255, null=True)),
                ('gift_card_amount_currency', models.CharField(max_length=255)),
                ('gift_card_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('price_currency', models.CharField(max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('accepts_crypto', models.BooleanField(default=False)),
                ('crypto_network', models.CharField(blank=True, max_length=255, null=True)),
                ('wallet_address', models.CharField(blank=True, max_length=255, null=True)),
                ('email_address', models.EmailField(max_length=254)),
                ('deposit_or_validate', models.CharField(blank=True, max_length=255, null=True)),
                ('deposit_step', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
