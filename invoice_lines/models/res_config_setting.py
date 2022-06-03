"""This"""

from odoo import models, fields, api


class InvoiceLinesResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    group_que = fields.Boolean(string="Invoice Group Menu", implied_group="invoice_lines.group_que")
