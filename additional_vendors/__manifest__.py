# -*- coding: utf-8 -*-
{
    'name': "Additional vendors",

    'summary': """
        Adds a new concept called “Additional Vendors”
        """,

    'description': """
        Odoo technical task:
        Adds a new concept called “Additional Vendors” with fields:
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
                'purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/additional_vendors_menu.xml',
        'views/additional_vendors_purchase_order_form.xml',
        'report/purchase_order_with_additional_vendors.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
