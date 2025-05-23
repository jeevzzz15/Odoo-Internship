from odoo import models

class ModelOneXlsx(models.AbstractModel):
    _name = 'report.zestybeanz.report_model_one_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, modelonedata):
        for obj in modelonedata:
            report_name = obj.name
            # One sheet by partner
            sheet = workbook.add_worksheet(report_name[:31])
            #bold = workbook.add_format({'bold': True})
            format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'color' : 'red','bold': True})
            format2 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'color' : 'blue','bold': True})
            sheet.write(2, 2, "Name", format1)
            sheet.write(3, 2, "Age", format1)
            sheet.write(4, 2, "Gender", format1)
            
            sheet.write(2, 3, obj.name, format2)
            sheet.write(3, 3, obj.age, format2)
            sheet.write(4, 3, obj.gender, format2)