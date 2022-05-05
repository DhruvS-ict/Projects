"""This"""

from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route('/create_record', type="http", auth="user", website=True)
    def smart_web(self):
        return request.render("invoice_lines.form_page_record", {})

    @http.route('/create_form/list', type="http", auth="user", website=True)
    def link_web_page(self, **kw):
        request.env['second.exam'].sudo().create(kw)
