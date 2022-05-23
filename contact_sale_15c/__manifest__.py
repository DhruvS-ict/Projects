# -*- coding: utf-8 -*-
{
    'name': 'Contact Sale',

    'version': '15.0.1.0.0',

    'category': 'Sales/Sales',

    'summary': 'Sale orders history for contacts',

    'description': """
        This module contains history records of sale orders for customers.
        """,

    'author': "Virendrasinh Dabhi",
    'website': "http://www.aktivsoftware.com",

    'depends': ['sale_management', 'contacts', 'base'],

    'data': [
        'security/ir.model.access.csv',
        'views/contact_sale_mail.xml',
        'views/contact_sale.xml',
        'views/contact_sale_menu_action.xml',
        'views/contact_button.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
