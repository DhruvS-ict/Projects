# -*- coding: utf-8 -*-
# Part of Odoo, Aktiv Software.
# See LICENSE file for full copyright & licensing details.

# Author: Aktiv Software.
# mail:   odoo@aktivsoftware.com
# Copyright (C) 2015-Present Aktiv Software PVT. LTD.
# Contributions:
#           Aktiv Software:
#              - Parth Radadia
#              - Shahil chauhan
#              -
{
    "name": "Multistep Delivery Schedule",
    "author": "Aktiv Software",
    "website": "https://aktivsoftware.com",
    "summary": """Multistep delivery Schedule""",
    "description": """
        
    """,
    "license": "OPL-1",
    "category": "Sales/Sales",
    "version": "15.0.1.0.0",
    "depends": [
        "base",
        "sale_management",
        "stock"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_order_views.xml",
        "wizard/delivery_schedule_wizard.xml",

    ],
    # "images": ["static/description/banner.jpeg"],
    # "currency": "EUR",
    # "price": 24.42,
    "application": True,
    "auto_install": False,
}
