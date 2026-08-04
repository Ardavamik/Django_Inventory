from django import forms
from .models import Item, Room

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['aciklama', 'demirbas_no', 'allocated_room','bakanlik_adi',
            'daire_adi',
            'malzeme_adi',
             'kiymet',
            'ayniyat_no',
            'fatura_no',]

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'description']