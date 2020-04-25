import csv
import xlsxwriter

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

def read_data():
    data=[]

    with open('sales.csv','r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)

    return data

def run():
    data = read_data()

    sales = []
    for row in data:
            sale = int(row['sales'])
            sales.append(sale)

    total = sum(sales)
    length = len(sales)
    average = sum(sales)/len(sales)


    print('Monthly Sales: {}'.format(sales))
    print('Total sales: {}'.format(total))
    print('Length list:{}'.format(length))
    print('Average Sales:{}'.format(average))

    min_sales = min(sales)
    print('Minimum Sales: {}'.format(min_sales))
    max_sales = max(sales)
    print('Maximum sales: {}'.format(max_sales))

run ()

worksheet.write('A1', 'Months')
worksheet.write('B1', 'Average Sales')
worksheet.write('C1', 'Minimum Sales')
worksheet.write('D1', 'Max Sales')
worksheet.write('E1', 'Total Sales')

row=1
column = 0
content = ["Jan", "Feb", "March", "April","May", "June", "July","August","September", "August", "September", "October", "Nov", "Dec"]

for item in content:
    worksheet.write(row, column, item)
    row +=2
#and add the results in other rows

workbook.close()


