# -*- coding: utf-8 -*-

import base64
from odoo import http
from odoo.http import request


class Website(http.Controller):
    @http.route(['/contacts'], type='http', auth="user", website=True)
    def contacts(self, **data):
        contacts = request.env['res.partner'].sudo().search([], order='id desc')
        return request.render(
            "controller.contacts_list", {'contacts': contacts})

    @http.route(['/manage/contact', '/manage/contact/<model("res.partner"):contact>'], type='http', auth="user",
                website=True)
    def manage_contact(self, contact=None, **post):
        print('\n\ncontact---------------', contact, '\n\n')
        print('\n\npost---------------', post.get('contact_id'), '\n\n')
        if post:
            partner_obj = request.env['res.partner'].sudo()
            data = {
                'name': post.get('name', False)
            }
            if post.get('contact_id', False):
                partner_obj.browse(int(post.get('contact_id'))).write(data)
            else:
                partner_obj.create(data)
            return request.redirect('/contacts')
        return request.render(
            "controller.contact_form", {'contact': contact})
