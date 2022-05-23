"""This"""

from odoo import models, fields, api
import datetime
from dateutil.relativedelta import relativedelta


class InheritResPartnerToCalculateAge(models.Model):
    _inherit = 'sale.order'

    @api.depends('date_of_birth_date')
    def _compute_calculate_age(self):
        if self.date_of_birth_date:
            yrs = relativedelta(datetime.date.today(), self.date_of_birth_date)
            self.your_age = yrs.years
        else:
            self.your_age = 0
