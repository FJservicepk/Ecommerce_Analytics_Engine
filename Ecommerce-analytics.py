import csv
import math

transactions = []
with open("transactions.csv", 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        transactions.append((int(row[0]), row[1], row[2], float(row[3])))

# Defining a funtion to find unique categories from transaction.csv file
def unique_categories(data_list):
    categories = []
    for order_id, name, category, amount in data_list:
        categories.append(category)
        unique_category = set(categories)
    return unique_category

print("================================================")
print(" Ecommerce Analytics Dashboard")
print("================================================")

print("\n1. Finding Unique Categories")
display_uni_category = unique_categories(transactions)
print(display_uni_category)

# defining a funtion to find each categories revenue
def categories_revenue(data_list):
    cate_revenue = {}
    for order_id, name, category, amount in data_list:
        if category in cate_revenue:
            cate_revenue[category] += amount
        else:
            cate_revenue[category] = amount
    return cate_revenue

print("\n2. Categories Revenue")
total_categories_revenue = categories_revenue(transactions)
print(total_categories_revenue)

# defining a funtion to identify vip customer
def identify_vip_customer(data_list, vip_threshold = 500.0):
    customer_data = {}
    for order_id, name, category, amount in data_list:
        if name in customer_data:
            customer_data[name]["total_spent"] += amount
            customer_data[name]["order_count"] += 1
        else:
            customer_data[name] = {"total_spent": amount, "order_count": 1, "is_VIP": False}
    for vip in customer_data.values():
        if vip["total_spent"] >= vip_threshold:
            vip["is_VIP"] = True
    return customer_data

find_vip_cus = identify_vip_customer(transactions)
print("\n3. Identifying VIP Customer")
for name, info in find_vip_cus.items():
    print(f"Name: {name} | Total Spent: {info['total_spent']} | Order Count: {info['order_count']} | Vip Customer {info['is_VIP']}")

# defining a funtion to Calculate Stats
def Calculate_stats(data_list):
    amount_list = []
    for order_id, name, category, amount in data_list:
        amount_list.append(amount)
    mean_is = sum(amount_list)/len(amount_list)
    variance_is = sum((x - mean_is)**2 for x in amount_list)/len(amount_list)
    standard_dev = math.sqrt(variance_is)
    return {"Mean": mean_is, "Standard Deviation": standard_dev}

print("\n4. Calculating Stats")
stats = Calculate_stats(transactions)
print(f"Total Average Order: {stats['Mean']}")
print(f"Standard Deviation: {stats['Standard Deviation']:.2f}")
print("================================================")