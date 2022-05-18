"""This"""

from odoo.http import request
from odoo import http
from odoo.addons.portal.controllers import portal
import base64


class ContractsAccount(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super(ContractsAccount, self)._prepare_home_portal_values(counters)
        contracts = request.env['hr.contract'].search_count([('employee_id', '=', request.env.user.employee_id.id)])
        values.update({
            'contracts_count': contracts
        })
        return values

    @http.route('/contracts_history', type="http", auth="user", website=True)
    def contracts_history_details(self, **kw):
        contract_record = request.env['hr.contract'].search([('employee_id', '=', request.env.user.employee_id.id)])
        return request.render("contracts_account.contracts_history_web_portal",
                              {'contract_record': contract_record})

    @http.route('/individual_details/<model("hr.contract"):employee>', type="http", auth="user", website=True)
    def personal_contract_history_details(self, employee):
        return request.render("contracts_account.individual_contract_details_page_layout",
                              {'details': employee})

    @http.route('/file_save', type="http", auth="user", website=True)
    def save_uploaded_file(self, **kw):
        if kw:
            print("____________________________________", kw)
            contract = request.env['hr.contract'].browse()
            print("_____________________________________Contr", contract)
            Attachments = request.env['ir.attachment']
            name = kw.get('attachment').filename
            print("____________________________________________", name)
            file = kw.get('attachment')
            project_id = kw.get('project_id')
            Attachments.create({
                'name': name,
                'type': 'binary',
                'datas': base64.b64encode(file.read()),
                'res_model': contract._name,
                'res_id': project_id
            })

        # if request.httprequest.method == 'POST':
        #     # ...
        #     # code that creates and fills a dictonary with validated data
        #     # ...
        #     new_task = request.env['hr.contract'].sudo().create()
        #     if 'attachment' in request.params:
        #         attached_files = request.httprequest.files.getlist('attachment')
        #         for attachment in attached_files:
        #             attached_file = attachment.read()
        #             request.env['ir.attachment'].sudo().create({
        #                 'name': attachment.filename,
        #                 'res_model': 'hr.contract',
        #                 'res_id': new_task.id,
        #                 'type': 'binary',
        #                 'datas_fname': attachment.filename,
        #                 'datas': attached_file.encode('base64'),
        #             })
