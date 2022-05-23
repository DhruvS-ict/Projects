"""This"""

from odoo import models, fields, api
from datetime import datetime


class ContactSale(models.Model):
    """This class is for fields & orm methods."""
    _name = 'contact.sale'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _description = "Created this module."
    _rec_name = 'contact_sale_name'

    contact_sale_name = fields.Char(string="Name", readonly=1)
    contact_id = fields.Many2one('res.partner', string="Contact", tracking=True)
    sale_order_id = fields.Many2one('sale.order', string="Sale Order", tracking=True)
    sales_person = fields.Many2one('res.users', related="sale_order_id.user_id", readonly=1)
    follow_ups_no = fields.Integer(string="Followups Number")
    contact_sale_history_lines_ids = fields.One2many('contact.sale.history', 'contact_sale_id',
                                                     string="Contact Sale History Lines")
    status = fields.Selection([('draft', 'draft'), ('in progress', 'In Progress'),
                               ('done', 'done'), ('cancel', 'Cancel')], string="Status", default='draft')

    @api.model
    def create(self, vals):
        print("Contact Sale Token Generates in process................", vals)
        vals['contact_sale_name'] = self.env['ir.sequence'].next_by_code("contact.sale")
        return super(ContactSale, self).create(vals)

    def contact_sale_draft(self):
        print("DDD")
        for rec in self:
            rec.status = 'draft'

    def contact_sale_in_progress(self):
        print("III")
        for rec in self:
            rec.status = 'in progress'

    def contact_sale_done(self):
        print("DoDoDo")
        for rec in self:
            rec.status = 'done'

    def contact_sale_cancel(self):
        print("CCC")
        for rec in self:
            rec.status = 'cancel'


class ContactSaleHistory(models.Model):
    _name = 'contact.sale.history'

    contact_sale_id = fields.Many2one('contact.sale', string="Contact Sale")
    old_state = fields.Char(string="Old State")
    new_state = fields.Char(string="New State")
    old_no_follow_ups = fields.Integer(string="Old No Followups")
    new_no_follow_ups = fields.Integer(string="New No Followups")





# • Contact (M2O Res Partner)
# • Sale Order (Allow to select Sale Order which has above selected contact)
# • Salesperson (Automatically set based on Sale Order)
# • Status (Draft, in progress, Done, Cancel)
# • No. of follow ups
# • Contact Sale History Lines (O2M of Contact Sale History)