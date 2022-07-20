# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software.
# See LICENSE file for full copyright & licensing details.

# Author: Aktiv Software.
# mail:   odoo@aktivsoftware.com
# Copyright (C) 2015-Present Aktiv Software PVT. LTD.
# Contributions:
#           Aktiv Software:
#              - Parth Radadia
#              - Dhruv Shah
#              - Harshil Soni
{
    'name': "Product Purchase History",
    'author': "Aktiv Software",
    'website': "https://aktivsoftware.com",
    'summary': """
        View Purchase Product History""",
    'description': """
        Title: Product Purchase History \n 
        Author: Aktiv Software \n 
        mail: odoo@aktivsoftware.com \n 
        Copyright (C) 2015-Present Aktiv Software PVT. LTD. \n 
        Contributions: Aktiv Software
    """,
    "license": "OPL-1",
    'category': 'Purchase/Purchase',
    'version': '15.0.1.0.0',
    'depends': ['base', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/purchase_history_wizard.xml',
        'views/purchase_order.xml',
    ],
    'images': [
        'static/description/banner.jpeg'
    ],
    # 'currency': 'ASK_TO_SAURABH',
    # 'price': ASK_TO_SAURABH,
}
