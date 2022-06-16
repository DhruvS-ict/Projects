"""This"""
from odoo import models, fields, api


class BatchWizard(models.TransientModel):
    """This class is for wizard object."""
    _name = 'batch.wizard'
    _description = 'Batch Wizard'

    batch_order_ids = fields.One2many('batch.order', 'batch_sale_order_id', string="Batch Order")

    @api.model
    def default_get(self, fields):
        """In this default_get function, wizard gets open with default values of selected
        sale_order_ids --> order_line. By assigning order_line of selected sale_order_ids
        to batch_order_ids field."""
        lst = []
        res = super(BatchWizard, self).default_get(fields)
        rec = self.env['batch.sale.workflow'].browse(self.env.context.get('active_ids'))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~rec: ", rec)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~rec: ", rec.batch_sale_order_ids)
        if rec.batch_sale_order_ids:
            for line in rec.batch_sale_order_ids:
                lst.append((0, 0, {
                    'batch_order_product_id': line.order_line.product_id.id,
                    'batch_order_name': line.order_line.name,
                    'batch_order_unit_price': line.order_line.price_unit,
                    'batch_order_quantity': line.order_line.product_uom_qty
                }))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~lst: ", lst)
            vals = res.update({'batch_order_ids': lst})
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~vals : ", vals)
            return res

    def create_new_sale_order(self):
        """In this function new sale order is created by assigning batch_order_ids(O2m)
        value to sale order_line fields."""
        """And active_ids is used to fetch current record in batch_sale_workflow and get 
        customer_id from active record."""
        list_d = []
        batch_env = self.env['batch.sale.workflow']
        print("_________________________________???___________batch_env : ", batch_env.batch_customer_id.id)
        if self.batch_order_ids:
            for batch_line in self.batch_order_ids:
                list_d.append((0, 0, {
                    'product_id': batch_line.batch_order_product_id.id,
                    'name': batch_line.batch_order_name,
                    'price_unit': batch_line.batch_order_unit_price,
                    'product_uom_qty': batch_line.batch_order_quantity
                }))
                print("________________________???__________list : ", list_d)
            rec = batch_env.browse(self.env.context.get('active_ids'))
            self.env['sale.order'].create({'partner_id': rec.batch_customer_id.id, 'order_line': list_d})


class BatchOneToMany(models.TransientModel):
    """This class is created for one to many field."""
    _name = 'batch.order'

    batch_sale_order_id = fields.Many2one('batch.wizard', string="Batch Record")
    batch_order_product_id = fields.Many2one('product.product', string="Product")
    batch_order_name = fields.Text(string="Description")
    batch_order_unit_price = fields.Float(string="Unit Price", related='batch_order_product_id.list_price')
    batch_order_quantity = fields.Float(string="Quantity")
