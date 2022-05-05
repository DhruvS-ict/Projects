"""This"""

from odoo import models, fields, api


class InvoiceLines(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'account.move.line'
    _description = "Created this module."

    delivery_address = fields.Many2one('res.partner', string="Delivery Address")
    vendor = fields.Many2one('res.partner', string="Vendor", domain=[('supplier_rank', '>', 0)])
    vendor_price = fields.Float(string="Vendor Price")
    planned_gp = fields.Float(string="Planned GP")
    description = fields.Text(string="Description", compute="_compute_merging_two_fields")

    @api.onchange('price_unit', 'vendor_price')
    def calculate_gp(self):
        """This is onchange api model."""
        for rec in self:
            print(f"----------{self}")
            if rec.price_unit or rec.vendor_price:
                rec.planned_gp = ((rec.price_unit - rec.vendor_price) / rec.price_unit) * 100

    @api.depends('delivery_address', 'name')
    def _compute_merging_two_fields(self):
        for rec in self:
            if rec.delivery_address and rec.name:
                rec.description = ", ".join([rec.delivery_address.name, rec.name])
            else:
                rec.description = " "
