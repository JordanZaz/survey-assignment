from django.db import models


class SellerOnboarding(models.Model):
    survey_id = models.CharField(max_length=255, unique=True)
    store_name = models.CharField(max_length=255, blank=True, null=True)
    gift_card_number = models.CharField(max_length=255, blank=True, null=True)
    gift_card_pin = models.CharField(max_length=255, blank=True, null=True)
    gift_card_amount_currency = models.CharField(max_length=255)
    gift_card_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    price_currency = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    accepts_crypto = models.BooleanField(default=False)
    crypto_network = models.CharField(max_length=255, blank=True, null=True)
    wallet_address = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    deposit_or_validate = models.CharField(
        max_length=255, blank=True, null=True)
    deposit_step = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.store_name or "None"
