"""This"""
from odoo import models, fields, api


class PromotionslDiscountSaleOrder(models.Model):
    """Inherit sale_order."""
    _inherit = 'sale.order'
    _description = "Sale Order"

    button_visible = fields.Boolean(string="Button Visible", compute="_compute_button_visible")

    def apply_promotional_discount(self):
        print("AAA")
        min_discount = []
        promotion = self.env['promotional.discount'].search(
            [('date_start', '<=', self.date_order), ('date_end', '>=', self.date_order),
             ('minimum_order_amount', '<', self.amount_total)])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~promotion :- ", promotion)
        discount_product = self.env['product.product'].search([('default_code', '=', 'DISC')])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~discount :- ", discount_product)
        for rec in promotion:
            print("~~~~~~~~~~~~~rec   ", rec)
            if rec.discount_type == 'percent':
                percentage_value = self.order_line.price_unit - (self.order_line.price_unit * rec.discount / 100)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~percentage_value :- ", percentage_value)
                min_discount.append(percentage_value)
                print("~~~~~~~~~~~~~min_discount   ", min_discount)
            elif rec.discount_type == 'fixed':
                min_discount.append(rec.discount)
                print("~~~~~~~~~~~~~min_discount   ", min_discount)

        for line in self.order_line:
            print("~~~~~~~~~~~~~line   ", line)
            line.create({
                'product_id': discount_product.id,
                'name': discount_product.name,
                'order_id': self.id,
                'price_unit': -(min(min_discount))
            })
            print("~~~~~~~~~~~~~~~~~~~~~~~~order_id : ", self.id)
            final_discount_value = line.price_unit - min(min_discount)
            print("~~~~~~~~~~~~~~~~~~~~~~~~final_discount_value : ", final_discount_value)

            self.update({'amount_total': final_discount_value})

        # email_sent = self.env.ref('promotional_discount.promotional_discount_email').id
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``email_sent : ", email_sent)
        # self.env['mail.template'].browse(email_sent).send_mail(self.id, force_send=True)

    @api.depends('order_line')
    def _compute_button_visible(self):
        product_env = self.env['product.product'].search([('default_code', '=', 'DISC')])
        for line in self.order_line:
            if line.product_id.id == product_env.defaul_code.id:
                self.button_visible = False
            else:
                self.button_visible = True

