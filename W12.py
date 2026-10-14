import matplotlib.pyplot as plt

def create_line_chart():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 4, 10]
    plt.plot(x, y, linestyle='--', marker='o')
    plt.title("Simple Line Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()

def create_bar_chart():
    products = ['Product A', 'Product B', 'Product C']
    revenue = [45000, 78000, 32000]
    plt.bar(products, revenue)
    plt.ylabel('Revenue ($)')
    plt.title('Product Performance')
    plt.show()

def create_pie_chart():
    hobbies = ['Gaming', 'Reading', 'Exercise', 'Gardening']
    hours = [10, 6, 5, 3]
    plt.pie(hours, labels=hobbies)
    plt.title('Weekly Time Spent on Hobbies')
    plt.show()

create_line_chart()
create_bar_chart()
create_pie_chart()