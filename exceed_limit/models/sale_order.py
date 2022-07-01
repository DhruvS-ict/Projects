"""This"""
from odoo import models, fields, api
from odoo.exceptions import UserError


class SaleOrderExceedLimit(models.Model):
    """Inherit sale_order."""
    _inherit = 'sale.order'
    _description = "Sale Order"

    @api.model
    def create(self, vals):
        total_credit = []
        total_block = []
        sale_credit = self.search([('state', '=', 'draft'), ('partner_id', '=', vals.get('partner_id'))])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~sale_credit: ", sale_credit)
        sale_block = self.search([('state', '=', 'sale'), ('partner_id', '=', vals.get('partner_id'))])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~sale_block: ", sale_block)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~vals: ", vals)
        for credit in sale_credit:
            total_credit.append(credit.amount_total)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~total amount: ", total_credit)
            total_credit_limit = sum(total_credit)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~total_credit_limit: ", total_credit_limit)
            if total_credit_limit > credit.partner_id.credit_limit_score:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~credit_limit_score", self.partner_id.credit_limit_score)
                raise UserError("Your Sale Order Credit Limit has been Exceeded.")
            else:
                pass
        for block in sale_block:
            total_block.append(block.amount_total)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~total amount: ", total_block)
            total_block_limit = sum(total_block)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~total_block_limit: ", total_block_limit)
            if total_block_limit > block.partner_id.blocking_limit_score:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~block_limit_score", self.partner_id.blocking_limit_score)
                sale_block.send_email()
                raise UserError("You cannot create SO as the Block Limit has been Exceeded.")
            else:
                pass
        return super(SaleOrderExceedLimit, self).create(vals)

    def send_email(self):
        email_send = self.env.ref('SaleOrderExceedLimit.promotional_discount_email').id
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~email_sent : ", email_send)
        self.env['mail.template'].browse(email_send).send_mail(self.id, force_send=True)
