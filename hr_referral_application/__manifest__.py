# -*- coding: utf-8 -*-
{
    'name': "hr referral application",

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
    'depends': ['base', 'hr', 'hr_recruitment'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/hr_referral_application.xml',
        'views/referral_program_form.xml',
        'views/res_config_settings.xml',

    ],
    'assets': {'web.assets_frontend': [
        'hr_referral_application/static/src/css/referral_program_form.css',
    ], },
    'application': True,
    "license": "LGPL-3"
}
