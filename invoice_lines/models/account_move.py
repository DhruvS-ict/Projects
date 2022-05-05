"""This"""

from odoo import models, fields, api


class InheritAccountMoveInToInvoiceLines(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'account.move'
    _description = "Created this module."

    def generate_bill(self):
        print("BBBn")
        vendor_rec = self.invoice_line_ids.mapped("vendor.id")
        for record in vendor_rec:
            a = []
            for line in self.invoice_line_ids.filtered(lambda x: x.vendor.id == record):
                a.append((0, 0, {
                    'product_id': line.product_id.id,
                    'price_unit': line.vendor_price,
                    'delivery_address': line.delivery_address,
                    'planned_gp': line.planned_gp,
                    'description': line.description}))
            self.create({'move_type': 'in_invoice', 'partner_id': record, 'invoice_line_ids': a})
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': 'http://localhost:15000/web?debug=1#cids=1&menu_id=146&action=247&model=account.move&view_type=list'
        }
        # for rec in self:
        #     self.create({'move_type': 'in_invoice', 'partner_id': rec.invoice_line_ids.vendor})
