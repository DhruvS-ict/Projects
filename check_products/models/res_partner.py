"""This"""

from odoo import models, fields, api


class ContactCreationResPartner(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'res.partner'
    _description = "Created this module."

    contact_creation_your_name = fields.Char(string="Your Name", required=True)
    contact_creation_your_email = fields.Char(string="Your Email", required=True)
    contact_creation_phone_number = fields.Char(string="Phone Number", required=True)
    contact_creation_image = fields.Binary(string="Image", required=True)
