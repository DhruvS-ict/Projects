"""This"""
from odoo import models, fields, api


class ProductTemplate(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'product.template'
    _description = "Created this module."

    is_rental = fields.Boolean(string="Is Rental", required=True)
    rental_type = fields.Many2one('rental.type', string="Rental Type")
    # domain="[('rental_type', '=', 'True')]")