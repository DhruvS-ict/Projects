# -*- coding: utf-8 -*-
from odoo import models, fields


class ContactSaleHistory(models.Model):
    _name = 'contact.sale_history'
    _description = 'Contact Sale History'

    contact_sale_id = fields.Many2one('contact.sale')

    old_state = fields.Char(string="Old State")
    new_state = fields.Char(string="New State")
    old_follow_up_no = fields.Integer(string="Old No. of follow ups")
    new_follow_up_no = fields.Integer(string="New No. of follow ups")
