"""This"""

from odoo import models, fields, api


class PratikSaleOrderLine(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'sale.order.line'
    _description = "Created this module."

    max_qty_allowed = fields.Float(string="Max Qty Allowed", related="product_id.qty_on_order")
