# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software.
# See LICENSE file for full copyright & licensing details.
"""import models, fields and api from odoo"""
from odoo import models, fields, api
from datetime import timedelta


class SaleOrderLine(models.Model):
    """created class to define wizard action in functions."""
    _inherit = "sale.order.line"

    # def _prepare_procurement_group_vals(self):
    #     return {
    #         'name': self.order_id.name,
    #         'move_type': self.order_id.picking_policy,
    #         'sale_id': self.order_id.id,
    #         'partner_id': self.order_id.partner_shipping_id.id,
    #     }
    #
    # def _prepare_procurement_values(self, group_id=False):
    #     """ Prepare specific key for moves or other components that will be created from a stock rule
    #     comming from a sale order line. This method could be override in order to add other custom key that could
    #     be used in move/po creation.
    #     """
    #     values = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
    #     print("\n~~~~~~~values ", values)
    #     self.ensure_one()
    #     print("\n~~~~~~~self.ensure_one ", self.ensure_one)
    #     # Use the delivery date if there is else use date_order and lead time
    #     date_deadline = self.order_id.commitment_date or (
    #                 self.order_id.date_order + timedelta(
    #             days=self.customer_lead or 0.0))
    #     date_planned = self.product_id.scheduled_date
    #     values.update({
    #         'group_id': group_id,
    #         'sale_line_id': self.id,
    #         'date_planned': date_planned,
    #         'date_deadline': date_deadline,
    #         'route_ids': self.route_id,
    #         'warehouse_id': self.order_id.warehouse_id or False,
    #         'partner_id': self.order_id.partner_shipping_id.id,
    #         'product_description_variants': self._get_sale_order_line_multiline_description_variants(),
    #         'company_id': self.order_id.company_id,
    #         'product_packaging_id': self.product_packaging_id,
    #     })
    #     return values

    def _action_launch_stock_rule(self):
        # for order_id in set(order.order_id for order in self):
        #     order = order_id[0]
        #     if order.multistep_delivery:
        #         procurements = []
        #         for delivery_id in order.delivery_ids:
        #             print("\n\n\ndelivery_id-=------------", delivery_id)
        #             group_id = order.procurement_group_id
        #             print("\n~~~~~~~~group_id ", group_id)
        #             if not group_id:
        #                 group_id = self.env['procurement.group'].create(delivery_id._prepare_procurement_group_vals())
        #                 print("\n~~~~~~~group_id ", group_id)
        #                 order.procurement_group_id = group_id
        #             else:
        #                 # In case the procurement group is already created and the order was
        #                 # cancelled, we need to update certain values of the group.
        #                 updated_vals = {}
        #                 print("\n~~~~~~~updated_vals ", updated_vals)
        #                 print("\n~~~~~~~group_id ", group_id)
        #                 print("\n~~~~~~~group_id.partner_id ", group_id.partner_id)
        #                 print("\n~~~~~~~self.order_id.partner_shipping_id ", self.order_id.partner_shipping_id)
        #                 if group_id.partner_id != self.order_id.partner_shipping_id:
        #                     updated_vals.update(
        #                         {'partner_id': self.order_id.partner_shipping_id.id})
        #                 if group_id.move_type != self.order_id.picking_policy:
        #                     updated_vals.update(
        #                         {'move_type': self.order_id.picking_policy})
        #                 if updated_vals:
        #                     group_id.write(updated_vals)
        #
        #             values = delivery_id._prepare_procurement_values(group_id=group_id)
        #             print("\n~~~~~~~values ", values)
        #             product_qty = delivery_id.delivery_schedule_ids.quantity
        #             print("\n~~~~~~~product_qty ", product_qty)

        #             line_uom = line.product_uom
        #             quant_uom = line.product_id.uom_id
        #             product_qty, procurement_uom = line_uom._adjust_uom_quantities(
        #                 product_qty, quant_uom)
        #             procurements.append(self.env['procurement.group'].Procurement(
        #                 line.product_id, product_qty, procurement_uom,
        #                 line.order_id.partner_shipping_id.property_stock_customer,
        #                 line.name, line.order_id.name, line.order_id.company_id,
        #                 values))
        #         if procurements:
        #             self.env['procurement.group'].run(procurements)
        #
        #         # This next block is currently needed only because the scheduler trigger is done by picking confirmation rather than stock.move confirmation
        #         orders = self.mapped('order_id')
        #         for order in orders:
        #             pickings_to_confirm = order.picking_ids.filtered(
        #                 lambda p: p.state not in ['cancel', 'done'])
        #             if pickings_to_confirm:
        #                 # Trigger the Scheduler for Pickings
        #                 pickings_to_confirm.action_confirm()
        #         return True
        if self.order_id.multistep_delivery:
            print("\n~~~~self.order_id.multistep_delivery ",
                  self.order_id.multistep_delivery)
            picking_type = self.env["stock.picking.type"].search(
                [
                    ("company_id", "=", self.company_id.id),
                    ("code", "=", 'outgoing'),
                ]
            )
            print('\n\n\npicking_type', picking_type.default_location_dest_id)
            for line in self.order_id.delivery_ids:
                values = {
                    "partner_id": self.order_id.partner_shipping_id.id,
                    "picking_type_id": picking_type.id,
                    "origin": self.order_id.name,
                    "owner_id": self.order_id.partner_id.id,
                    "location_id": picking_type.default_location_src_id.id,
                    "location_dest_id": picking_type.default_location_dest_id.id,
                }

                receipt = self.env["stock.picking"].create(values)
                print('\n\n\nreceipt', receipt)
                receipt.write(
                    {
                        "move_ids_without_package": [
                            (
                                0,
                                0,
                                {
                                    "name": line.sale_line_id.product_id.name,
                                    "product_id": line.sale_line_id.product_id.id,
                                    "product_uom": line.sale_line_id.product_id.uom_id.id,
                                    "product_uom_qty": line.quantity,
                                    "location_id": receipt.location_id.id,
                                    "location_dest_id": receipt.location_dest_id.id,
                                },
                            )
                            for line in line.delivery_schedule_ids
                        ]
                    }
                )
                receipt.action_confirm()
            # self.env['stock.picking'].create(
            #     {
            #         "location_id": (self.env['stock.location'].search([])).location_id.id,
            #         "scheduled_date": [
            #             (
            #                 0, 0, {
            #                     "schedule_date": schedule.schedule_date
            #                 }
            #             ) for schedule in self.order_id.delivery_ids
            #         ],
            #         "move_ids_without_package": [
            #             (
            #                 0, 0, {
            #                     "product_id": [
            #                         (
            #                             0, 0, {
            #                                 "sale_line_id": product.sale_line_id.id
            #                             }
            #                         ) for product in line.delivery_schedule_ids
            #                     ],
            #                     "product_uom_qty": [
            #                         (
            #                             0, 0, {
            #                                 "quantity": qty.quantity
            #                             }
            #                         ) for qty in line.delivery_schedule_ids
            #                     ]
            #                 }
            #             ) for line in self.order_id.delivery_ids
            #         ]
            #     }
            # )
        else:
            return super(SaleOrderLine, self)._action_launch_stock_rule()
