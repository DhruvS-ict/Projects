"""This"""

from odoo import models, fields, api
from datetime import datetime


class RentalManagement(models.Model):
    """This class is for fields & orm methods."""
    _name = 'rental.management'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _description = "Created this module."

    name = fields.Char(string="Name", required=False, tracking=True)
    rental_type_id = fields.Many2one('rental.type', string="Rental Type", required=False)
    start_date = fields.Datetime(string="Start Date", default=datetime.now())
    end_date = fields.Datetime(string="End Date", default=datetime.now())
    rental_product_id = fields.Many2one('product.template', string="Rental Product",
                                        domain="[('rental_type','=',rental_type_id)]")
    price = fields.Float(string="Price", related="rental_product_id.list_price", store=True)
    state = fields.Selection([('draft', 'Draft'), ('waiting', 'Waiting'),
                              ('approve', 'Approve'), ('cancel', 'Cancel')],
                             string="State")
    dob_id = fields.Many2one('rental.management', string="Name & Date")
    dob_ids = fields.Many2one('rental.management', string="Name & Date")
    first_amount = fields.Integer(string="First Amount")
    last_amount = fields.Integer(string="Last Amount")
    total_amount = fields.Integer(string="Total Amount", compute="_compute_set_total_amount")
    email = fields.Char(string="Email")
    rental_image = fields.Binary(string="Image")
    rent_ids = fields.One2many('rent.one','management_id',string="Rents")
    # purchase_id = fields.Many2one('purchase.order')

    _sql_constraints = [('raiseerror_uniq', 'unique (name)',
                         "This name is already exists! Please enter unique name"), ]

    def read_record(self):
        """This function is created for search_method button.
        It will give record id's according to domain(conditions.)"""
        rec = self.env['res.partner'].search([])
        print("----------------------------------------read Method = ", rec, "-----------------------------")
        return {
            'effect': {
                'fadeout': 'fast',
                'message': 'Record read successfully',
                'type': 'rainbow_man',
            }
        }

    def searchread_method(self):
        """This function is created for search_read method button.
        It will do a search & return a list of dict."""
        rec = self.env['res.partner'].search_read([('name', '!=', False)], ['name'])
        for res in rec:
            print("----------------------------------------search_read Method = ", res, "-----------------------------")
        return {
            'effect': {
                'fadeout': 'fast',
                'message': 'Record searched and read successfully',
                'type': 'rainbow_man',
            }
        }

    # def create_rent_one(self):
    #     """This function is created for create button.
    #             And also return rainbow effect."""
    #     self.create({'name':"dhruv",'rent_ids':[(0,0,{'rent_client':99999})],'rent_payment_id':"1"})







    def browsemethod(self):
        """This is Browse method."""
        res = self.env['rental.management'].browse([1, 2])
        print("--------------------------------------------------browse Method = ", res,
              "-------------------------------")
        return {
            'effect': {
                'fadeout': 'fast',
                'message': 'Record browsed successfully',
                'type': 'rainbow_man',
            }
        }

    # @api.model
    # def default_get(self, fields):
    #     rec = super(RentalManagement, self).default_get(fields)
    #     rec['name'] = 'Kavish'
    #     rec['customer_id'] = 3
    #     return rec

    @api.depends('first_amount', 'last_amount')
    def _compute_set_total_amount(self):
        """This is api depends in which total_amount fields changes,
        depends on other two fields."""
        for rec in self:
            print("----------------------------------------records = ", rec)
            rec.total_amount = rec.first_amount * rec.last_amount

    # @api.depends('name')
    # def _compute_set_email(self):
    #     """This is api depends in which total_amount fields changes,
    #     depends on other two fields."""
    #     for rec in self:
    #         print("----------------------------------------records = ", rec)
    #         rec.email = rec.name + "@gmail.com"

    # def default_get(self, fields):
    #     """This is default get function."""
    #     rec = super(RentalManagement, self).default_get(fields)
    #     print("-------------------------------------------------------", rec)
    #     rec['name'] = 'Kavish'
    #     rec['customer_id'] = 5
        # return rec




class RentalType(models.Model):
    """This class is for fields & orm methods."""
    _name = 'rental.type'
    _description = "Created this module."

    name = fields.Char(string="Name")
    code = fields.Char(string="Customer")
    description = fields.Char(string="Description")


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_checked = fields.Boolean(string="Check", config_parameter='rental_management.active')
    description = fields.Char(config_parameter='rental_management.description')
    seting_id = fields.Many2one('res.partner', config_parameter='rental_management.seting_id', string="Settings")

    # is_active = fields.Boolean(string='Active', config_parameter='rental_management.active')

    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()
    #
    #     res['is_checked'] = self.env['ir.config_parameter'].get_param(
    #         'rental_management.is_checked')
    #     res['test_char'] = self.env['ir.config_parameter'].get_param(
    #         'test_char')
    #
    #     return res
    #
    # @api.model
    # def set_values(self):
    #     self.env['ir.config_parameter'].set_param(
    #         'rental_management.is_checked', self.is_checked)
    #     self.env['ir.config_parameter'].set_param(
    #         'test_char', self.test_char)
    #     super(ResConfigSettings, self).set_values()

    @api.onchange('is_checked')
    def set_field(self):
        """This is onchange api model."""
        for rec in self:
            if not rec.is_checked:
                rec.description = False
                rec.seting_id = False






class RentOneToMany(models.Model):
    """This class is created for one to many field."""
    _name = 'rent.one'
    rent_payment_id = fields.Many2one('res.partner', string="Rent Payment")
    rent_client = fields.Char(string="Rent Client")
    management_id = fields.Many2one('rental.management', string="Rental Management ID")



