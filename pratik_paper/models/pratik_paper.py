"""This"""
from odoo import models, fields, api
from datetime import date


class PratikPaper(models.Model):
    """This class is for fields & orm methods."""
    _name = 'pratik.paper'
    _description = "Created this module."

    name = fields.Char(string="Name", required=True)
