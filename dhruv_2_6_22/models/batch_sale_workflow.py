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
                                             ('merge', 'Merge')], string="Operation Type", default='confirm',
                                            required=True)
    """"""
    batch_customer_id = fields.Many2one('res.partner', string="Customer")
    """"""
    batch_status = fields.Selection([('draft', 'Draft'), ('done', 'Done'),
                                     ('cancel', 'Cancel')], string="status", default='draft')
    """"""
    batch_sale_order_ids = fields.Many2many('sale.order', 'batch_sale_workflow_sale_order',
                                            'batch_sale_workflow_id', 'sale_order_id', string="Sale Order")
    batch_operation_date = fields.Datetime(string="Operation Date")

    @api.model
    def create(self, vals):
        print("...........................Contact Sale Token Generates in process................", vals)
        vals['batch_name'] = self.env['ir.sequence'].next_by_code("batch.sale.workflow")
        return super(BatchSaleWorkFlow, self).create(vals)

    def proceed_operation_button(self):
        for rec in self:
            rec.batch_status = 'done'
        self.batch_sale_order_ids.write({
            'date_order': self.batch_operation_date
        })
        if self.batch_operation_type == 'merge':
            action = {
                "name": "Batch wizard",
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "res_model": "batch.wizard",
                "target": "new",
                # "context": {'active_ids': records.ids}
            }
            return action
        # # sale_env = self.env['sale.order']
        # if self.batch_operation_type in 'confirm':
        #     self.batch_sale_order_ids.write({'state': 'sale'})
        # elif self.batch_operation_type in 'cancel':
        #     self.batch_sale_order_ids.write({'state': 'cancel'})
        # elif self.batch_operation_type in 'merge':
        #     self.batch_sale_order_ids.write({'state': 'cancel'})
        #     self.env['sale.order'].create({'partner_id': self.batch_customer_id.id,
        #                                    'order_line': self.batch_sale_order_ids.order_line})

    def cancel(self):
        print("CCC")
        for rec in self:
            rec.batch_status = 'cancel'

    def set_to_draft(self):
        print("SSS")
        for rec in self:
            rec.batch_status = 'draft'

    # @api.onchange('batch_operation_type', 'batch_responsible_id')
    # def confirm_state(self):
    #     """This is onchange api model."""
    #     if self.batch_operation_type:
    #         if self.batch_operation_type == 'confirm':
    #             domain = [('state', '=', ['draft', 'sent']),
    #                       ('user_id', '=', self.batch_responsible_id.id)]
    #             # return {'domain': {'batch_sale_order_ids': domain}}
    #         elif self.batch_operation_type in 'cancel':
    #             domain = [('state', '=', ['draft', 'sent', 'sale']),
    #                       ('user_id', '=', self.batch_responsible_id.id)]
    #             # return {'domain': {'batch_sale_order_ids': domain}}
    #         elif self.batch_operation_type in 'merge':
    #             domain = [('state', '=', ['draft', 'sent']),
    #                       ('user_id', '=', self.batch_responsible_id.id),
    #                       ('partner_id', '=', self.batch_customer_id.id)]
    #         return {'domain': {'batch_sale_order_ids': domain}}

    # @api.onchange('batch_operation_type', 'batch_responsible_id')
    # @api.model
    # def fields_get(self, allfields=None, attributes=None):
    #     fields = super().fields_get(allfields=allfields, attributes=attributes)
    #     fields['batch_sale_order_ids']['domain'] = "[('state', '=', 'draft'), ('user_id', '=', batch_responsible_id)]"
    #     return fields['batch_sale_order_ids']['domain']
