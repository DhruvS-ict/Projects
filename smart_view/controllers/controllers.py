"""This"""

from odoo import http
from odoo.http import request


class Website(http.Controller):
    @http.route(['/new'], type="http", auth="user", website=True)
    def smart_web(self):
        contact_record = request.env['res.partner'].sudo().search([])
        return request.render("smart_view.new_page", {"record_list": contact_record})

    @http.route(['/new/record/<model("res.partner"):customer>'], type="http", auth="user", website=True)
    def link_web_page(self, customer):
        return request.render("smart_view.contacts_link_record_page", {'custom': customer})
