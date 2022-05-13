"""This"""

from odoo import http
from odoo.http import request


class ReferralProgramForm(http.Controller):
    @http.route('/referral_program_form', type="http", auht="user", website=True)
    def create_web_form(self, **kw):
        if kw:
            request.env['hr.referral.application'].sudo().create(kw)

            request.env['res.partner'].sudo().create({'name': kw.get('name'),
                                                      'email': kw.get('email')})
            print("____________________________", kw)
        referral_name = request.env['hr.employee'].sudo().search([])
        degree_rec = request.env['hr.recruitment.degree'].sudo().search([])
        department_rec = request.env['hr.job'].sudo().search([])
        return request.render("hr_referral_application.referral_program_form",
                              {'referral_name_id': referral_name,
                               'degree_id': degree_rec,
                               'department_id': department_rec})
