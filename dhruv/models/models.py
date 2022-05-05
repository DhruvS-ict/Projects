# -*- coding: utf-8 -*-

from odoo import models, fields, api, time
from datetime import datetime

class dhruv(models.Model):
    _name = 'dhruv.dhruv'
    _description = 'dhruv.dhruv'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    today = fields.Date()
    # tarikh = fields.Date(string='Date', default=datetime.today())
    age = fields.Integer(string="Age")
    male = fields.Boolean()
    active = fields.Boolean(string="Active", default=True)
    # mod_ids = fields.One2many()


@api.depends('value')
def _value_pc(self):
    for record in self:
        record.value2 = float(record.value) / 100
