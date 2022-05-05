"""This"""

from odoo import models, fields, api


class InheritSaleAction(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'sale.order'
    _description = "Created this module."


    def state_change(self):
        """This is onchange api model."""
        # for rec in self:
        #     if rec.state == 'draft':
        #         rec.state = 'sent'
        rec = self.search([]).write({"state": "sent"})
        print("---------------------------------", rec)
