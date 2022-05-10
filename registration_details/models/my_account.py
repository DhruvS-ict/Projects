"""This"""

from odoo.http import request
from odoo.addons.portal.controllers import portal


class MyAccount(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        values["abc"] = request.env["rental.management"].search_count([('state', '=', 'waiting')])
        return values



# class CustomerPortal(portal.CustomerPortal):
#
#     def _prepare_home_portal_values(self, counters):
#         values = super()._prepare_home_portal_values(counters)
#         values["abc"] = request.env["rental.management"].search_count([('state', '=','waiting')])
#         # partner = request.env.user.partner_id
#         #
#         # SaleOrder = request.env['sale.order']
#         # if 'quotation_count' in counters:
#         #     values['quotation_count'] = SaleOrder.search_count(self._prepare_quotations_domain(partner)) \
#         #         if SaleOrder.check_access_rights('read', raise_exception=False) else 0
#         # if 'order_count' in counters:
#         #     values['order_count'] = SaleOrder.search_count(self._prepare_orders_domain(partner)) \
#         #         if SaleOrder.check_access_rights('read', raise_exception=False) else 0
#
#         return values






