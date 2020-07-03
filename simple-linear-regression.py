import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('apartment_prices.xlsx')
##df = df.set_index('Property')
print(df.head())

price = df['Price'] #Prices of all apartments
size = df['m2'] #Sizes of all apartments
Property = df['Property'] #List of all properties
apartments = [100, 110, 120, 130, 140, 150]

#Calculate mean
mean_size = round(np.mean(size), 4)
mean_price = round(np.mean(price), 4)

n = len(price)
numerator = 0
denominator = 0
for i in range(n):
    numerator += (size[i] - mean_size) * (price[i] - mean_price)
    denominator += (size[i] - mean_size) ** 2

#Simple linear regression coefficients
b1 = round(numerator / denominator, 4)
b0 = round(mean_price - b1 * mean_size, 4)

min_size = np.min(size)
max_size = np.max(size)

x = np.linspace(min_size, max_size)
y = b0 + b1 * x

abs_difference = []
rel_difference = []
ss_r = 0
ss_t = 0

for i in range(n):
    y_pred = b0 + b1 * size[i]
    ss_r += (price[i] - y_pred) ** 2
    ss_t += (price[i] - mean_price) ** 2
    abs_difference.append(round(price[i] - y_pred,0))
    rel_difference.append(round((price[i] - y_pred) / y_pred,4))

for i in range(n):
    if rel_difference[i] == np.min(rel_difference):
        print('The cheapest property is property '+ Property[i]+
        ' with a price of ' + str(price[i]) + ' and size of '+
        str(size[i]) + ' m2.')

r2 = 100 - round((ss_r/ss_t),4) * 100
print('R-squared - Coefficient of determination: ' + str(r2) + '%.')

def estimate(size):
    price = round(b0 + b1 * size,0)
    return price

for i in apartments:
    print('The apartment has a size of ' + str(i) +
    ' m2 and it\'s estimated price is ' + str(estimate(i)))

plt.scatter(size, price, color = 'red', label = 'Data points')
plt.plot(x,y, color = 'blue', label = 'Regression line')
plt.xlabel('Size in m2')
plt.ylabel('Price in EUR')
plt.legend()
plt.show()
