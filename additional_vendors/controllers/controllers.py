# -*- coding: utf-8 -*-
# from odoo import http


# class AdditionalVendors(http.Controller):
#     @http.route('/additional_vendors/additional_vendors/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/additional_vendors/additional_vendors/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('additional_vendors.listing', {
#             'root': '/additional_vendors/additional_vendors',
#             'objects': http.request.env['additional_vendors.additional_vendors'].search([]),
#         })

#     @http.route('/additional_vendors/additional_vendors/objects/<model("additional_vendors.additional_vendors"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('additional_vendors.object', {
#             'object': obj
#         })
