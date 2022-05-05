"""This"""

from odoo import http
from odoo.http import request


class Website(http.Controller):
    @http.route(['/contact'], type="http", auth="user", website=True)
    def smart_web(self):
        contact_record = request.env['res.partner'].sudo().search([])
        return request.render("invoice_lines.main_page", {"record_list": contact_record})

    @http.route(['/contact/record/<model("res.partner"):customer>'], type="http", auth="user", website=True)
    def link_web_page(self, customer):
        return request.render("invoice_lines.contacts_link_record_page", {'custom': customer})

    # def createO(self, vals):
    #     random = ''
    #     vals.update({'random': random})
    #     res = super(Website, self).createO(vals)
    #     # res.random = random = res.write({'random': random})
    #     return  res
    # active_model = self._contyext.get('active_model')
    # active_id = self._contyext.get('active_id')
    # self.env[active_model].browse(active_id).message_post("Messsage")