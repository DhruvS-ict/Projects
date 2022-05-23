# -*- coding: utf-8 -*-
{
    'name': "Contracts Account",

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
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'hr', 'hr_contract'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/contracts_account.xml',
        'views/contracts_account_history.xml',
        'views/contract_individual_detail.xml',
        # 'views/trainees_practical.xml',
    ],
    # 'assets': {'web.assets_frontend': [
    #     'registration_details/static/src/css/registration_details_form.css',
    # ]},
    'application': True,
    "license": "LGPL-3"
}
