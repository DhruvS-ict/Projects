"""This"""

from odoo import models, fields, api


class ProductVariant(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'product.product'
    _description = "Created this module."

    qty_on_order = fields.Float(string="Quantity on Order", default="1.0")
