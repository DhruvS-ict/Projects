"""This"""
from odoo import models, fields, api


class SaleWizard(models.TransientModel):
    """This class is for wizard object."""
    _name = 'res.wizard'
    _description = 'res.wizard'

    order_record_ids = fields.One2many('order.partner', 'res_record_id', string="Record")

    def create_so(self):
        print("-------------------------------------------SSSSSSS--------------------------------------")
        lst = []
        for res in self.order_record_ids:
            lst.append((0, 0, {
                'product_id': res.order_product_id.id,
                'product_uom_qty': res.order_quantity,
                'price_unit': res.order_unit_price
            }))
        for rec in self._context.get('active_ids'):
            vals = self.env['sale.order'].create({'partner_id': rec, 'order_line': lst})
            print("--------------------", vals)
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': 'http://localhost:15000/web?debug=1#cids=1&menu_id=214&action=316&model=sale.order&view_type=list'
        }


class SaleOneToMany(models.TransientModel):
    """This class is created for one to many field."""
    _name = 'order.partner'

    res_record_id = fields.Many2one('res.wizard', string="Res Record")
    order_product_id = fields.Many2one('product.product', string="Product")
    order_quantity = fields.Float(string="Quantity")
    order_unit_price = fields.Float(string="Unit Price", related='order_product_id.list_price')
