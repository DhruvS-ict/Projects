"""This"""

from odoo import models, fields, api
# import datetime
# from ast import literal_eval


class ResConfigSettingExeedLimit(models.TransientModel):
    _inherit = 'res.config.settings'

    exceed_limit_mail = fields.Char(string="Notify Person for limit Exceed",
                                    config_parameter="exceed_limit.exceed_limit_mail")

    # @api.depends('exceed_limit_mail')
    # def _compute_send_email(self):
        # email_send = self.env.ref('ResConfigSettingExeedLimit.promotional_discount_email').id
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``email_sent : ", email_send)
        # self.env['mail.template'].browse(email_send).send_mail(self.id, force_send=True)

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
    # @api.model
    # def set_values(self):
    #     res = super(InheritResConfigSetting, self).set_values()
    #     self.env['ir.config_parameter'].set_param('exam.current_month_ids', self.current_month_ids.ids)
    #     return res


