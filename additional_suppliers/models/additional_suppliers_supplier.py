# -*- coding: utf-8 -*-

from odoo import models, fields


class AdditionalSupplier(models.Model):
    _name = 'additional_suppliers.supplier'
    _description = 'additional supplier'

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    admission_date = fields.Datetime('Admission Date', required=True)
    currency_id = fields.Many2one('res.currency', 'Currency', required=True,
                                  default=lambda self: self.env.company.currency_id.id)
    purchase_amount = fields.Monetary(string='Purchase Amount', required=True, default=0.00, copy=False)
    expense_account_id = fields.Many2one('account.account', string='Expense Account',
                                         domain=[('user_type_id', '=', 'expenses')])

    state = fields.Selection([
        ('in progress', 'In Progress'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='in progress')
