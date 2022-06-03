# -*- coding: utf-8 -*-
{
    'name': "Controller",

    'summary': """
        This Module display contacts in website""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Custom',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'contacts'],

    'assets': {
        'web.assets_frontend': [
            # 'controller/controller/static/src/js/portal.js',
            'controller/controller/static/src/css/portal.css',
        ],

        'web.assets_common': [
            # 'controller/controller/static/src/js/portal.js',
        ],
    },

    # always loaded
    'data': [
        'views/controller.xml',
        'views/contact_form.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

    # only loaded in demonstration mode
    'license': 'LGPL-3',
}
