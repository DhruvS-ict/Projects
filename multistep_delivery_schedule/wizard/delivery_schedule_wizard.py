# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software.
# See LICENSE file for full copyright & licensing details.
"""import models, fields and api from odoo"""
from odoo import models, fields, api, _
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT


class ManageDeliveryScheduleWizard(models.TransientModel):
    """
    created class to create delivery lines in sale order and default
    get lines in delivery schedule lines in update wizard.
    """

    _name = "manage.delivery.schedule.wizard"
    _description = "Manage Delivery schedule wizard"

    delivery_schedule_ids = fields.One2many(
        "delivery.schedule.wizard",
        "delivery_schedule_wizard_id",
        string="Delivery Schedule Lines",
    )
    sale_id = fields.Many2one("sale.order", string="Sale Order")

    def delivery_schedule(self):
        """This function creates delivery lines in sale order."""
        sale_env = self.env["sale.order"].search(
            [("id", "=", self._context.get("active_id"))]
        )
        sale_env.update(
            {
                "delivery_ids": [(5, 0, 0)]
                + [
                    (
                        0,
                        0,
                        {
                            "schedule_date": rec.schedule_date,
                            "temp_sale_id": sale_env.id,
                            "delivery_schedule_ids": [
                                (
                                    0,
                                    0,
                                    {
                                        "sale_line_id": line.sale_line_id.id,
                                        "quantity": line.quantity,
                                    },
                                )
                                for line in rec.delivery_schedule_line_ids
                            ],
                        },
                    )
                    for rec in self.delivery_schedule_ids
                ]
            }
        )

    @api.model
    def default_get(self, fields):
        """This function by default sets value of sale_id."""
        res = super(ManageDeliveryScheduleWizard, self).default_get(fields)
        if (
            self.env.context.get("active_id")
            and self.env.context.get("active_model") == "sale.order"
        ):
            order = self.env["sale.order"].browse(self.env.context.get("active_id"))
            if order.exists():
                res.update({"sale_id": order.id})
        return res

    @api.onchange("sale_id")
    def onchange_sale_order(self):
        """This function checks if line is created or not."""
        if self.sale_id:
            self.delivery_schedule_ids = self._get_delivery_schedule_data(self.sale_id)
        else:
            self.delivery_schedule_ids = [(5, 0, 0)]

    def _get_delivery_schedule_data(self, order):
        """This function creates delivery schedule lines inside update wizard."""
        return [
            (
                0,
                0,
                {
                    "schedule_date": (schedule.schedule_date)
                    and schedule.schedule_date.strftime(DATE_FORMAT)
                    or False,
                    "temp_sale_id": order.id,
                    "delivery_schedule_line_ids": [
                        (
                            0,
                            0,
                            {
                                "sale_line_id": line.sale_line_id.id,
                                "quantity": line.quantity,
                            },
                        )
                        for line in schedule.delivery_schedule_ids
                    ],
                },
            )
            for schedule in order.delivery_ids
        ]


class DeliveryScheduleWizard(models.TransientModel):
    """
    created class to set relation to manage delivery schedule wizard model.
    """

    _name = "delivery.schedule.wizard"
    _description = "Delivery schedule wizard"

    schedule_date = fields.Date(string="Schedule Date")
    delivery_schedule_line_ids = fields.One2many(
        "delivery.schedule.wizard.line",
        "delivery_schedule_id",
        string="Schedule Delivery",
    )
    delivery_schedule_wizard_id = fields.Many2one(
        "manage.delivery.schedule.wizard", string="Delivery Schedule Wizard"
    )
    sale_id = fields.Many2one("sale.order", string="Sale Order")
    temp_sale_id = fields.Many2one("sale.order", string="Sale Order")

    @api.model
    def default_get(self, fields):
        """
        This function sets the default value of sale_id.
        """
        res = super(DeliveryScheduleWizard, self).default_get(fields)
        res_id = self._context.get("sale_id", False)
        res_model = self._context.get("active_model", False)
        if res_id and res_model == "sale.order":
            record = self.env[res_model].browse(res_id)
            res.update(
                {
                    "sale_id": record.id, "temp_sale_id": record.id
                }
            )
        return res


class DeliveryScheduleLineWizard(models.TransientModel):
    """
    created class to set relation to delivery schedule wizard model.
    """

    _name = "delivery.schedule.wizard.line"
    _description = "Delivery Schedule Line Wizard"

    delivery_schedule_id = fields.Many2one(
        "delivery.schedule.wizard", string="Delivery Schedule"
    )
    sale_line_id = fields.Many2one("sale.order.line", string="Order Line")
    quantity = fields.Integer(string="Quantity")
