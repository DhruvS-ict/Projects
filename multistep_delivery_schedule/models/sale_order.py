# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software.
# See LICENSE file for full copyright & licensing details.
from odoo import models, fields
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    """created class to define wizard action in functions."""

    _inherit = "sale.order"

    multistep_delivery = fields.Boolean(string="Multistep Delivery", default=False)
    delivery_ids = fields.One2many(
        "delivery.schedule", "sale_id", string="Schedule Delivery"
    )
    sale_id = fields.Many2one("sale.order", string="Sale Order")

    def activate_multistep_delivery(self):
        """This function redirect to form view of given model."""
        self.write({"multistep_delivery": True})
        return {
            "name": "Delivery Schedule",
            "view_mode": "form",
            "res_model": "manage.delivery.schedule.wizard",
            "view_id": self.env.ref(
                "multistep_delivery_schedule.delivery_schedule_wizard_form"
            ).id,
            "type": "ir.actions.act_window",
            "target": "new",
            "context": {"default_sale_id": self.id},
        }

    def deactivate_multistep_delivery(self):
        """This function updates multistep delivery."""
        self.write({"multistep_delivery": False})

    def update_multistep_delivery(self):
        """This function redirect to form view of given model."""
        return {
            "name": "Update Delivery Schedule",
            "view_mode": "form",
            "res_model": "manage.delivery.schedule.wizard",
            "view_id": self.env.ref(
                "multistep_delivery_schedule.delivery_schedule_wizard_form"
            ).id,
            "type": "ir.actions.act_window",
            "target": "new",
            "context": {"default_sale_id": self.id},
        }

    def action_confirm(self):
        """
        This function sumup the quantity for respected product and raise error on
        checking conditions.
        """
        if self.multistep_delivery:
            for order_line in self.order_line:
                total_qty = sum(
                    line.quantity
                    for line in self.delivery_ids.delivery_schedule_ids.filtered(
                        lambda order: order.sale_line_id == order_line
                    )
                )
                if not total_qty == order_line.product_uom_qty:
                    raise ValidationError(
                        "Please check the quantity of %s to be delivered."
                        % order_line.display_name
                    )
        return super(SaleOrder, self).action_confirm()
