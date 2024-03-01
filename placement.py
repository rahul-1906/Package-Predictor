import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
Linear = LinearRegression()
import random
plt.rcParams["font.family"] = "cursive"

df=pd.read_csv('D:\placement.csv')
x=df.iloc[:,0:1]
y=df.iloc[:,1:2]

Linear.fit(x,y)


coefi=Linear.coef_
Sales_prediction=Linear.predict(x)
plt.xlabel('CGPA')
plt.ylabel('Package')
#plt.plot(x,Sales_prediction)

plt.figure(facecolor='lightgreen' )
ax = plt.axes()
ax.set_facecolor("#b7f8db")
plt.title("CGPA vs PACKAGE")
plt.xlabel('CGPA')
plt.ylabel('PACKAGE')

plt.scatter(x,y, color='grey' ,  facecolor='aliceblue' , marker='.')

plt.scatter(x,Sales_prediction , color='black' ,  facecolor='white' , marker='*')


cg= float(input("Enter Your CGPA: "))
pack = random.random()*5
pack = str(round(pack, 2))
print(pack)
