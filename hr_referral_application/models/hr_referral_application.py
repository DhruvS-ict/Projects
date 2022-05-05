"""This"""
from odoo import models, fields, api
from datetime import date


class HrReferralApplication(models.Model):
    """This class is for fields & orm methods."""
    _name = 'hr.referral.application'
    _description = "Created this module."

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    referral_name_id = fields.Many2one('hr.employee', string="Referral Name")
    degree_id = fields.Many2one('hr.recruitment.degree', string="Degree")
    department_id = fields.Many2one('hr.job', string="Department")
    expected_salary = fields.Float(string="Expected Salary")
    summary = fields.Text(string="Summary")
    expected_joining_date = fields.Date(string="Expected Joining Date")
    stages = fields.Selection([('draft', 'Draft'), ('approved', 'Approved'),
                               ('cancel', 'cancel')], string="Stages")

    def approved_func(self):
        print("AAA")
        for rec in self:
            rec.stages = 'approved'

    def create_application(self):
        print("CCC")






# Create a New Model named 'hr.referral.application' with following fields:
# 1. Name
# 2. Email
# 3. Referral Name - many2one (with hr.employee)
# 4. Degree - many2one (with hr.recruitment.degree)
# 5. Department - many2one (with hr.job)
# 6. Expected Salary
# 7. Summary
# 8. Expected joining Date
# • This Should Contain Following Stages- Draft, Approved, Cancel
# • Add a Button Named Approve. By Clicking this Button the Stage of the Record should be changed
# to 'Approved'.
# • Add a button named Create Application. This button should only be visible in Stage 'Approve'.