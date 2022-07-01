"""This"""
from odoo import models, fields, api


class AddFieldToSaleOrder(models.Model):
    """Inherited sale_order."""
    _inherit = 'sale.order'
    _description = "Sale Order"

    add_product_id = fields.Many2one('product.product', string="Product")
    add_product_quantity = fields.Float(string="Quantity")

    @api.onchange('add_product_id', 'add_product_quantity')
    def create_order_line_onselect_product_qty(self):
        """In order_product_record, I'd browse"""
        updated_order_line_record = []
        for rec in self:
            updated_order_line_record.append((0, 0, {
                'product_id': rec.add_product_id.id,
                'name': rec.add_product_id.name,
                'order_id': rec.id,
                'price_unit': rec.add_product_id.list_price,
                'product_uom_qty': rec.add_product_quantity,
                'product_uom': rec.add_product_id.uom_id.id
            }))
        self.update({'order_line': updated_order_line_record})
