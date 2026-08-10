from django.test import TestCase
from app.models import Item, Room


class ItemModelTest(TestCase):

    def test_item_is_active_by_default(self):
        item = Item.objects.create(
            bakanlik_adi="BASBAKANLIK",
            daire_adi="YONETIM",
            malzeme_adi="PRINTER",
            ayniyat_no="123456",
            fatura_no="654321",
            demirbas_no="12345678901234567",
            kiymet="1000.00",
            aciklama="Test printer",
        )

        self.assertEqual(item.status, "ACTIVE")

    def test_item_string_representation(self):
        item = Item.objects.create(
            bakanlik_adi="BASBAKANLIK",
            malzeme_adi="PRINTER",
            demirbas_no="12345678901234567",
            kiymet="1000.00",
            aciklama="Test printer",
        )

        self.assertEqual(
            str(item),
            "Test printer (12345678901234567) 1000.00 TL"
        )


class RoomModelTest(TestCase):

    def test_room_name(self):
        room = Room.objects.create(
            room_name="A101",
            description="Test room"
        )

        self.assertEqual(str(room), "A101")