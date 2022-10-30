from django import forms
from .models import Weapon

class WeaponForm(forms.ModelForm):
    name = forms.CharField(label='무기 이름')
    power = forms.IntegerField(label='무기 공격력')

    class Meta:
        model = Weapon
        fields = '__all__'