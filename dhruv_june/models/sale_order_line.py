"""This"""

from odoo import models, fields, api


class AddFieldToSaleOrderLine(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'sale.order.line'
    _description = "Sale order line."

    order_line_length = fields.Float(string="Length", related="product_id.add_length")
    order_line_total_length = fields.Float(string="Total Length", compute="_compute_amount")

    @api.depends('order_line_length')
    def _compute_amount(self):
        res = super(AddFieldToSaleOrderLine, self)._compute_amount()
        for order in self:
            order.order_line_total_length = order.order_line_length * order.product_uom_qty
            order.price_subtotal = order.order_line_length * order.product_uom_qty * order.price_unit
        return res

        # self.order_line_total_length = self.order_line_length * self.product_uom_qty
        # res = super(AddFieldToSaleOrderLine, self)._compute_amount()
        # self.price_unit = self.product_id.list_price
        # self.price_subtotal = self.order_line_length * self.product_uom_qty * self.price_unit
        # self.update({
        #     'price_unit': self.price_unit,
        #     'price_subtotal': self.price_subtotal
        # })
        #
        # return res









# @api.depends('order_line_total_length')
# def _compute_calculate_sub_total(self):
#     """In order_product_record, I'd browse"""
#     res = super(AddFieldToSaleOrderLine, self)._compute_amount(self)
#     for rec in self:
#         # sub_total = rec.order_line_length * rec.product_uom_qty * rec.price_unit
#         rec.update({
#             'price_unit': rec.product_id.list_price,
#             'price_subtotal': rec.order_line_length * rec.product_uom_qty * rec.price_unit
#         })
#     return res
#     # self.update({'order_line': updated_sub_total})


# @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
#     def _compute_amount(self):
#         """
#         Compute the amounts of the SO line.
#         """
#         for line in self:
#             price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
#             taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
#             line.update({
#                 'price_tax': taxes['total_included'] - taxes['total_excluded'],
#                 'price_total': taxes['total_included'],
#                 'price_subtotal': taxes['total_excluded'],
#             })
#             if self.env.context.get('import_file', False) and not self.env.user.user_has_groups('account.group_account_manager'):
#                 line.tax_id.invalidate_cache(['invoice_repartition_line_ids'], [line.tax_id.id])
