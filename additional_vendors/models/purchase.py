from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    additional_vendors_ids = fields.Many2many('additional_vendors.vendor', string='Additional vendors',
                                              domain=[('state', '=', 'confirmed')])

    additional_vendors_recorded = fields.Boolean(string='Recorded', default=False)

    def action_record(self):
        journal = self.env['account.journal'].sudo().search([('company_id', '=', self.company_id.id),
                                                             ('type', '=', 'general')])[0]

        payable_account_id = self.env['account.account'].search([
            ('company_id', '=', self.company_id.id),
            ('internal_type', '=', 'payable'),
        ], limit=1).id

        move_lines = []
        credit_account_id = payable_account_id

        for vendor in self.additional_vendors_ids:
            debit_account_id = vendor.expense_account_id.id

            move_lines.append((0, 0, {
                'account_id': debit_account_id,
                'debit': self.amount_total,
            }))

            move_lines.append((0, 0, {
                'account_id': credit_account_id,
                'credit': self.amount_total,
            }))

        new_entry = self.env['account.move'].create({
            'journal_id': journal.id,
            'date': fields.Date.today(),
            'ref': 'additional vendor entry',
            'line_ids': move_lines,
        })

        new_entry.action_post()
        self.additional_vendors_recorded = True

