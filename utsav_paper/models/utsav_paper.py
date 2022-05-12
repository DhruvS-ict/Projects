"""This"""
from odoo import models, fields, api
from datetime import date


class UtsavPaper(models.Model):
    """This class is for fields & orm methods."""
    _name = 'utsav.paper'
    _description = "Created this module."

    utsav_paper_name = fields.Char(string="Name", required=True)
