{
    'name': "dhruv june",

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
    'depends': ['base', 'sale_management', 'account'],

    # always loaded
    'data': [
        'views/account_move_line.xml',
        'views/product_product.xml',
        'views/sale_order.xml',
        'views/sale_order_line.xml',
    ],
    'application': True,
    "license": "LGPL-3"
}
# -*- coding: utf-8 -*-
