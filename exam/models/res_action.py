"""This"""

from odoo import models, fields, api


class InheritResPartnerToCalculateAge(models.Model):
    _inherit = 'res.partner'
    _description = "Created this module."


