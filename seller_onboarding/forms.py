from django import forms
from .models import SellerOnboarding


class SellerOnboardingForm(forms.ModelForm):
    crypto_network = forms.ChoiceField(
        choices=[('', '---------'), ('Polygon', 'Polygon'),
                 ('Ethereum', 'Ethereum')],
        widget=forms.Select(),
        required=False,
    )

    class Meta:
        model = SellerOnboarding
        fields = [
            'store_name',
            'gift_card_amount',
            'price',
            'crypto_network',
            'wallet_address',
            'email_address',
        ]
        widgets = {
            'store_name': forms.TextInput(attrs={'required': False}),
            'gift_card_amount': forms.NumberInput(attrs={'step': 'any', 'required': False}),
            'price': forms.NumberInput(attrs={'step': 'any', 'required': False}),
            'wallet_address': forms.TextInput(attrs={'required': False}),
            'email_address': forms.EmailInput(attrs={'required': False}),
        }

# NOTE: Some redundancy exists in the widget attributes below, as they are set to
# 'required': False. These attributes are not necessary, as the form fields will
# inherit the required status from the corresponding model fields.
# However, this code was put together quickly for demonstration purposes.
