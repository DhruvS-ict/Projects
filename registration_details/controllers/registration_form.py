"""This"""

from odoo import http
from odoo.http import request


class ReferralProgramForm(http.Controller):
    @http.route('/registration_web_form', type="http", auth="user", website=True)
    def create_web_form(self, **kw):
        print ("innnnnnnnnnnnn")
        if kw:
            request.env['registration.details'].sudo().create(kw)
            return request.render("registration_details.registration_thanks_page", {})
        registration_name = request.env['res.partner'].search([])
        print("_______________________________", registration_name)
        country_rec = request.env['res.country'].search([])
        state_part = request.env['res.country.state'].search([])
        return request.render("registration_details.registration_details_form",
                              {'registration_name_id': registration_name,
                               'country_details': country_rec,
                               'state_records': state_part})

    # @http.route('/registration_thankyou', type="http", auth="user", website=True)
    # def redirect_thankyou_page(self):
    #     return request.render("registration_details.registration_thanks_page", {})
