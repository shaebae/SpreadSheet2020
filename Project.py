import csv

def read_data():
    data=[]

    with open('sales.csv','r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)

    return data

def run():
    data = read_data()

    months = []
    for row in data:
            month = (row['month'])
            months.append(month)

    sales = []
    for row in data:
            sale = int(row['sales'])
            sales.append(sale)
    total = sum(sales)
    length = len(sales)
    average = sum(sales)/len(sales)

    monthly_changes = []
    for i in range(11):
        monthly_change = ((float(sales[i + 1])/float(sales[i])-1)*100)
        monthly_changes.append(monthly_change)

    for i in range(11):
        print(months[i +1], format(monthly_changes[i]/100,".0%"))

    print("Monthly percentage changes:")


    print('Monthly Sales: {}'.format(sales))
    print('Total sales: {}'.format(total))
    print('Length list:{}'.format(length))
    print('Average Sales:{}'.format(average))

    min_sales = min(sales)
    print('Minimum Sales: {}'.format(min_sales))
    max_sales = max(sales)
    print('Maximum sales: {}'.format(max_sales))
run ()