import json
# import requests
from odoo import http, _, exceptions
from odoo.http import request, Response
from odoo.tests import Form
import werkzeug.wrappers

class MaterialRestApi(http.Controller):
    @http.route(['/api/product_material_delete/<int:id>'], type='http', auth='public', methods=['DELETE'], csrf=False)
    def material_resapi_delete(self, id, **kwargs):
        material = request.env['product.material'].sudo().search([('id', '=', id)])
        
        if not material:
            return Response(
                    json.dumps({'status': 404,'message': 'Data material tidak ditemukan'}),
                    status=404,
                    content_type='application/json'              
                )
            
        material.sudo().unlink()
        return Response(
                    json.dumps({'status': 200,'message': 'Data Berhasil dihapus'}),
                    status=200,
                    content_type='application/json'              
                )
        
    @http.route(['/api/product_material_edit/<int:id>'], type='json', auth='public', methods=['PUT'], csrf=False)
    def material_resapi_edit(self, id, **params):
    
        try:
            load = request.jsonrequest
        except Exception as e:
            return Response(
                status=400,
                content_type='application/json'
            )
        

        material = request.env['product.material'].sudo().search([('id', '=', id)])   

        if not material:
            return Response(
                    status=404,
                    content_type='application/json'              
                )
        editable_field = {'material_type', 'material_code', 'name', 'buy_price', 'supplier'}
        update_field ={k: v for k, v in load.items() if k in editable_field}
        
        if not update_field:
            return Response(
                    status=400,
                    content_type='application/json'              
                )
        
        try:
            material.write(update_field)
        except Exception as e:
            return Response(
                    status=500,
                    content_type='application/json'       
                )
        
        return werkzeug.wrappers.Response(
                    status=200,
                    content_type='application/json; charset=utf-8',
                    response=json.dumps({'status': 200,'message': 'Data Berhasil dihapus'})
                )          
                