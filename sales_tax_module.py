SALES_TAX_RATE = 0.06

def calculate_sales_tax(total):
    return round(total * SALES_TAX_RATE, 2)

def calculate_total_after_tax(total):
    return round(total + calculate_sales_tax(total), 2)