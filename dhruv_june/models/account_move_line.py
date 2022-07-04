"""This"""

from odoo import models, fields, api


class InvoiceLines(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'account.move.line'
    _description = "Created this module."

    move_line_length = fields.Float(string="Length", related="product_id.add_length")
    move_line_total_length = fields.Float(string="Total Length", compute="_compute_generate_invoice")

    @api.depends('move_line_total_length')
    def _compute_generate_invoice(self):
        for move in self:
            move.move_line_total_length = move.product_id.add_length * move.quantity
            move.price_subtotal = move.product_id.add_length * move.quantity * move.product_id.list_price
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~move_line_total_length ", move.move_line_total_length)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~move.price_subtotal ", move.price_subtotal)
