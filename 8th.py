import pandas as pd
data=[10,20,30,40,50,60]
pandas_series=pd.Series(data)

print("Original Pandas Series")
print(pandas_series)
print(f"Type of Pands Series :{type(pandas_series)}")

python_list=pandas_series.tolist()

print("\n Converted Python List")
print(python_list)
print(f"Type of Pandas list :{type(python_list)}")


data1=[10,"Abhinav",30.00,True]
pandas_series1=pd.Series(data1)

print("Original Mixed Pandas Series")
print(pandas_series1)
print(f"Type of Pandas Series :{type(pandas_series1)}")

python_list1=pandas_series1.tolist()

print("\n Converted Python List")
print(python_list1)
print(f"Type of Pandas list :{type(python_list1)}")