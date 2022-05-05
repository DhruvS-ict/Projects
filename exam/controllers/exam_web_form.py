"""This"""

from odoo import http
from odoo.http import request


class ExamWebForm(http.Controller):
    @http.route('/open_form', type="http", website=True)
    def create_web_form(self, **kw):
        if kw:
            request.env['invoice.lines'].sudo().create(kw)
        return request.render("exam.exam_form_page", {})

    # @http.route('/open_form/detail', type="http", auth="user", website=True)
    # def form_record(self, **kw):
    #     request.env['invoice.lines'].sudo().create(kw)
    #     details = request.env['invoice.lines'].sudo().search([])
    #     return request.render("exam.record_detail_page", {'key': details})
