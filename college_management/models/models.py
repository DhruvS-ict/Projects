"""This"""
from odoo import models, fields


class CollegeManagement(models.Model):
    """This class is for fields & orm methods."""
    _name = 'college_management.college_management'
    _description = 'college_management.college_management'
    # _inherit = 'mail.thread','mail.activity.mixin'
    """"""
    name = fields.Char()
    phone_no = fields.Char(string="Phone Number")
    value = fields.Integer()
    """"""
    value2 = fields.Selection([('bad', 'Bad'), ('average', 'Average'),
                               ('good', 'Good'), ('better', 'Better'),
                               ('best', 'Best'), ('pro', 'Pro')],
                              string="value2")
    """"""
    description = fields.Text()
    # x_signature = fields.Char(string="Signature")
    """"""
    status = fields.Selection([('draft', 'Draft'), ('paid', 'Paid'),
                               ('offer', 'Offer'), ('sent', 'Sent')],
                              string="status")
    """"""
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('other', 'Other')], string="Gender")
    # task = fields.Selection([('done','Done'),('pending','Pending')],
    # string="task",default="pending")
    # g_num = fields.Integer(compute="g_num")
    """"""
    interested = fields.Boolean(string="interested")
    """"""
    cus_one_to_many = fields.One2many('college.cus', 'management_id',
                                      string="cus_one_to_many")
    """"""
    lang_id = fields.Many2one('res.partner', string="lang_id")
    """"""
    cllg_faculty = fields.Many2many('res.partner', string="cllg_faculty")
    """"""
    # call_num = fields.Char('res.partner', string="call_num")
    cus_image = fields.Binary(string="cus_image")
    """"""
    client_otm = fields.One2many('college.client', 'address_id',
                                 string="client_otm")

    purchase_id = fields.Many2one('purchase.order')

    # _sql_constraints = [
    #     ('name_uniq', 'unique (name)', "This name already exists !
    #     Please enter unique nam  Kavishhh"),]

    def object_button(self):
        """This function is created for object button."""
        return self

    def current_clients(self):
        """This function is created for current button."""
        return self

    def create_orm(self):
        """This function is created for create button."""
        vals = [{'name': 'client_1', 'value': '11', 'status': 'draft',
                 'interested': False, 'gender': 'male'},
                {'name': 'client_2', 'value': '12', 'status': 'sent',
                 'interested': True, 'gender': 'female'},
                {'name': 'client_3', 'value': '13', 'status': 'paid',
                 'interested': True, 'gender': 'male'},
                {'name': 'client_4', 'value': '14', 'status': 'offer',
                 'interested': False, 'gender': 'female'}]
        self.env['college_management.college_management'].create(vals)

    def write_orm(self):
        """This function is created for write button."""
        self.write({'gender': 'other', "name": "xyz"})
        return self

    def unlink_orm(self):
        """This function is created for unlink button."""
        record = self.env['college_management.college_management'].browse(109)
        record.unlink()
        return self


class CollegeManagementCus(models.Model):
    """This class is created for one to many field."""
    _name = 'college.cus'
    _description = 'college.cus'
    cus_id = fields.Many2one('res.partner', string="otm_id")
    n_name = fields.Char(string="Naming")
    management_id = fields.Many2one('college_management.college_management',
                                    string="management_id")

    def fun1(self):
        """This function is created for tp."""
        return self

    def fun2(self):
        """This function is created for tp."""
        return self


class CollegeManagementClient(models.Model):
    """This class is created for one to many field."""
    _name = 'college.client'
    _description = 'college.client'
    address_id = fields.Many2one('college_management.college_management',
                                 string="address_id")

    def func1(self):
        """This function is created for tp."""
        return self

    def func2(self):
        """This function is created for tp."""
        return self
