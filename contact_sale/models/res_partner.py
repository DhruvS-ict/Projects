"""This"""

from odoo import models, fields, api
import datetime
from dateutil.relativedelta import relativedelta


class ContactSaleResPartner(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'res.partner'
    _description = "Created this module."

    contact_sale_count = fields.Integer(compute="test")

    def test(self):
        for rec in self:
            rec.contact_sale_count = self.env['contact.sale'].search_count([('contact_id', '=', rec.id)])
