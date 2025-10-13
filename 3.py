from statistics import LinearRegression

import matplotlib.pyplot as plt
import numpy as np
from numpy import reshape
from sklearn.linear_model import LinearRegression

students=["Alice","Bob","Carol","eve","helen"]
x=np.array([1,2,3,4,5,6,7,8,9]),reshape(-1,1)
y=np.array([2,4,6,8,6,8,5,6,7])
model=LinearRegression()
model.fit(x,y)
y_pred=model.predict(x)

print(f"Coefficent (Slope): {model.coef-[0]}")
print(f"Intercept: {model.intercept_}")
plt.plot(x,y_pred,color='r',label="Linear Regression")
plt.plot(x,y,color='b',label="Actual Data")

plt.title('Linear Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
plt.legend()
