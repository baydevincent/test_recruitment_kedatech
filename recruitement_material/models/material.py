from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.exceptions import ValidationError


class ProductMaterial(models.Model):
    _name = 'product.material'

    material_code = fields.Char('Material Code', required=True, default='New')
    name = fields.Char('Material Name', required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')], required=True, index=True)
    buy_price = fields.Integer(string='Material Buy Price', required=True)
    supplier = fields.Many2one('res.partner', string='Related Supplier', required=True)
    
    @api.constrains('buy_price')
    def check_buy_price(self):
        if self.buy_price < 100:
            raise ValidationError(_("Buy Price kurang dari 100!"))