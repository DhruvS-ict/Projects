"""This"""
from datetime import datetime
from odoo import models, fields, api


# from odoo.exceptions import ValidationError


class SmartView(models.Model):
    """This class is for fields & orm methods."""
    _name = 'smart.view'
    # _inherit = 'mail.thread','mail.activity.mixin'
    _description = "Created this module to display Smart button inside sheet in form view mode."
    _rec_name = "age"
    name = fields.Char(string="Name")
    name1 = fields.Char(string="name1")
    # phone_no = fields.Char(string="Phone Number", related="name.phone_no")
    age = fields.Integer(string="Age", tracking=True)
    residential_address = fields.Text(string="Residential Address")
    date = fields.Datetime(string='Date', default=datetime.now())
    mail_id = fields.Char(string="Mail ID")
    dob = fields.Date(string="Date of Birth")
    select = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Select")

    # cus_one_to_many = fields.One2many('smart.cus','management_id',string="cusonetomany",
    #                                   related="name.cus_one_to_many")

    # _sql_constraints = [('raiseerror_uniq', 'unique (name)',
    # "This name is already exists! Please enter unique name"),]

    def submit_button(self):
        """This function is created for submit button."""
        return self

    # def smart_button(self):
    #     """This function is created for smart button."""
    #     return self

    def create_orm(self):
        """This function is created for create button.
        And also return rainbow effect."""
        vals = {'name': 'Raj', 'age': '34', 'residential_address': 'Gujarat', 'create_uid': '3'}
        # self.message_post(body="xyz has created recent record.")
        self.env['smart.view'].create(vals)
        return {
            'effect': {
                'fadeout': 'fast',
                'message': 'Record created successfully',
                'type': 'rainbow_man',
            }
        }

    def write_orm(self):
        """This function is created for write button."""
        self.message_post(body="phone number is updated successfully.")
        self.write({'phone_no': 999999999999999999})
        return self

    def browse_orm(self):
        """This function is created for unlink button."""
        self.env['smart.view'].browse(108)
        return self

    def search_method(self):
        """This function is created for search_method button.
        It will give record id's according to domain(conditions.)"""
        search_rec = self.env['smart.view'].search([('name', '=', 'Kavish'), ('age', '>', '18')])
        print("----------------------------------------search_rec = ", search_rec, "-----------------------------")

    def count(self):
        """This function is created for search-count_method button.
        It will give total count(numbers) of record according to domain(conditions.)"""
        count_rec = (self.env['smart.view'].search_count([('age', '>', '40')]))
        print("-------------------------------------------count_rec = ", count_rec, "-------------------------------")

    @api.model
    def create(self, vals):
        """This function is created for calling Super."""
        res = super(SmartView, self).create(vals)
        if vals.get('select') == 'male':
            res['name'] = "Mr." + res['name']
        elif vals.get('select') == 'female':
            res['name'] = "Mrs." + res['name']
        return res

    @api.model
    def create(self, vals):
        """This function is created for calling Super."""
        res = super(SmartView, self).create(vals)
        res['name1'] = res['name']
        return res

# class CollegeManagementCus(models.Model):
#     """This class is created for one to many field."""
#     _name = 'smart.cus'
#     cus_id = fields.Many2one('res.partner', string="otm_id")
#     n_name = fields.Char(string="Naming")
#     management_id = fields.Many2one('college_management.college_management',
#     string="management_id")

# @api.constrains('age')
# def check_age(self):
#     for rec in self:
#         if rec.age <= 18:
#             raise ValidationError("Sorry your age is not valid.")
#
# @api.constrains('name')
# def check_name(self):
#     for rec in self:
#         if (rec.name).isnumeric:
#             raise ValidationError("This is not a valid name.")
#
# @api.constrains('residential_address')
# def check_name(self):
#     for rec in self:
#         if 'Gujarat' not in rec.residential_address:
#             raise ValidationError("Sorry ! You are outsider from Gujarat.")


# @api.depends('value')
# def _value_pc(self):
#     for record in self:
#         record.value2 = float(record.value) / 100
