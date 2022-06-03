"""This"""
from odoo import models, fields, api


class InvoiceLinesWizard(models.TransientModel):
    """This class is for wizard object."""
    _name = 'invoice.wizard'
    _description = 'created wizard'

    wizard_name_id = fields.Char(string="Name")
    wizard_email = fields.Char(string="Email")
    wizard_salary = fields.Float(string="Salary")
    wizard_summary = fields.Text(string="Summary")
    wizard_stages = fields.Selection([('draft', 'Draft'), ('approved', 'Approved'),
                                      ('cancel', 'cancel')], string="Stages")

    def invoice_wizard_submit(self):
        context = self._context
        print("____________________________context", context)
        wizard_id = self.env[context['active_model']].browse(context['active_id'])
        wizard_id.write({
            'invoices_name': self.wizard_name_id,
            'invoices_email': self.wizard_email,
            'invoices_salary': self.wizard_salary,
            'invoices_summary': self.wizard_summary,
            'invoices_stages': self.wizard_stages
        })
        