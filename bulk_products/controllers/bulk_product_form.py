"""This"""

from odoo.http import request
from odoo import http
from odoo.addons.portal.controllers import portal
import base64


class BulkProductsWebsiteForm(portal.CustomerPortal):
    @http.route('/product_list', type="http", auth="user", website=True)
    def bulk_product_list(self, **kw):
        bulk_record = request.env['bulk.products'].search([])
        return request.render("bulk_products.bulk_product_website_record_list",
                              {'bulk_record': bulk_record})

    @http.route('/product_list/<model("bulk.products"):product>', type="http", auth="user", website=True)
    def bulk_product_list_details(self, product):
        return request.render("bulk_products.bulk_product_website_list_detail",
                              {'bulk_detail': product})

    @http.route(['/manage/bulk_products', '/manage/bulk_products/<model("bulk.products"):price>'], type='http', auth="user",
                website=True)
    def manage_contact(self, price=None, **post):
        print('\n\ncontact---------------', price, '\n\n')
        print('\n\npost---------------', post.get('bulk_product_id'), '\n\n')
        master_rec = request.env['product.template'].search([])
        if post:
            product_obj = request.env['bulk.products'].sudo()
            data = {
                'bulk_products_name': post.get('bulk_products_name', False),
                'master_product_id': post.get('master_product_id'),
                'bulk_products_email': post.get('bulk_products_email', False)
            }
            print("`````````````````````````````````data", data)
            if post.get('bulk_product_id', False):
                product_obj.browse(int(post.get('bulk_product_id'))).write(data)
            else:
                product_obj.create(data)
            return request.redirect('/product_list')
        return request.render("bulk_products.bulk_product_edit", {'bulk_price': price, 'master': master_rec})
