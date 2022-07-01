"""This"""

from odoo import models, fields, api


class ResConfigSettingCovidDelivery(models.TransientModel):
    _inherit = 'res.config.settings'

    group_covid_delivery_message = fields.Boolean(string="Covid Delivery", implied_group="covid_delivery.group_covid_delivery_message")


