# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software.
# See LICENSE file for full copyright & licensing details.
from odoo import models, fields, api


class DeliverySchedule(models.Model):
    """created class to get default sale id and updated."""

    _name = "delivery.schedule"
    _description = "Delivery Schedule"

    schedule_date = fields.Date(string="Schedule Date")
    sale_id = fields.Many2one("sale.order", string="Sale Order")
    temp_sale_id = fields.Many2one("sale.order", string="Sale Order")
    delivery_schedule_ids = fields.One2many(
        "delivery.schedule.line", "delivery_schedule_id", string="Delivery Lines"
    )

    @api.model
    def default_get(self, fields):
        """This function shows the result(res) for the given class."""
        res = super(DeliverySchedule, self).default_get(fields)
        return res


class DeliveryScheduleLines(models.Model):
    """created class."""

    _name = "delivery.schedule.line"
    _description = "Delivery Schedule Lines"

    delivery_schedule_id = fields.Many2one(
        "delivery.schedule", string="Delivery Schedule"
    )
    sale_line_id = fields.Many2one("sale.order.line", string="Order Line")
    quantity = fields.Integer(string="Quantity")
