# -*- coding: utf-8 -*-
{
    'name': "Website Sale Products",

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
    'depends': ['base', 'sale_management', 'website'],

    # always loaded
    'data': [
        'views/website_sale_products_list.xml'
    ],
    # 'assets': {'web.assets_frontend': [
    #     'website_sale_product/static/src/website_sale_products.css',
    # ], },
    "license": "LGPL-3"
}
