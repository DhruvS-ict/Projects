"""This"""

from odoo import models, fields, api


class AdvanceAction(models.Model):
    """This class is for fields & orm methods."""
    _name = 'advance.action'
    _description = "Created this module."
    _rec_name = "advance_users"

    advance_users = fields.Char(string="Name")
    state = fields.Selection([('draft', 'Draft'), ('waiting', 'Waiting'),
                              ('approve', 'Approve'), ('cancel', 'Cancel')],
                             string="State")
    # user_mail_address = fields.Char(string="User Email")
    # # customer_mail_address = fields.Char(string="Customer Email")
    # send_email_to = fields.Char(string="Email to")
    from_email = fields.Char(string="email from")
    to_email = fields.Char(string="email to")

    # def send_email(self):
    #     template_id = self.env.ref('advance_actions.advance_actions_email_template_id').id
    #     self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
    def email_send(self):
        """This function is created to send email on button click."""
        email_sent = self.env.ref('advance_actions.new_advance_actions_email_template_id').id
        self.env["mail.template"].browse(email_sent).send_mail(self.id, force_send=True)
