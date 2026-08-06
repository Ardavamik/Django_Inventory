from django import forms
from .models import Item, Room

class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['aciklama', 'demirbas_no', 'allocated_room','bakanlik_adi',
            'daire_adi',
            'malzeme_adi',
             'kiymet',
            'ayniyat_no',
            'fatura_no',]

class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['aciklama', 'allocated_room','bakanlik_adi',
            'daire_adi',
            'malzeme_adi',
             'kiymet',
            'ayniyat_no',
            'fatura_no',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["bakanlik_adi"].disabled = True
        self.fields["daire_adi"].disabled = True
        self.fields["kiymet"].disabled = True
        self.fields["ayniyat_no"].disabled = True
        self.fields["fatura_no"].disabled = True


class RoomCreateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'description']


class RoomUpdateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'description']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    
            self.fields["room_name"].disabled = True
            