# -*- coding: utf-8 -*-
{
    'name': "dhruv_2_6_22",

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
    'depends': ['base', 'contacts', 'website', 'sale_management', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/batch_sale_workflow_data.xml',
        'views/contact_creation.xml',
        'views/batch_sale_workflow.xml',
    ],
    'assets': {'web.assets_frontend': [
        'dhruv_2_6_22/static/src/contact_creation.css',
    ], },
    'application': True,
    "license": "LGPL-3"
}
