"""This"""

from odoo import http
from odoo.http import request


class InvoiceLineForm(http.Controller):
    @http.route('/invoice_form', type="http", auth="user", website=True)
    def invoice_form(self, **kw):
        if kw:
            request.env['invoice.lines'].sudo().create(kw)
        return request.render("exam.invoice_exam_form", {})

    @http.route('/invoice_form/records', type="http", auth="user", website=True)
    def invoice_rec(self, **data):
        details = request.env['invoice.lines'].search([])
        return request.render("exam.invoice_form_details", {'invoice_form_details': details})
    