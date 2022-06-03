"""This"""

from odoo import models, fields, api


class BatchSaleWorkFlow(models.Model):
    """This class is for fields & orm methods."""
    _name = 'batch.sale.workflow'
    _description = 'batch sale workflow'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _rec_name = 'batch_name'

    """"""
    batch_name = fields.Char(string='Name', readonly=True)
    batch_responsible_id = fields.Many2one('res.users', string="Responsible")
    """"""
    batch_operation_type = fields.Selection([('confirm', 'Confirm'), ('cancel', 'Cancel'),
                                             ('merge', 'Merge')], string="Operation Type")
    """"""
    batch_customer_id = fields.Many2one('res.partner', string="Customer")
    """"""
    batch_status = fields.Selection([('draft', 'Draft'), ('done', 'Done'),
                                     ('cancel', 'Cancel')], string="status")
    """"""
    batch_sale_order_ids = fields.Many2many('sale.order', 'batch_sale_workflow_sale_order',
                                            'batch_sale_workflow_id', 'sale_order_id', string="Sale Order")
    batch_operation_date = fields.Datetime(string="Operation Date")

    @api.model
    def create(self, vals):
        print("...........................Contact Sale Token Generates in process................", vals)
        vals['batch_name'] = self.env['ir.sequence'].next_by_code("batch.sale.workflow")
        return super(BatchSaleWorkFlow, self).create(vals)

    def proceed_operation(self):
        print("PPP")
        for rec in self:
            rec.batch_status = 'done'
        self.batch_sale_order_ids.date_order = self.batch_operation_date

    def cancel(self):
        print("CCC")
        for rec in self:
            rec.batch_status = 'cancel'

    def set_to_draft(self):
        print("SSS")
        for rec in self:
            rec.batch_status = 'draft'

    def done(self):
        print("DDD")
        for rec in self:
            rec.batch_status = 'done'

    @api.onchange('batch_operation_type')
    def confirm_state(self):
        """This is onchange api model."""
        if self.batch_operation_type in 'confirm':
            domain = [('state', '=', ['|', (['draft', 'sent'])]),
                      ('user_id', '=', self.batch_responsible_id.id)]
            return {'domain': {'batch_sale_order_ids': domain}}
        