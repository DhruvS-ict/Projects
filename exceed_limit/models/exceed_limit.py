"""This"""

from odoo import models, fields, api


class PromotionalDiscount(models.Model):
    """This class is for fields & orm methods."""
    _name = 'promotional.discount'
    _description = 'promotional discount'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _rec_name = 'product_name'

    product_name = fields.Char(string='Product Name')
    discount_type = fields.Selection([('percent', 'Percentage'), ('fixed', 'Fixed Amount')],
                                     string='Discount Type', required=True)
    discount = fields.Float(string='Discount', store=True)
    minimum_order_amount = fields.Integer(string='Minimum Order Amount')
    date_start = fields.Datetime(string='Start Date')
    date_end = fields.Datetime(string='End Date')
    currency_id = fields.Many2one('res.currency', string='Discount Currency', default=2)
    # fixed_amount = fields.Float('Discount (Fixed)')
    discounted_mail_id = fields.Char(string='E-mail')
    discounted_customer_id = fields.Many2one('res.partner', string='Discounted Customer')

    def send_email(self):
        email_sent = self.env.ref('promotional_discount.promotional_discount_email').id
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``email_sent : ", email_sent)
        self.env['mail.template'].browse(email_sent).send_mail(self.id, force_send=True)
    # @api.onchange('discount_type')
    # @api.model
    # def create(self, vals):
    #     res = super(PromotionalDiscount, self).create(vals)
    #     if vals.get('discount_type') == 'percent':
    #         res['discount'] = res['discount'] + "%"
    #     elif vals.get('discount_type') == 'fixed':
    #         res['discount'] = res['discount'] + "₹"
    #     return res


    # def write(self, vals):
    #     rec = self.env('res.currency').search([])
    #     if vals.get('discount_type') == 'percent':
    #         vals['discount'] = vals['discount'] + "%"
    #     elif vals.get('discount_type') == 'fixed':
    #         vals['discount'] = rec.currency_id.id + vals['discount']
    #     return super(PromotionalDiscount, self).write(vals)
        # discount = self.default_get(['discount']).get('discount')
        # print("`````````````````````````````````````````````discount  : ", discount)
        # return {'value': {'discount': discount}}
