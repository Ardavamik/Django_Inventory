from django.test import TestCase
from app.forms import ItemForm


class ItemFormTest(TestCase):

    def test_valid_item_form(self):

        form = ItemForm(data={
            "bakanlik_adi": "BASBAKANLIK",
            "daire_adi": "YONETIM",
            "malzeme_adi": "PRINTER",
            "kiymet": "1000.00",
            "ayniyat_no": "123456",
            "fatura_no": "654321",
            "demirbas_no": "12345678901234567",
            "aciklama": "Test printer",
            "allocated_room": "",
        })

        self.assertTrue(form.is_valid())

    def test_invalid_ayniyat_no(self):

        form = ItemForm(data={
            "bakanlik_adi": "BASBAKANLIK",
            "malzeme_adi": "PRINTER",
            "ayniyat_no": "12345",
            "fatura_no": "654321",
            "demirbas_no": "12345678901234567",
            "aciklama": "Test",
        })

        self.assertFalse(form.is_valid())

    
    def test_invalid_demirbas_no(self):

        form = ItemForm(data={
            "bakanlik_adi": "BASBAKANLIK",
            "malzeme_adi": "PRINTER",
            "ayniyat_no": "123456",
            "fatura_no": "654321",
            "demirbas_no": "12345",
            "aciklama": "Test",
        })

        self.assertFalse(form.is_valid())