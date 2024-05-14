# -*- coding: utf-8 -*-
# from odoo import http


# class AdditionalSuppliers(http.Controller):
#     @http.route('/additional_suppliers/additional_suppliers/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/additional_suppliers/additional_suppliers/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('additional_suppliers.listing', {
#             'root': '/additional_suppliers/additional_suppliers',
#             'objects': http.request.env['additional_suppliers.additional_suppliers'].search([]),
#         })

#     @http.route('/additional_suppliers/additional_suppliers/objects/<model("additional_suppliers.additional_suppliers"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('additional_suppliers.object', {
#             'object': obj
#         })
