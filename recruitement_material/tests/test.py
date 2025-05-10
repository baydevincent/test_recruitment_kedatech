from odoo.tests import HttpCase
import json

class TestMaterialApi(HttpCase):

    def test_material_resapi_edit(self):
        # Persiapan data uji
        product = self.env['product.material'].create({
            'material_code': 'MTR001',
            'name': 'Material Test',
            'material_type': 'product',
            'buy_price': 100000,
        })

        # Data JSON untuk pembaruan
        data = {
            'material_code': 'MTR001',
            'material_name': 'Material Updated',
            'material_type': 'product',
            'buy_price': 120000,
        }

        # Mengirim permintaan PUT
        response = self.url_open(
            '/api/product_material_edit/%d' % product.id,
            method='PUT',
            json=data
        )

        # Memverifikasi respons
        self.assertEqual(response.status_code, 200)
        self.assertIn('Data Berhasil dihapus', response.json().get('message'))

        # Memverifikasi pembaruan data
        product.refresh()
        self.assertEqual(product.name, 'Material Updated')
        self.assertEqual(product.buy_price, 120000)

    def test_material_resapi_delete(self):
        # Persiapan data uji
        product = self.env['product.material'].create({
            'material_code': 'MTR002',
            'name': 'Material Test Delete',
            'material_type': 'product',
            'buy_price': 100000,
        })

        # Mengirim permintaan DELETE
        response = self.url_open(
            '/api/product_material_delete/%d' % product.id,
            method='DELETE'
        )

        # Memverifikasi respons
        self.assertEqual(response.status_code, 200)
        self.assertIn('Data Berhasil dihapus', response.json().get('message'))

        # Memverifikasi penghapusan data
        product = self.env['product.material'].browse(product.id)
        self.assertFalse(product.exists())
