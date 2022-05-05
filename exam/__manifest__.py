# -*- coding: utf-8 -*-
{
    'name': "Exam",

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
    'depends': ['base', 'sale_management', 'contacts', 'hr', 'website', "invoice_lines"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/res_wizard.xml',
        'views/css_form.xml',
        'views/exam.xml',
        'views/exam_web_form.xml',
        'views/invoice_line_form.xml',
        'views/res_config_setting.xml',
        'views/res_partner.xml',
        # 'views/res_action.xml',

    ],
    'assets': {'web.assets_frontend': [
            'exam/static/src/css/form.css',
        ], },
    "license": "LGPL-3"
}
