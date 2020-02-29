from tkinter import *
from sklearn import tree
from tkinter import messagebox
app = Tk()
app.geometry("1366x760")
app.title("Old Car Price Prediction")




#########################################################################################
####             work of pandas features and label
#########################################################################################
import pandas as pd
data = pd.read_csv('trained_data2.csv', header = 0)

features = []
for i in range(len(data)):
    x = list(data.iloc[i])
    x.pop()
    features.append(x)

# for label
label = list(data.Price)
print(features, label)

########################################################################################
####               main Working of prediction with sklearn



########################################################################################



def getdata():
    global features
    global label
    x1 = float(input1.get())
    x2 = float(input2.get())
    x3 = float(input3.get())
    x4 = float(input4.get())
    x5 = float(input5.get())
    x6 = float(input6.get())
    x7 = float(input7.get())
    x8 = float(input8.get())
    x9 = float(input9.get())
    print(x1, x2, x3, x4, x5, x6, x7, x8, x9)

    
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, label)

    print(clf.predict([[x1, x2, x3, x4, x5, x6, x7, x8, x9]]))
        
    arr = clf.predict([[x1, x2, x3, x4, x5, x6, x7, x8, x9]])
    print("arr = " , arr)
    
    final_result.delete(0, END)
    final_result.insert(0, arr[0])


    

frame1 = Frame(app)


Heading = Label(frame1, text="OLD CAR PRICE PREDICTION", font = ('helvetica', 30 , "underline"), fg = "blue")
Heading.grid()

frame1.pack(pady = 40)


frame2 = Frame(app)

#frame2_label = Label(frame2, text="Welcome !", fg = "red").grid(row = 0, column = 0, columnspan = 3)


label1 = Label(frame2, text = " Engine Size ", font = ('helvetica', 15 ), justify =  LEFT).grid(row = 1, column = 0)
input1 = Entry(frame2, font = ('helvetica', 20))
input1.grid(row = 2, column = 0, padx = 50)

label2 = Label(frame2, text=" Cylinders ", font = ('helvetica', 15 )).grid(row = 1, column = 1)
input2 = Entry(frame2, font = ('helvetica', 20))
input2.grid(row = 2, column = 1, padx = 50)

label3 = Label(frame2, text="Horse Power", font = ('helvetica', 15 )).grid(row = 1, column = 2)
input3 = Entry(frame2, font = ('helvetica', 20))
input3.grid(row = 2, column = 2, padx = 50)


label4 = Label(frame2, text = " MPG City ", font = ('helvetica', 15 ), justify =  LEFT).grid(row = 3, column = 0)
input4 = Entry(frame2, font = ('helvetica', 20))
input4.grid(row = 4, column = 0, padx = 50)

label5 = Label(frame2, text=" MPG Highway ", font = ('helvetica', 15 )).grid(row = 3, column = 1)
input5 = Entry(frame2, font = ('helvetica', 20))
input5.grid(row = 4, column = 1, padx = 50)

label6 = Label(frame2, text=" Weight  ", font = ('helvetica', 15 )).grid(row = 3, column = 2)
input6 = Entry(frame2, font = ('helvetica', 20))
input6.grid(row = 4, column = 2, padx = 50)


label7 = Label(frame2, text=" WheelBase ", font = ('helvetica', 15 )).grid(row = 5, column = 0)
y = StringVar()
input7 = Entry(frame2, textvariable = y, font = ("helvetica", 20))
input7.grid(row = 6, column = 0, padx = 50)


label8 = Label(frame2, text=" Length (Car) ", font = ('helvetica', 15 )).grid(row = 5, column = 1)
y = StringVar()
input8 = Entry(frame2, textvariable = y, font = ("helvetica", 20))
input8.grid(row = 6, column = 1, padx = 50)


label9 = Label(frame2, text=" Distance Covered (in Kms) ", font = ('helvetica', 15)).grid(row = 5, column = 2)
y = StringVar()
input9 = Entry(frame2, textvariable = y, font = ("helvetica", 20))
input9.grid(row = 6, column = 2, padx = 50)





# result Entry Tag


label_final_result = Label(frame2, text="Expected Price : Rs. ").grid(row = 7,column = 0)
final_result = Entry(frame2, font = ('helvetica', 30 ))
final_result.grid(row = 7, column =1,  columnspan = 2, pady = 40)







button2 = Button(frame2, text = "Get Price", font = ('helvetica', 25 ), command = getdata).grid(row = 7, column = 2)

frame2.pack(pady = 10)




app.mainloop()
