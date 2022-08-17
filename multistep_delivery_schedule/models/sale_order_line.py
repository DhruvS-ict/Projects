# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software.
# See LICENSE file for full copyright & licensing details.
"""import models, fields and api from odoo"""
from odoo import models, fields, api
from datetime import timedelta


class SaleOrderLine(models.Model):
    """created class to define wizard action in functions."""
    _inherit = "sale.order.line"

    def _action_launch_stock_rule(self):
        if self.order_id.multistep_delivery:

            # to create procurement group or update
            group_id = self.order_id.procurement_group_id
            if not group_id:
                group_id = self.env['procurement.group'].create({
                    'name': self.order_id.name,
                    'move_type': self.order_id.picking_policy,
                    'sale_id': self.order_id.id,
                    'partner_id': self.order_id.partner_shipping_id.id,
                })
                self.order_id.procurement_group_id = group_id
            else:
                updated_vals = {}
                if group_id.partner_id != self.order_id.partner_shipping_id:
                    updated_vals.update(
                        {'partner_id': self.order_id.partner_shipping_id.id})
                if group_id.move_type != self.order_id.picking_policy:
                    updated_vals.update({'move_type': self.order_id.picking_policy})
                if updated_vals:
                    group_id.write(updated_vals)
            for delivery in self.order_id.delivery_ids:
                procurements = []
                for line in delivery.delivery_schedule_ids:
                    values = {
                        'group_id': group_id,
                        'sale_line_id': line.sale_line_id.id,
                        'date_planned': delivery.schedule_date,
                        'date_deadline': delivery.schedule_date,
                        'route_ids': line.sale_line_id.route_id,
                        'warehouse_id': line.sale_line_id.order_id.warehouse_id or False,
                        'partner_id': self.order_id.partner_shipping_id.id,
                        'product_description_variants': line.sale_line_id._get_sale_order_line_multiline_description_variants(),
                        'company_id': self.order_id.company_id,
                        'product_packaging_id': line.sale_line_id.product_packaging_id,
                    }
                    product_qty = line.quantity

                    line_uom = line.sale_line_id.product_uom
                    quant_uom = line.sale_line_id.product_id.uom_id
                    product_qty, procurement_uom = line_uom._adjust_uom_quantities(
                        product_qty, quant_uom)
                    procurements.append(self.env['procurement.group'].Procurement(
                        line.sale_line_id.product_id, product_qty, procurement_uom,
                        self.order_id.partner_shipping_id.property_stock_customer,
                        line.sale_line_id.name, self.order_id.name,
                        self.order_id.company_id,
                        values))
                if procurements:
                    print("\n\nprocurements------",procurements)
                    self.env['procurement.group'].run(procurements)

            # picking_type = self.env["stock.picking.type"].search(
            #     [
            #         ("company_id", "=", self.company_id.id),
            #         ("code", "=", 'outgoing'),
            #         # ("code", "in", ['|', ('outgoing'), ('incoming'), ('internal')])
            #     ]
            # )
            # for line in self.order_id.delivery_ids:
            #     values = {
            #         "partner_id": self.order_id.partner_shipping_id.id,
            #         "picking_type_id": picking_type.id,
            #         "origin": self.order_id.name,
            #         "owner_id": self.order_id.partner_id.id,
            #         "location_id": picking_type.default_location_src_id.id,
            #         "location_dest_id": picking_type.default_location_dest_id.id,
            #         # "group_id": self.order_id.procurement_group_id.id,
            #     }
            #
            #     receipt = self.env["stock.picking"].create(values)
            #     receipt.write(
            #         {
            #             "move_ids_without_package": [
            #                 (
            #                     0,
            #                     0,
            #                     {
            #                         "name": line.sale_line_id.product_id.name,
            #                         "product_id": line.sale_line_id.product_id.id,
            #                         "product_uom": line.sale_line_id.product_id.uom_id.id,
            #                         "product_uom_qty": line.quantity,
            #                         "location_id": receipt.location_id.id,
            #                         "location_dest_id": receipt.location_dest_id.id,
            #                         "group_id": self.order_id.procurement_group_id.id,
            #                     },
            #                 )
            #                 for line in line.delivery_schedule_ids
            #             ],
            #         }
            #     )
            #     print("\n~~~~~~~group_id ", receipt.group_id, "\n")
            #     receipt.action_confirm()
        else:
            return super(SaleOrderLine, self)._action_launch_stock_rule()