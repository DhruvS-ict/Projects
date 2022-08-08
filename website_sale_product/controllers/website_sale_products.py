"""This"""

from odoo.http import request
from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleInheritForVariants(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True)
    def shop(self, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        res = super(WebsiteSaleInheritForVariants, self).shop(page=0, category=None)
        # self.notify_danger("Welcome to Python World")
        # print("Welcome to Python World")
        # request.render('covid_delivery.covid_alert_message')
        return res
