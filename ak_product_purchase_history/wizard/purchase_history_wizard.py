# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software.
# See LICENSE file for full copyright & licensing details.
"""import models, fields and api from odoo"""
from odoo import models, fields, api


class ProductPurchaseHistoryWizard(models.TransientModel):
    """created wizard to view wizard having purchase history for product."""

    _name = "product.purchase.history.wizard"
    _description = "product purchase history wizard"

    total_orders = fields.Integer(
        string="Total Orders", compute="_compute_product_purchase_order"
    )
    product_id = fields.Many2one("product.product", string="Product")
    datetime_start = fields.Date()
    datetime_end = fields.Date()
    supplier_id = fields.Many2one("res.partner", string="Supplier")
    purchase_history_ids = fields.One2many(
        "product.purchase.history",
        "product_purchase_history_id",
        string="Product Purchase History",
    )

    @api.depends("product_id", "datetime_end", "datetime_start", "supplier_id")
    def _compute_product_purchase_order(self):
        """
        This function first deletes and then creates the records
        accord to supplier and daterange for a specific product.
        """

        domain = []
        if self.product_id:
            domain.append(
                ("order_line.product_id.id", "=", self.product_id.id)
            )
        if self.supplier_id:
            domain.append(("partner_id.id", "=", self.supplier_id.id))
        if self.datetime_start:
            domain.append(("date_planned", ">=", self.datetime_start))
        if self.datetime_end:
            domain.append(("date_planned", "<=", self.datetime_end))
        filter_history_search = self.env["purchase.order"].search(domain)
        self.update({"total_orders": len(filter_history_search)})
        updated_history_line = [(5, 0, 0)] + [
            (
                0,
                0,
                {
                    "purchase_id": record.id,
                    "partner_id": record.partner_id.id,
                    "history_datetime": record.date_planned,
                },
            )
            for record in filter_history_search
        ]
        self.update({"purchase_history_ids": updated_history_line})


class ProductPurchaseHistoryLine(models.TransientModel):
    """created product purchase history line fields."""

    _name = "product.purchase.history"
    _description = "Product Purchase History"

    product_purchase_history_id = fields.Many2one(
        "product.purchase.history.wizard"
    )
    purchase_id = fields.Many2one(
        "purchase.order", string="Purchase order", readonly=True
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Supplier",
        related="purchase_id.partner_id",
        readonly=True,
    )
    history_datetime = fields.Datetime(
        string="Datetime", related="purchase_id.date_planned", readonly=True
    )
