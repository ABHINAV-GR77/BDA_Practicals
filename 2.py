#import package
import matplotlib.pyplot as plt

#create a dataset
students=["Abhinav","karthikeyan","chitru","melvyn","vaisagh","albin"]
eng_mark=[86,80,88,77,50,80]
sci_mark=[90,67,89,36,56,90]
math_mark=[70,87,77,78,67,80]

#create bar chart properties
plt.figure(figsize=(8,6))
x=range(len(students))
plt.bar(x,math_mark,width=0.2,label="MATH",align='center')
plt.bar([i+0.2 for i in x],sci_mark,width=0.2,label="SCIENCE",align='center')
plt.bar([i+0.4 for i in x],eng_mark,width=0.2,label="ENGLISH",align='center')

#label the Bar chart
plt.xticks([i+0.2 for i in x],students)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Performance in Subjects")
plt.legend()
plt.show()



