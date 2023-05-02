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

    def __init__(self, *args, **kwargs):
        super(SellerOnboardingForm, self).__init__(*args, **kwargs)
        if 'submit' not in self.data:
            self.fields['email_address'].required = False
