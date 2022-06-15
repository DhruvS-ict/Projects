"""This"""

from odoo.http import request
from odoo import http


class CheckProductsWebsite(http.Controller):
    @http.route('/check_product', type="http", auth="user", website=True)
    def check_products_form(self):
        return request.render("check_products.check_products_form", {})

    @http.route('/check_product/products', type="http", auth="user", website=True)
    def check_products(self, **kw):
        check_record = request.env['product.product'].search([])
        filter_consu_sale = check_record.filtered(lambda x: x.detailed_type == 'consu' and x.sale_ok == True and x.purchase_ok == False)
        filter_consu_purchase = check_record.filtered(lambda x: x.detailed_type == 'consu' and x.sale_ok == False and x.purchase_ok == True)
        filter_consu_sale_purchase_on = check_record.filtered(lambda x: x.detailed_type == 'consu' and x.sale_ok == True and x.purchase_ok == True)
        filter_consu_sale_purchase_none = check_record.filtered(lambda x: x.detailed_type == 'consu' and x.sale_ok == False and x.purchase_ok == False)
        filter_service = check_record.filtered(lambda x: x.detailed_type == 'service' and (x.sale_ok == True or x.purchase_ok == True))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~filter_consu_sale record: ", filter_consu_sale)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~filter_consu_purchase record: ", filter_consu_purchase)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~filter_consu_sale_purchase_on record: ", filter_consu_sale_purchase_on)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~filter_consu_sale_purchase_none record: ", filter_consu_sale_purchase_none)
        for rec in check_record:
            print("___________________________", kw.get('sale_ok'))
            print("___________________________", kw.get('purchase_ok'))
            if kw.get('detailed_type') == 'consu' and kw.get('sale_ok') == 'on' and kw.get('purchase_ok') == None:
                return request.render("check_products.check_products_web_menu_list", {'check_record': filter_consu_sale})
            elif kw.get('detailed_type') == 'consu' and kw.get('sale_ok') == None and kw.get('purchase_ok') == 'on':
                return request.render("check_products.check_products_web_menu_list", {'check_record': filter_consu_purchase})
            elif kw.get('detailed_type') == 'consu' and kw.get('sale_ok') == 'on' and kw.get('purchase_ok') == 'on':
                return request.render("check_products.check_products_web_menu_list", {'check_record': filter_consu_sale_purchase_on})
            elif kw.get('detailed_type') == 'consu' and kw.get('sale_ok') == None and kw.get('purchase_ok') == None:
                return request.render("check_products.check_products_web_menu_list", {'check_record': filter_consu_sale_purchase_none})
            elif kw.get('detailed_type') == 'service':
                return request.render("check_products.check_products_web_menu_list", {'check_record': filter_service})
