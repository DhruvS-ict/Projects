# -*- coding: utf-8 -*-

from odoo import models, fields, api


class demo_addons(models.Model):
    _name = 'demo_addons.demo_addons'
    _description = 'demo_addons.demo_addons'
    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    number = fields.Integer(readonly=True)
    male = fields.Boolean()
    active = fields.Boolean(string="Activate", default=True)
    file = fields.Binary()




@api.depends('value')
def _value_pc(self):
    for record in self:
        record.value2 = float(record.value) / 100
