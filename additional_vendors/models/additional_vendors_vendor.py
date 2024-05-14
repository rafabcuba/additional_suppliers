# -*- coding: utf-8 -*-

from odoo import models, fields


class AdditionalVendor(models.Model):
    _name = 'additional_vendors.vendor'
    _description = 'additional vendor'
    _inherit = ['mail.thread']

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    admission_date = fields.Datetime('Admission Date', required=True)
    currency_id = fields.Many2one('res.currency', 'Currency', required=True,
                                  default=lambda self: self.env.company.currency_id.id)
    purchase_amount = fields.Monetary(string='Purchase Amount', required=True, default=0.00, copy=False)
    expense_account_id = fields.Many2one(
        'account.account', string='Expense Account',
        domain=lambda self: [('user_type_id', '=', self.env.ref('account.data_account_type_expenses').id)])

    state = fields.Selection([
        ('in progress', 'In Progress'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='in progress')

    def action_confirm(self):
        self.state = 'confirmed'

    def action_cancel(self):
        self.state = 'cancelled'
