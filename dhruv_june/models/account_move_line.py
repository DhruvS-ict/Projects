"""This"""

from odoo import models, fields, api


class InvoiceLines(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'account.move.line'
    _description = "Created this module."

    move_line_length = fields.Float(string="Length")
    move_line_total_length = fields.Float(string="Total Length", compute="_compute_generate_invoice")

    @api.depends('move_line_total_length')
    def _compute_generate_invoice(self):
        sale_line = self.env['sale.order.line'].search([])
        new_invoice_line_create = []
        for rec in sale_line:
            new_invoice_line_create.append((0, 0, {
                'product_id': rec.product_id.id,
                'name': rec.product_id.name,
                'order_id': rec.id,
                'price_unit': rec.price_unit,
                'quantity': rec.product_uom_qty,
                'product_uom': rec.product_uom.id,
                'move_line_length': rec.order_line_length,
                'move_line_total_length': rec.order_line_total_length,
                'price_subtotal': rec.price_subtotal
            }))
        self.create({'invoice_line_ids': new_invoice_line_create})