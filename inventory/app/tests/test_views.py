from django.test import TestCase
from django.urls import reverse

from app.models import Item, Room
from django.contrib.auth.models import User

class ItemListViewTest(TestCase):

    def test_all_items_page(self):

        response = self.client.get(
            reverse("all_items")
        )

        self.assertEqual(response.status_code, 200)


class AddItemViewTest(TestCase):

    def test_add_item(self):

        response = self.client.post(
            reverse("add_item"),
            {
                "bakanlik_adi": "BASBAKANLIK",
                "daire_adi": "YONETIM",
                "malzeme_adi": "PRINTER",
                "kiymet": "1000.00",
                "ayniyat_no": "123456",
                "fatura_no": "654321",
                "demirbas_no": "12345678901234567",
                "aciklama": "Test printer",
                "allocated_room": "",
            }
        )

        self.assertEqual(response.status_code, 302)

        item = Item.objects.get(
            demirbas_no="12345678901234567")

        self.assertEqual(item.status, "ACTIVE")

        '''
        self.assertTrue(
            Item.objects.filter(
                demirbas_no="12345678901234567"
            ).exists()
        )
        '''

class UpdateItemViewTest(TestCase):

    def setUp(self):

        self.item = Item.objects.create(
            bakanlik_adi="BASBAKANLIK",
            daire_adi="YONETIM",
            malzeme_adi="PRINTER",
            ayniyat_no="123456",
            fatura_no="654321",
            demirbas_no="12345678901234567",
            kiymet="1000.00",
            aciklama="Old description",
        )

    def test_update_item(self):

        response = self.client.post(
            reverse(
                "update_item",
                args=[self.item.id]
            ),
            {
                "bakanlik_adi": "BASBAKANLIK",
                "daire_adi": "NEW DAIRE",
                "malzeme_adi": "SERVER",
                "kiymet": "2000.00",
                "ayniyat_no": "123456",
                "fatura_no": "654321",
                "demirbas_no": "12345678901234567",
                "aciklama": "New description",
                "allocated_room": "",
            }
        )

        self.assertEqual(response.status_code, 302)

        self.item.refresh_from_db()

        self.assertEqual(
            self.item.aciklama,
            "New description"
        )

        self.assertEqual(
            self.item.kiymet,
            2000
        )

class WarehouseTest(TestCase):

    def setUp(self):

        self.warehouse = Room.objects.create(
            room_name="Warehouse"
        )

        self.item = Item.objects.create(
            bakanlik_adi="BASBAKANLIK",
            malzeme_adi="PRINTER",
            ayniyat_no="123456",
            fatura_no="654321",
            demirbas_no="12345678901234567",
            aciklama="Old printer",
        )

    def test_move_to_warehouse(self):

        response = self.client.post(
            reverse(
                "move_to_warehouse",
                args=[self.item.id]
            )
        )

        self.assertEqual(response.status_code, 302)

        self.item.refresh_from_db()

        self.assertEqual(
            self.item.status,
            "PASSIVE"
        )

        self.assertEqual(
            self.item.allocated_room,
            self.warehouse
        )

class DeleteItemTest(TestCase):

    def test_delete_item(self):

        item = Item.objects.create(
            bakanlik_adi="BASBAKANLIK",
            malzeme_adi="PRINTER",
            ayniyat_no="123456",
            fatura_no="654321",
            demirbas_no="12345678901234567",
            aciklama="Test printer",
        )

        item_id = item.id

        response = self.client.post(
            reverse(
                "delete_item",
                args=[item_id]
            )
        )

        self.assertEqual(response.status_code, 302)

        self.assertFalse(
            Item.objects.filter(id=item_id).exists()
        )

class AuthenticationTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

    def test_anonymous_user_cannot_access_items(self):

        response = self.client.get(
            reverse("all_items")
        )

        self.assertEqual(response.status_code, 302)


    def test_authenticated_user_can_access_items(self):

        self.client.login(
            username="testuser",
            password="testpassword"
        )

        response = self.client.get(
            reverse("all_items")
        )

        self.assertEqual(response.status_code, 200)