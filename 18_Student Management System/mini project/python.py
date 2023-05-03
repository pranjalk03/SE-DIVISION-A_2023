marks=[] sum1=0

for i in range(0,5):
marks.append(int(input("Enter marks of subject :  ")))
sum1 = sum1 + marks[i]
print(“Sum of marks is”,sum1)

per = sum1/5
print(“Percentage is “, per)
if per>90:
print(" A")
elif per>70:
       print(" B")
elif per>50:
       print(" C")
elif per>30:
       print(" D")
else:
print(" Fail")
