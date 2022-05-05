"""This"""
import base64
from io import BytesIO
from odoo.tools.misc import xlwt
from odoo import models, fields, api
from datetime import date



class XlsxReport(models.TransientModel):
    """This class is for fields & orm methods."""
    _name = 'xls.rent'
    # _inherit = 'report.report_xlsx.abstract'
    s_date = fields.Date(string='Start Date', required=True, default=date.today().replace(day=11))
    e_date = fields.Date(string='End Date', required=True, default=date.today().replace(day=11))  #date
    employee_id = fields.Many2one('res.partner', string="Employee")  #company_id
    summary_data = fields.Char('Name', size=256)
    excel_file = fields.Binary('Pay Slip Summary Report', readonly=True)  #file_name
    state = fields.Selection([('choose', 'choose'), ('get', 'get')],
                             default='choose')

    def action_xlwt_report(self):
        employee_name = self.employee_id.name     #company
        excel_file = 'Timesheet.xls'      #Report
        workbook = xlwt.Workbook(encoding="UTF-8")
        format0 = xlwt.easyxf(
            'font:height 500,bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                              left thin, right thin, top thin, bottom thin;')
        formathead2 = xlwt.easyxf(
            'font:height 250,bold True;pattern: pattern solid, fore_colour gray25;align: horiz center; borders: top_color black, bottom_color black, right_color black, left_color black,\
                              left thin, right thin, top thin, bottom thin;')
        format1 = xlwt.easyxf('font:bold True;pattern: pattern solid, fore_colour gray25;align: horiz left; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                 left thin, right thin, top thin, bottom thin;')
        format2 = xlwt.easyxf('font:bold True;align: horiz left')
        format3 = xlwt.easyxf('align: horiz left; borders: top_color black, bottom_color black, right_color black, left_color black,\
                                 left thin, right thin, top thin, bottom thin;')
        sheet = workbook.add_sheet("Payslip Summary Report")
        sheet.col(0).width = int(7 * 260)
        sheet.col(1).width = int(30 * 260)
        sheet.col(2).width = int(40 * 260)
        sheet.col(3).width = int(20 * 260)
        sheet.row(0).height_mismatch = True
        sheet.row(0).height = 150 * 4
        sheet.row(1).height_mismatch = True
        sheet.row(1).height = 150 * 2
        sheet.row(2).height_mismatch = True
        sheet.row(2).height = 150 * 3
        sheet.write_merge(0, 0, 0, 3, 'Aktiv Software Report', format0)
        sheet.write_merge(1, 1, 0, 3, 'Date:' + str(self.date), formathead2)
        sheet.write_merge(2, 2, 0, 3, 'Employee : ' + employee_name, formathead2)
        sheet.write(3, 0, 'Sl.No#', format1)
        sheet.write(3, 1, 'Employee Bank Account', format1)
        sheet.write(3, 2, 'Employee Name', format1)
        sheet.write(3, 3, 'Amount', format1)
        fp = BytesIO()
        workbook.save(fp)
        self.write(
            {'state': 'get', 'excel_file': base64.encodestring(fp.getvalue()), 'summary_data': excel_file})
        fp.close()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'xls.rent',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'target': 'new',
        }
