"""This"""

from odoo.http import request
from odoo import http
import base64


class ContactCreationForm(http.Controller):
    @http.route('/contact_creation', type="http", auth="user", website=True)
    def contact_creation_record_in_contacts(self, **kw):
        return request.render("dhruv_2_6_22.contact_creation_form", {})

    @http.route('/contact_creation/contact_creation_thankyou', type="http", auth="user", website=True)
    def redirect_contact_creation_thankyou_page(self, **kw):
        files = request.httprequest.files.getlist('contact_creation_image')
        for file in files:
            partner = request.env['res.partner'].create({
                'name': kw.get('contact_creation_your_name'),
                'email': kw.get('contact_creation_your_email'),
                'phone': kw.get('contact_creation_phone_number'),
                'image_1920': base64.b64encode(file.read())
            })

        return request.render('dhruv_2_6_22.contact_creation_thanks_page', {})
