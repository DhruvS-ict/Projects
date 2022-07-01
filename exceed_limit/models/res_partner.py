"""This"""
from odoo import models, fields, api


class ContactsExceedLimit(models.Model):
    """Inherit sale_order."""
    _inherit = 'res.partner'
    _description = "Contacts"

    credit_limit = fields.Boolean(string="Credit Limit")
    credit_limit_score = fields.Float(string="Credit Limit Score")
    blocking_limit = fields.Boolean(string="Blocking Limit")
    blocking_limit_score = fields.Float(string="Blocking Limit Score")

