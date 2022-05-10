"""This"""

from odoo import models, fields, api
import datetime
# from ast import literal_eval


class ReferralResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    name = fields.Char(string="Name", config_parameter='hr_referral_application.name')
    expected_joining_date = fields.Datetime(string="Expected Joining Date",
                                            config_parameter='hr_referral_application.expected_joining_date')

    # @api.depends('current_month_ids')
    # def _compute_display_current_month(self):
    #     self.current_month_ids = datetime.date.today()

    # @api.model
    # def get_values(self):
    #     res = super(InheritResConfigSetting, self).get_values()
    #     save_record = self.env['ir.config_parameter'].sudo().get_param('exam.current_month_ids')
    #     # print ("??????", type(current_month_ids), type(eval(current_month_ids)))
    #     if save_record:
    #         res.update(current_month_ids=[(6, 0, eval(save_record))])
    #     return res
    #
    #
    #
    # @api.model
    # def set_values(self):
    #     res = super(InheritResConfigSetting, self).set_values()
    #     self.env['ir.config_parameter'].set_param('exam.current_month_ids', self.current_month_ids.ids)
    #     return res
