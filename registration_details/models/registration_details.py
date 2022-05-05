"""This"""
from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta
import time


class RegistrationDetails(models.Model):
    """This class is for fields & orm methods."""
    _name = 'registration.details'
    _description = "Created this module."

    registration_id = fields.Many2one('res.partner', string="Name", required=True)
    mail = fields.Char(string="Email")
    mobile_number = fields.Char(string="Mobile Number")
    country = fields.Many2one('res.country', string="Country")
    state = fields.Many2one('res.country.state', string="State")
    educational_qualification = fields.One2many('registration.one', 'detail_id',
                                                string="Educational Qualification")
    stage = fields.Selection([('draft', 'Draft'), ('approved', 'Approved'),
                              ('cancel', 'cancel')], string="Stage")

    def approved_func(self):
        print("AAA")
        for rec in self:
            rec.stage = 'approved'

    def cancel_func(self):
        print("AAA")
        for rec in self:
            rec.stage = 'cancel'

    def reset_func(self):
        print("AAA")
        for rec in self:
            rec.stage = 'draft'


class RegistrationOneToMany(models.Model):
    """This class is created for one to many field."""
    _name = 'registration.one'

    detail_id = fields.Many2one('registration.details')
    degree = fields.Many2one('hr.recruitment.degree', string="Degree")
    institute_name = fields.Char(string="Institute Name")
    pass_out_year = fields.Selection([('2015', '2015'), ('2016', '2016'),
                                      ('2017', '2017'), ('2018', '2018'),
                                      ('2019', '2019'), ('2020', '2020'),
                                      ('2021', '2021'), ('2022', '2022'),
                                      ('2023', '2023')], string="Pass Out Year")
    calculate_difference = fields.Integer(string="Calculate Difference", compute="_compute_calculate_difference")


    @api.depends('pass_out_year')
    def _compute_calculate_difference(self):
        for rec in self:
            if rec.pass_out_year:
                year = date.today().year
                rec.calculate_difference = year - int(rec.pass_out_year)
            else:
                rec.calculate_difference = 0
    #
    #


# Backend
# - Create a New Menu Named "Registration Details".
# - Create a New Model "student.information" which will have the Following Fields
# 	1) Name
# 	2) Email
# 	3) Mobile Number
# 	4) Country
# 	5) State
# 	6) Educational Qualification (One2many field with relation student.information)
# 		a) degree
# 		b) Institute Name
# 		c) Pass out Year
# 		d) "Calculate Difference of Year" - This will Calculate the Difference between the Present Year and the Passout Year.
#     7) Stage ( Add Draft, Approved and Cancel )
#
# - Create a Group Named "Educational Manager".
# - Add 'Approve' button and on click of it Stage should change to "Approve"
# - Add 'Cancel' button and on click of it Stage should change to "Cancel"
# - Add 'Reset' button(Visible in Cancel State) and on click of it stage should change to "Draft"
# - Only Users with "Educational Manager" Access Rights will have Access of Approving the Registration Form.