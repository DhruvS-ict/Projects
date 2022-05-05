"""This"""

from odoo import models, fields, api


class InheritResServerAction(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'res.partner'
    _description = "Created this module."

    def advance_action_change(self):
        """This is onchange api model."""
        # record_to_update = self.env['res.partner']
        # if record_to_update.exists():
        #     vals={}
        self.write({'name':'Kavish Shah','phone':'+56 77989745634','email':'kavish1234@gmail.com'})


    def advance_action_create(self):
        """This is onchange api model."""
        vals={'name':'Dhruv Shah','phone':'+34 67857868978','email':'dhruvshah526@gmail.com'}
        self.env['res.partner'].create(vals)