# -*- coding: utf-8 -*-
{
    'name': "Additional suppliers",

    'summary': """
        Adds a new concept called “Additional Suppliers”
        """,

    'description': """
        Odoo technical task:
        Adds a new concept called “Additional Suppliers” with fields:
        Partner,
        Date,
        Purchase amount,
        expense account,
        State
    """,

    'author': "Rafael Enrique Báez Guevara",
    'website': "https://www.linkedin.com/in/rafabcuba/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Purchases',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'purchase'
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}