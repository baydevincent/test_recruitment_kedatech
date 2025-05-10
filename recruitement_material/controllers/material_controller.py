import json
import requests
from odoo import http, _, exceptions
from odoo.http import request
from odoo.tests import Form
import werkzeug.wrappers

class MaterialRestApi(http.Controller):
    @http.route(['/api/product_material_get_all/'], type='http', auth='public', methods=['GET'], csrf=False)
    def material_resapi_get_all(self, **params):
        material = request.env['product.material'].sudo().search([])
        data_supplier ={}
        data_material =[]
        for h in material:
            for partner in h.supplier:
                data_supplier = {'supplier_id': partner.id, 
                                 'supplier_name': partner.name}
            dict_product = {'id': h.id, 
                            'material_code': h.material_code,
                            'material_name': h.name,
                            'material_type': h.material_type,
                            'material_buy_price': h.buy_price,
                            'supplier': data_supplier}
            data_material.append(dict_product)
        data = {
                'status': 200,
                'message': 'success',
                'response': data_material
            }
        try:
            return werkzeug.wrappers.Response(
                    status=200,
                    content_type='application/json; charset=utf-8',
                    response=json.dumps(data)
                )
        except:
            return werkzeug.wrappers.Response(
                status=400,
                content_type='application/json; charset=utf-8',
                headers=[('Access-Control=Allow-Origin', '*')],
                response=json.dumps({
                        'error' : 'ERROR',
                        'error_descrip': 'Something Wrong',
                    })
                )
            
    @http.route(['/api/product_material_get_cotton/'], type='http', auth='public', methods=['GET'], csrf=False)
    def material_resapi_get_cotton(self, **params):
        material = request.env['product.material'].sudo().search([('material_type', 'ilike', 'cotton')])
        data_supplier ={}
        data_material =[]
        for h in material:
            for partner in h.supplier:
                data_supplier = {'supplier_id': partner.id, 
                                 'supplier_name': partner.name}
            dict_product = {'id': h.id, 
                            'material_code': h.material_code,
                            'material_name': h.name,
                            'material_type': h.material_type,
                            'material_buy_price': h.buy_price,
                            'supplier': data_supplier}
            data_material.append(dict_product)
        data = {
                'status': 200,
                'message': 'success',
                'response': data_material
            }
        try:
            return werkzeug.wrappers.Response(
                    status=200,
                    content_type='application/json; charset=utf-8',
                    response=json.dumps(data)
                )
        except:
            return werkzeug.wrappers.Response(
                status=400,
                content_type='application/json; charset=utf-8',
                headers=[('Access-Control=Allow-Origin', '*')],
                response=json.dumps({
                        'error' : 'ERROR',
                        'error_descrip': 'Something Wrong',
                    })
                )
     
    @http.route(['/api/product_material_get_jeans/'], type='http', auth='public', methods=['GET'], csrf=False)
    def material_resapi_get_jeans(self, **params):
        material = request.env['product.material'].sudo().search([('material_type', 'ilike', 'jeans')])
        data_supplier ={}
        data_material =[]
        for h in material:
            for partner in h.supplier:
                data_supplier = {'supplier_id': partner.id, 
                                 'supplier_name': partner.name}
            dict_product = {'id': h.id, 
                            'material_code': h.material_code,
                            'material_name': h.name,
                            'material_type': h.material_type,
                            'material_buy_price': h.buy_price,
                            'supplier': data_supplier}
            data_material.append(dict_product)
        data = {
                'status': 200,
                'message': 'success',
                'response': data_material
            }
        try:
            return werkzeug.wrappers.Response(
                    status=200,
                    content_type='application/json; charset=utf-8',
                    response=json.dumps(data)
                )
        except:
            return werkzeug.wrappers.Response(
                status=400,
                content_type='application/json; charset=utf-8',
                headers=[('Access-Control=Allow-Origin', '*')],
                response=json.dumps({
                        'error' : 'ERROR',
                        'error_descrip': 'Something Wrong',
                    })
                )
            
    @http.route(['/api/product_material_get_fabric/'], type='http', auth='public', methods=['GET'], csrf=False)
    def material_resapi_get_fabric(self, **params):
        material = request.env['product.material'].sudo().search([('material_type', 'ilike', 'fabric')])
        data_supplier ={}
        data_material =[]
        for h in material:
            for partner in h.supplier:
                data_supplier = {'supplier_id': partner.id, 
                                 'supplier_name': partner.name}
            dict_product = {'id': h.id, 
                            'material_code': h.material_code,
                            'material_name': h.name,
                            'material_type': h.material_type,
                            'material_buy_price': h.buy_price,
                            'supplier': data_supplier}
            data_material.append(dict_product)
        data = {
                'status': 200,
                'message': 'success',
                'response': data_material
            }
        try:
            return werkzeug.wrappers.Response(
                    status=200,
                    content_type='application/json; charset=utf-8',
                    response=json.dumps(data)
                )
        except:
            return werkzeug.wrappers.Response(
                status=400,
                content_type='application/json; charset=utf-8',
                headers=[('Access-Control=Allow-Origin', '*')],
                response=json.dumps({
                        'error' : 'ERROR',
                        'error_descrip': 'Something Wrong',
                    })
                )    