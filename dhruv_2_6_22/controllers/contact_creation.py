"""This"""

from odoo.http import request
from odoo import http
from odoo.addons.portal.controllers import portal
import base64
from odoo.tools.translate import encode


class ContactCreationForm(http.Controller):
    @http.route('/contact_creation', type="http", auth="user", website=True)
    def contact_creation_record_in_contacts(self, **kw):
        return request.render("dhruv_2_6_22.contact_creation_form", {})

    # @http.route('/image_save', type="http", auth="user", website=True)
    # def save_uploaded_file(self, **kw):
    #     multiple_attachments = request.httprequest.files.getlist('attachment')
    #     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~multiple_attachments~~~", multiple_attachments)
    #     for upload_image in multiple_attachments:
    #         print("____________________________________", kw)
    #         contract = request.env['res.partner'].browse()
    #         print("_____________________________________Contr", contract)
    #         Attachments = request.env['ir.attachment']
    #         name = kw.get('attachment').filename
    #         print("____________________________________________", name)
    #         file = kw.get('attachment')
    #         project_id = kw.get('project_id')
    #         Attachments.create({
    #             'name': name,
    #             'res_name': name,
    #             'type': 'binary',
    #             'datas': base64.b64encode(file.read()),
    #             'res_model': contract._name,
    #             'res_id': project_id
    #         })

    # @http.route('/image_save', type="http", auth="public", website=True)
    # def save_uploaded_file(self, **kw):
    #
    #     files = request.httprequest.files.getlist('contact_creation_image')
    #
    #     for file in files:
    #
    #         partner_id = int(kw.get('partner_id'))
    #
    #         attachment = file.read()
    #
    #         partner = request.env['res.partner'].sudo().browse(partner_id)
    #
    #         if partner:
    #             partner.write({'image_1920': base64.encodestring(attachment)})
    #
    #             request.env.user.image_1920 = base64.encodestring(attachment)
    #
    #     return request.redirect('/home')


    @http.route('/contact_creation/contact_creation_thankyou', type="http", auth="user", website=True)
    def redirect_contact_creation_thankyou_page(self, **kw):
        files = request.httprequest.files.getlist('contact_creation_image')

        for file in files:

            partner_id = int(kw.get('partner_id'))

            attachment = file.read()
            print("_____________________________________attachment", attachment)

            partner = request.env['res.partner'].sudo().browse(partner_id)

            if partner:
                partner.write({'image_1920': base64.encodestring(attachment)})

                request.env.user.image_1920 = base64.encodestring(attachment)

        if kw:
            request.env['res.partner'].sudo().create({'name': kw.get('contact_creation_your_name'),
                                                      'email': kw.get('contact_creation_your_email'),
                                                      'phone': kw.get('contact_creation_phone_number'),
                                                      'image_1920': kw.get('contact_creation_your_image')})

        return request.render('dhruv_2_6_22.contact_creation_thanks_page', {})

