import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(45)

pages = np.random.randint(100, 1000, 20)
price = np.random.randint(200, 1500, 20)
total_price = pages * price

df = pd.DataFrame(
    {
        "pages" : pages,
        "price" : price,
        "total_price" : total_price
    }
)

print("---------LIBRARY MANAGEMENT SYSTEM----------")
print(df)

print("\n AVERAGE_PRICE: ", np.mean(total_price))
print("\n HIGHIEST_PRICE: ", np.max(total_price))
print("\n LOWEST_PRICE: ", np.min(total_price))

print("\n ------------DISCOUNT IN BOOKS----------")
df["Discount"] = df["total_price"] / 10
print(df)

print("\n ---------FINAL PRICE--------")
print(total_price)

print("\n -----------MOST EXPENSIVE BOOK-----------")
df.sort_values(by="price", ascending = False).head(5)
print(df)

print("\n  ---------TOP 5 BOOKS-------")
print(df["total_price"].head())

print("\n --------LINE PLOT CHART---------")

plt.plot(
    total_price, color = "green"
)
plt.title("-----PRICE CHART-----")
plt.show()

print("\n ----------BAR CHART----------")

plt.bar(
    pages,
    price, linewidth = 70, color = "red"
)

plt.show()

print("\n ----------PIE CHART--------")

plt.pie(
    price
)
plt.title("-------- show pages--------")
plt.show()

analysis = df.groupby("price")["total_price"]
print(analysis)

df.to_csv("books.csv")
print(pd.read_csv("books.csv"))
