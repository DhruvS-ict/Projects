# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models, fields, api, _


class ContactSale(models.Model):
    _name = 'contact.sale'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Contact Sale'

    name = fields.Char(default=lambda self: _('New'), readonly=True)
    partner_id = fields.Many2one("res.partner", string="Contact",
                                 default=lambda self: 
                                     self._context['active_id']
                                 if('active_id' in self._context.keys())
                                 else False,
                                 required=True, tracking=True)
    sale_order_id = fields.Many2one("sale.order", string="Sale Order",
                                    tracking=True)
    salesperson_id = fields.Many2one('res.users',
                                     related="sale_order_id.user_id",
                                     string="Salesperson")
    status = fields.Selection(selection=[('draft', 'Draft'),
                                         ('in_progress', 'in progress'),
                                         ('done', 'Done'),
                                         ('cancel', 'Cancel')],
                              string="Status",
                              default="draft")
    follow_ups_no = fields.Integer(string="Follow ups No.")
    history_line_ids = fields.One2many('contact.sale_history',
                                       'contact_sale_id')

    @api.model_create_multi
    def create(self, values):
        '''
        It ganerates the uniq sequence number for every record.
        '''
        for vals in values:
            if vals.get('name', _('New')) == _('New'):
                seq_date = None
                if 'sale_order_id' in vals:
                    seq_date = fields.Datetime.context_timestamp(
                        self, fields.Datetime.to_datetime(datetime.today()))
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'contact.sale', sequence_date=seq_date) or _('New')
        return super(ContactSale, self).create(values)

    def set_draft(self):
        '''
        set status to 'Dtaft' status.
        Creates the History line.
        '''
        self.change_state('draft')

    def set_in_progress(self):
        '''
        set status to 'In Progress' status.
        Creates the History line.
        '''
        self.change_state('in_progress')

    def set_done(self):
        '''
        set status to 'Done' status.
        Creates the History line.
        Send Mail to Contact from Salesperson.
        '''
        self.change_state('done')

        template_id = self.env.ref('contact_sale.contact_sale_mail').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)

    def set_cancel(self):
        '''
        set status to 'cancel' status.
        Creates the History line.
        '''
        self.change_state('cancel')

    def change_state(self, state):
        old_status = self.status
        old_follow_up_no = self.follow_ups_no
        msg = "Status: " + old_status + " -> "
        self.follow_ups_no += 1
        new_follow_up_no = self.follow_ups_no
        self.status = state
        new_status = self.status
        msg = msg + new_status

        dictionary = {
            'old_state': old_status,
            'new_state': new_status,
            'old_follow_up_no': old_follow_up_no,
            'new_follow_up_no': new_follow_up_no,
        }
        self.write({
                    'history_line_ids': [(0, 0, dictionary)]
                    })
        self.message_post(body=msg)


class ContactSaleFollowUps(models.Model):
    _inherit = 'res.partner'
    _description = 'Add Contact Sale Follow Ups No. field'

    contact_sale_follow_ups = fields.Integer(compute="_compute_follow_ups")

    def _compute_follow_ups(self):
        '''
        calculate follow ups for contacts.
        '''
        for rec in self:
            no = self.env['contact.sale'].search_count([
                ('partner_id', '=', rec.id)])
            rec.contact_sale_follow_ups = no

    def contact_sale_view(self):
        '''
        returns tree,form view of Contact Sale model.
        '''
        sale_count = self.env['contact.sale'].search_count(
            [('partner_id', '=', self.id)])
        print("\n\n", sale_count, "\n\n")
        if sale_count == 0:
            view_action = {
                'type': 'ir.actions.act_window',
                'res_model': "contact.sale",
                'view_mode': "form",
            }
        elif sale_count == 1:
            rec = sale_count = self.env['contact.sale'].search(
                [('partner_id', '=', self.id)])
            view_action = {
                'type': 'ir.actions.act_window',
                'res_model': "contact.sale",
                'res_id': rec.id,
                'view_mode': "form",
            }
        else:
            view_action = {
                'type': 'ir.actions.act_window',
                'res_model': "contact.sale",
                'view_mode': "tree,form",
                'domain': [('partner_id', '=', self.id)]
            }
        return view_action
