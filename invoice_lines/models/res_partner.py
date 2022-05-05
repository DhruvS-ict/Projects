"""This"""

from odoo import models, fields, api
import random
import string


class InheritResPartnerInInvoiceLines(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'res.partner'
    _description = "Created this module."

    token_no = fields.Char(string="Token No")

    def generate_random_number(self):
        """This function is for generate random numbers on click of button."""
        var1 = random.choice(string.digits)
        var2 = random.choice(string.ascii_letters)
        var3 = random.choice(string.ascii_letters)
        self.token_no = var1 + var2 + var3 + "-M"
