"""This"""
from odoo import models, fields, api


class AddFieldToProducts(models.Model):
    """Inherited product_product."""
    _inherit = 'product.product'
    _description = "Product"

    add_length = fields.Float(string="Length")

