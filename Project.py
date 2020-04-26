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

    months = []
    for row in data:
        month = (row['month'])
        months.append(month)

    expenditure = []
    for row in data:
        expenditures = int(row['expenditure'])
        expenditure.append(expenditures)

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

    worksheet.write(0, 0, 'Month')
    row = 1
    for item in months:
        worksheet.write(row, 0, item)
        row = row + 1

    worksheet.write(0, 1, 'Sales')
    row = 1
    for item in sales:
        worksheet.write(row, 1, item)
        row = row + 1

    worksheet.write(0, 2, 'Expenditures')
    row = 1
    for item in expenditure:
        worksheet.write(row, 2, item)
        row = row + 1

    worksheet.write(0, 3, 'Monthly Sales Changes %')
    row = 2
    for item in monthly_changes:
        worksheet.write(row, 3, format(item/100,".0%"))
        row = row + 1
run ()



#and add the results in other rows

workbook.close()
