# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software.
# See LICENSE file for full copyright & licensing details.
from odoo import models, fields


class SaleOrderLine(models.Model):
    """created class to define wizard action in functions."""

    _inherit = "sale.order.line"

    def _action_launch_stock_rule(self):
        """
        create group_id if not and updates group_id if it's already created. After
        iteration values and other fields were append to procurements which will finally
        run. This action works if multistep_delivery is True, otherwise super calls.
        """
        if self.order_id.multistep_delivery:
            group_id = self.order_id.procurement_group_id
            if not group_id:
                group_id = self.env["procurement.group"].create(
                    {
                        "name": self.order_id.name,
                        "move_type": self.order_id.picking_policy,
                        "sale_id": self.order_id.id,
                        "partner_id": self.order_id.partner_shipping_id.id,
                    }
                )
                self.order_id.procurement_group_id = group_id
            else:
                updated_vals = {}
                if group_id.partner_id != self.order_id.partner_shipping_id:
                    updated_vals.update(
                        {"partner_id": self.order_id.partner_shipping_id.id}
                    )
                if group_id.move_type != self.order_id.picking_policy:
                    updated_vals.update({"move_type": self.order_id.picking_policy})
                if updated_vals:
                    group_id.write(updated_vals)
            for delivery in self.order_id.delivery_ids:
                procurements = []
                for line in delivery.delivery_schedule_ids:
                    values = {
                        "group_id": group_id,
                        "sale_line_id": line.sale_line_id.id,
                        "date_planned": delivery.schedule_date,
                        "date_deadline": delivery.schedule_date,
                        "route_ids": line.sale_line_id.route_id,
                        "warehouse_id": line.sale_line_id.order_id.warehouse_id
                        or False,
                        "partner_id": self.order_id.partner_shipping_id.id,
                        "product_description_variants": line.sale_line_id.
                        _get_sale_order_line_multiline_description_variants(),
                        "company_id": self.order_id.company_id,
                        "product_packaging_id": line.sale_line_id.product_packaging_id,
                    }
                    product_qty = line.quantity
                    line_uom = line.sale_line_id.product_uom
                    quant_uom = line.sale_line_id.product_id.uom_id
                    product_qty, procurement_uom = line_uom._adjust_uom_quantities(
                        product_qty, quant_uom
                    )
                    procurements.append(
                        self.env["procurement.group"].Procurement(
                            line.sale_line_id.product_id,
                            product_qty,
                            procurement_uom,
                            self.order_id.partner_shipping_id.property_stock_customer,
                            line.sale_line_id.name,
                            self.order_id.name,
                            self.order_id.company_id,
                            values,
                        )
                    )
                if procurements:
                    self.env["procurement.group"].run(procurements)
        else:
            return super(SaleOrderLine, self)._action_launch_stock_rule()
