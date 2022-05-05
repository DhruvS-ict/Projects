"""This"""

from odoo import models, fields, api
from datetime import datetime


class Exam(models.Model):
    """This class is for fields & orm methods."""
    _name = 'second.exam'
    _description = "Created this module."

    name = fields.Char(string="Name")
