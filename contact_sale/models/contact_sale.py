"""This"""

from odoo import models, fields, api
from datetime import datetime


class ContactSale(models.Model):
    """This class is for fields & orm methods."""
    _name = 'contact.sale'
    _description = "Created this module."

    contact_sale_name = fields.Char(string="Name", readonly=1)
    contact_id = fields.Many2one('res.partner', string="Contact")
    sale_order_id = fields.Many2one('sale.order', string="Sale Order")
    sales_person = fields.Many2one('res.users', related="sale_order_id.user_id", readonly=1)
    status = fields.Selection([('draft', 'draft'), ('in progress', 'In Progress'),
                               ('done', 'done'), ('Cancel', 'Cancel')], string="Status")

    @api.model
    def create(self, vals):
        print("Contact Sale Token Generates in process................", vals)
        vals['contact_sale_name'] = self.env['ir.sequence'].next_by_code("contact.sale")
        return super(ContactSale, self).create(vals)


class ContactSaleHistory(models.Model):
    _name = 'contact.sale.history'

    contact_sale = fields.Many2one('contact.sale', string="Contact Sale")
    old_state = fields.Char(string="Old State")
    new_state = fields.Char(string="New State")





# • Contact (M2O Res Partner)
# • Sale Order (Allow to select Sale Order which has above selected contact)
# • Salesperson (Automatically set based on Sale Order)
# • Status (Draft, in progress, Done, Cancel)
# • No. of follow ups
# • Contact Sale History Lines (O2M of Contact Sale History)