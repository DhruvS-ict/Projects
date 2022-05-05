from odoo import models, fields, api
from datetime import datetime


class birthDate(models.Model):
    _inherit = 'res.partner'
    user_dob = fields.Date(string="Birth Date")
    file_upload = fields.Binary()
    street3 = fields.Char(string="Street3")
    description = fields.Text(string="Description")
    character_reference = fields.Char(string="Character Reference", )
    user_number = fields.Integer(string="User Number")
    customer_reference = fields.Char()
    attach_docs = fields.Binary()
    cus_id = fields.Many2one('sale.order', string="cus_id")
    cus_details = fields.Many2many('sale.order', string="cus_details")
    cus_head = fields.Selection([('option1', 'Edit'),('option2','Update'),('option3','Delete')],'cus_head')
    cus_img = fields.Binary(string="cus_img")
    smart_test = fields.Text(string="smart_test")
