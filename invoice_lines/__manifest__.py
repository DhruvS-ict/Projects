# -*- coding: utf-8 -*-

{
    'name': "Invoice Lines",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'contacts', 'hr', 'account', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/account_move.xml',
        'views/account_move_line.xml',
        'views/invoice_lines.xml',
        'views/res_config_setting.xml',
        'views/res_partner.xml',
        'views/res_partner_controllers.xml',
        'views/website_form.xml',
        'wizard/invoice_wizard.xml',
        'reports/report_action.xml',
        'reports/main_sub_template.xml',
        'reports/paper_format.xml',
    ],
    "license": "LGPL-3"
}
