import csv
import xlsxwriter
import seaborn

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

    months = []
    for row in data:
        month = (row['month'])
        months.append(month)

    total = sum(sales)
    length = len(sales)
    average = sum(sales)/len(sales)

    monthly_changes = []
    for i in range(11):
        monthly_change = ((float(sales[i + 1])/float(sales[i])-1)*100)
        monthly_changes.append(monthly_change)

    print("Monthly percentage changes:")
    for i in range(11):
        print(months[i +1], format(monthly_changes[i]/100,".0%"))

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
worksheet.write('B1', 'Monthly sales')
worksheet.write('C1', '% of change sales')
worksheet.write('D1', 'Minimum Sales')
worksheet.write('E1', 'Max Sales')


row=1
column = 0
content = ["Jan", "Feb", "March", "April","May", "June", "July","August","September", "August", "September", "October", "Nov", "Dec", "", "Total Sales", "Average Sales"]

for item in content:
    worksheet.write(row, column, item)
    row +=1
#and add the results in other rows

workbook.close()

print("test")


