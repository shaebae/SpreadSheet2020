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

print("check")


