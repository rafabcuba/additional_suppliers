# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class additional_vendors(models.Model):
#     _name = 'additional_vendors.additional_vendors'
#     _description = 'additional_vendors.additional_vendors'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
