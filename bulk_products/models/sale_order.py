"""This"""

from odoo import models, fields, api


class BulkSaleOrder(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'sale.order'
    _description = "Created this module."

    bulk_product_template_id = fields.Many2one('bulk.products', string="Bulk Product Template")

    @api.onchange('bulk_product_template_id')
    def create_sale_order_line(self):
        bulk_record = self.env['bulk.products'].browse(self.bulk_product_template_id.id)
        print("___________________________", bulk_record)
        new_record = []
        for rec in bulk_record.bulk_products_ids:
            new_record.append((0, 0, {
                'product_id': rec.product_id,
                'name': rec.name,
                'product_uom_qty': rec.product_uom_qty,
                'product_uom': rec.product_id.uom_id.id
            }))
        self.update({'order_line': new_record})
    # print("BBB")
    # for record in self:
    #     bulk_record = record.env['bulk.products'].search([])
    #     print("___________________________", bulk_record)
    # a = []
    # for line in record.order_line:
    #     a.append((0, 0, {
    #         'product_id': line.product_id.id,
    #         'name': line.name,
    #         'product_uom_qty': line.product_uom_qty}))
    # self.create({'partner_id': record, 'order_line': a})
    # return self
    # for rec in self:
    #     rec.order_line = [(6, 0, rec.bulk_products.mapped('product_id').ids)]