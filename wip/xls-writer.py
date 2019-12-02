
import xlwt


eng_words =['test', 'home']


workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Sheet Name")
style = xlwt.easyxf()

# Specifying column






x=0
for z in eng_words:
    print (z)
    sheet.write(x, 0, z, style)
    x += 1





workbook.save("cristo.xls")
