"""This"""

from odoo import models, fields, api


class PratikSaleOrder(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'sale.order'
    _description = "Created this module."

    total_capacity = fields.Float(string="Total Capacity")

    def calculate_the_total_capacity(self):
        value = {}
        for rec in self:
            order = rec.env['sale.order'].browse(self.id)
            print("_______________________________________", order)
            for res in order:
                current_total = 0
                for record in res.order_line:
                    current_total += record.max_qty_allowed
                res.total_capacity = current_total
            return value
