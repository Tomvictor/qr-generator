import xlwt
from datetime import datetime

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('Technorip')

ws.write(0, 0, "No", style0)
ws.write(0, 1, "Timestamp", style0)
ws.write(0, 2, "Verification code", style0)
ws.write(0, 3, "Verification URL", style0)

ws.write(1, 0, datetime.now(), style1)

wb.save('example.xls')
