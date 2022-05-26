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
    contact_id = fields.Many2one('res.partner', string="Contact")
    sale_order_id = fields.Many2one('sale.order', string="Sale Order")
    sales_person = fields.Many2one('res.users', related="sale_order_id.user_id", store=True, readonly=1)
    follow_ups_no = fields.Integer(string="Followups Number")
    contact_sale_history_lines_ids = fields.One2many('contact.sale.history', 'contact_sale_id',
                                                     string="Contact Sale History Lines")
    status = fields.Selection([('draft', 'draft'), ('in progress', 'In Progress'),
                               ('done', 'done'), ('cancel', 'Cancel')], string="Status", default='draft')

    @api.model
    def create(self, vals):
        print("...........................Contact Sale Token Generates in process................", vals)
        vals['contact_sale_name'] = self.env['ir.sequence'].next_by_code("contact.sale")
        return super(ContactSale, self).create(vals)

    def contact_sale_draft(self):
        print("DDD")
        self.history_lines('draft')
        self.message_post(body=(('%s has been changed') % (self.contact_id.name),
                                ('%s has been changed') % (self.sale_order_id.name)))

    def contact_sale_in_progress(self):
        print("III")
        self.history_lines('in progress')
        self.message_post(body=(('%s has been changed') % (self.contact_id.name),
                                ('%s has been changed') % (self.sale_order_id.name)))

    def contact_sale_done(self):
        print("DoDoDo")
        self.history_lines('done')
        self.message_post(body=(('%s has been changed') % (self.contact_id.name),
                                ('%s has been changed') % (self.sale_order_id.name)))

    def contact_sale_cancel(self):
        print("CCC")
        self.history_lines('cancel')
        self.message_post(body=(('%s has been changed') % (self.contact_id.name),
                                ('%s has been changed') % (self.sale_order_id.name)))

    def history_lines(self, state):
        old_status = self.status
        print("___________________________________________Old Staus : ", old_status)
        old_followup_no = self.follow_ups_no
        print("___________________________________________Old Followup : ", old_followup_no)
        self.follow_ups_no += 1
        new_followup_no = self.follow_ups_no
        print("___________________________________________New Followup : ", new_followup_no)
        self.status = state
        new_status = self.status
        print("___________________________________________New Staus : ", new_status)
        history = {
            'old_state': old_status,
            'new_state': new_status,
            'old_no_follow_ups': old_followup_no,
            'new_no_follow_ups': new_followup_no
        }
        self.write({'contact_sale_history_lines_ids': [(0, 0, history)]})


class ContactSaleHistory(models.Model):
    _name = 'contact.sale.history'

    contact_sale_id = fields.Many2one('contact.sale', string="Contact Sale")
    old_state = fields.Char(string="Old State")
    new_state = fields.Char(string="New State")
    old_no_follow_ups = fields.Integer(string="Old No Followups")
    new_no_follow_ups = fields.Integer(string="New No Followups")





# Define fields
# partner_id = fields.Many2one('res.partner',  'Partner') # This standard field.
# partner_id_new = fields.Many2one('res.partner',  'Partner New') # This custom field.
# partner_id_old = fields.Many2one('res.partner',  'Partner' Old) # This custom field.
#
# Define onchange method
# @api.onchange('partner_id')
# def onchange_partner_id(self):
#     OldPartner = self.partner_id_new
#     self.partner_id_new = self.partner_id
#     self.partner_id_old = OldPartner
# you can get old partner on partner_id_old fields.)
