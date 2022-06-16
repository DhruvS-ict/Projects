"""This"""
from odoo import models, fields, api


class BatchSaleWorkflowSaleOrder(models.Model):
    """Inherit sale_order."""
    _inherit = 'sale.order'
    _description = "Sale Order"

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        """Here context is used to get field values from other model object. And values(values filled
        after running the program inside field) of fields will get inside args."""
        context = self._context or {}
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~context: ", context)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~context: ", context.get('batch_operation_type'))
        if context.get('batch_operation_type'):
            if context.get('batch_operation_type') == 'confirm':
                args = [('state', '=', ['draft', 'sent']),
                        ('user_id', '=', context.get('batch_responsible_id'))]
            elif context.get('batch_operation_type') == 'cancel':
                args = [('state', '=', ['draft', 'sent', 'sale']),
                          ('user_id', '=', context.get('batch_responsible_id'))]
            elif context.get('batch_operation_type') == 'merge':
                args = [('state', '=', ['draft', 'sent']),
                        ('user_id', '=', context.get('batch_responsible_id')),
                        ('partner_id', '=', context.get('batch_customer_id'))]
        return super(BatchSaleWorkflowSaleOrder, self)._search(args, offset, limit, order, count=count, access_rights_uid=access_rights_uid)
