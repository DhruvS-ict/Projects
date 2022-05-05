"""This"""

from odoo import models, fields, api


class InvoiceLines(models.Model):
    """This class is for fields & orm methods."""
    _name = 'invoice.lines'
    _description = "Created this module."

    invoices_name = fields.Char(string="Name")
    invoices_email = fields.Char(string="Email")
    invoices_salary = fields.Float(string="Salary")
    invoices_summary = fields.Text(string="Summary")
    invoices_stages = fields.Selection([('draft', 'Draft'), ('approved', 'Approved'),
                               ('cancel', 'cancel')], string="Stages")

