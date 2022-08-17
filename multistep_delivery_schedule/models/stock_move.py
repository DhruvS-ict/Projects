# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software.
# See LICENSE file for full copyright & licensing details.
"""import models, fields and api from odoo"""
from odoo import models, fields, api
from itertools import groupby
from odoo.tools.float_utils import float_compare


class StockMove(models.Model):
    """created class to define wizard action in functions."""
    _inherit = "stock.move"

    def _assign_picking(self):
        """ Try to assign the moves to an existing picking that has not been
        reserved yet and has the same procurement group, locations and picking
        type (moves should already have them identical). Otherwise, create a new
        picking to assign them to. """
        if self.group_id.sale_id.multistep_delivery:
            print("\n\n\n====", self.group_id.sale_id.multistep_delivery)
            Picking = self.env['stock.picking']
            grouped_moves = groupby(
                sorted(self, key=lambda m: [f.id for f in m._key_assign_picking()]),
                key=lambda m: [m._key_assign_picking()])
            for group, moves in grouped_moves:
                moves = self.env['stock.move'].concat(*list(moves))
                new_picking = False
                picking = moves[0]._search_picking_for_assignation()
                moves = moves.filtered(
                    lambda m: float_compare(m.product_uom_qty, 0.0,
                                            precision_rounding=m.product_uom.rounding) >= 0)
                if not moves:
                    continue
                new_picking = True
                picking = Picking.create(moves._get_new_picking_values())

                moves.write({'picking_id': picking.id})
                moves._assign_picking_post_process(new=new_picking)
            return True
        else:
            return super(StockMove, self)._assign_picking()
