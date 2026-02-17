import tkinter as tk
from tkinter import messagebox

class Calculator:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")

        self.labelNum1 = tk.Label(self.window,text="Number 1:")
        self.labelNum1.place(x=10,y=10)
        self.entryNum1 = tk.Entry(self.window)
        self.entryNum1.place(x=80,y=10)

        self.radioValue = tk.IntVar()
        self.radioValue.set(0)
        self.radioButtonAdd = tk.Radiobutton(self.window, text="Add", value=1, variable=self.radioValue)
        self.radioButtonAdd.place(x=220, y=10)
        self.radioButtonSubtraction = tk.Radiobutton(self.window, text="Subtraction", value=2, variable=self.radioValue)
        self.radioButtonSubtraction.place(x=220, y=40)
        self.radioButtonMultiplication = tk.Radiobutton(self.window, text="Multiplication", value=3, variable=self.radioValue)
        self.radioButtonMultiplication.place(x=220, y=70)
        self.radioButtonDivision = tk.Radiobutton(self.window, text="Division", value=4, variable=self.radioValue)
        self.radioButtonDivision.place(x=220, y=100)

        self.labelNum2 = tk.Label(self.window,text="Number 2:")
        self.labelNum2.place(x=10,y=40)
        self.entryNum2 = tk.Entry(self.window)
        self.entryNum2.place(x=80,y=40)

        self.labelResult = tk.Label(self.window,text="Result:")
        self.labelResult.place(x=30,y=70)
        self.entryResult = tk.Entry(self.window)
        self.entryResult.place(x=80,y=70)
        self.entryResult.configure(state="disabled")

        self.buttonCalc = tk.Button(self.window,text="Calc", command=self.Calc)
        self.buttonCalc.place(x=80, y=100)

        self.buttonClear = tk.Button(self.window,text="Clear", command=self.Clear)
        self.buttonClear.place(x=120, y=100)

        
        self.window.geometry("320x150")
        self.window.mainloop()
    
    def Clear(self):
        self.radioValue.set(0)
        self.entryResult.configure(state="normal")
        self.entryResult.delete(0, tk.END)
        self.entryResult.configure(state="disabled")
        self.entryNum1.delete(0, tk.END)
        self.entryNum2.delete(0, tk.END)

    def Calc(self):

        self.entryResult.configure(state="normal")
        self.entryResult.delete(0, tk.END)
        self.entryResult.configure(state="disabled")
        
        oper = int(self.radioValue.get())
        n1 = float(self.entryNum1.get())
        n2 = float(self.entryNum2.get())
        result = 0
        match oper:
            case 1:
                result = n1 + n2
            case 2:
                result = n1 - n2
            case 3:
                result = n1 * n2
            case 4:
                result = n1 / n2
            case _:
                messagebox.showerror("Error","Please Selecte an option!!!")
        self.entryResult.configure(state="normal")
        self.entryResult.insert(0,result)
        self.entryResult.configure(state="disabled")

def main():
    objCalculator = Calculator()

if __name__=="__main__":
    main()