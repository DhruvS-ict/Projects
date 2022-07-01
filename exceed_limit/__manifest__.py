{
    'name': "Exceed Limit",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dhruv Shah",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'mail', 'contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/exceed_limit.xml',
        'views/exceed_limit_email.xml',
        'views/res_config_settings.xml',
        'views/res_partner.xml',
    ],
    'application': True,
    "license": "LGPL-3"
}
# -*- coding: utf-8 -*-
