"""This"""
from odoo import models, fields, api


class BatchSaleWorkflowSaleOrder(models.Model):
    """This class is for fields & orm methods."""
    _inherit = 'sale.order'
    _description = "Sale Order"

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        context = self._context or {}
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~context: ", context)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~context: ", context.get('batch_operation_type'))
        if context.get('batch_operation_type'):
            if context.get('batch_operation_type') == 'confirm':
                args = [('state', '=', ['draft', 'sent']),
                        ('user_id', '=', context.get('batch_responsible_id').id)]

        return super(BatchSaleWorkflowSaleOrder, self)._search(args, offset, limit, order, count=count, access_rights_uid=access_rights_uid)
