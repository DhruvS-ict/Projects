"""This"""
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class BulkProducts(models.Model):
    """This class is for fields & orm methods."""
    _name = 'bulk.products'
    _description = "Created this module."
    _rec_name = 'bulk_products_name'

    bulk_products_image = fields.Binary(string="Product Image")
    bulk_products_name = fields.Char(string="Name", required=True)
    master_product_id = fields.Many2one('product.template', string="Master Product")
    bulk_products_phone = fields.Char(string="Phone")
    bulk_products_email = fields.Char(string="Email")
    bulk_products_user_id = fields.Many2one('res.partner', string="User")
    bulk_products_ids = fields.One2many('bulk.one', 'bulk_p_id', string="Bulk Products")

# # Whatsapp Integration
#     def btn_whatsapp(self):
#         if not self.bulk_products_phone:
#             raise ValidationError(("Missing Phone Number"))
#         message = 'Hi %s, this message is sent through Odoo by Whatsapp-web-api.' % (self.bulk_products_name)
#         wa_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.bulk_products_phone, message)
#         return{
#             'type': 'ir.actions.act_url',
#             'target': 'new',
#             'url': wa_api_url
#         }


class BulkProductsOneToMany(models.Model):
    """This class is created for one to many field."""
    _name = 'bulk.one'

    product_id = fields.Many2one('product.product', string="Product")
    name = fields.Text(string="Description")
    product_uom_qty = fields.Float(string="Product uom qty")
    bulk_p_id = fields.Many2one('bulk.products')
