from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    additional_vendors_ids = fields.Many2many('additional_vendors.vendor', string='Additional vendors',
                                              domain=[('state', '=', 'confirmed')])
