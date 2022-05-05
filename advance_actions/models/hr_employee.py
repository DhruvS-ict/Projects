"""This"""

from odoo import models, fields, api


class InheritEmployees(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'hr.employee'
    _description = "Created this module."

    # name = fields.Char(string="Name")
    age = fields.Char(string="Age")
