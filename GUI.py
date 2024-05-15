import tkinter
from tkinter import *
from tkinter.messagebox import showerror

window = Tk()
window.title("Bank Misr , plan your loan application")
window.geometry("1000x500+200+50")

def Calculate():
    amount_of_money = float(E2.get())
    number_of_years = int(E3.get())
    if number_of_years==1:
        interest_in_one_year = int((amount_of_money * (13.76 / 100)))
        total_interset = int((interest_in_one_year * number_of_years))
        total_loan = int(((interest_in_one_year * number_of_years) + amount_of_money))
        pay_per_month = int((total_loan / (number_of_years * 12)))
        output_text = f"interest in one year: {interest_in_one_year}\n"f"total interest: {total_interset}\n" \
                      f"total loan: {total_loan}\n"f"payment per month: {pay_per_month}"
    elif number_of_years==3:
        interest_in_one_year = int((amount_of_money*(14.06/100)))
        total_interset =int( (interest_in_one_year*number_of_years))
        total_loan =int( ((interest_in_one_year*number_of_years)+amount_of_money))
        pay_per_month = int((total_loan / (number_of_years * 12)))
        output_text = f"interest in one year: {interest_in_one_year}\n"f"total interest: {total_interset}\n" \
                      f"total loan: {total_loan}\n"f"payment per month: {pay_per_month}"
    elif number_of_years == 5:
        interest_in_one_year = int((amount_of_money * (14.87 / 100)))
        total_interset = int((interest_in_one_year * number_of_years))
        total_loan = int(((interest_in_one_year * number_of_years) + amount_of_money))
        pay_per_month = int((total_loan / (number_of_years * 12)))
        output_text = f"interest in one year: {interest_in_one_year}\n"f"total interest: {total_interset}\n" \
                      f"total loan: {total_loan}\n"f"payment per month: {pay_per_month}"
    elif number_of_years==7:
        interest_in_one_year = int((amount_of_money * (15.71 / 100)))
        total_interset = int((interest_in_one_year * number_of_years))
        total_loan = int(((interest_in_one_year * number_of_years) + amount_of_money))
        pay_per_month = int((total_loan / (number_of_years * 12)))
        output_text = f"interest in one year: {interest_in_one_year}\n"f"total interest: {total_interset}\n" \
                      f"total loan: {total_loan}\n"f"payment per month: {pay_per_month}"
    elif number_of_years!= int() or amount_of_money!= float():
        showerror("showerror","error")
    output_label.config(text=output_text)
def clear():

    E2.delete(0,'end')
    E3.delete(0,'end')
    output_label.config(text='')
def EXIT():
    window.quit()

f1 = Frame(window)
f1.pack(side=TOP)
f2= Frame(window)
f2.pack(side =LEFT)
f3 = Frame(window)
f3.pack(side =RIGHT)
f4 = Frame(window)
f4.pack(side =BOTTOM)
f5 = Frame(window)
f5.pack(side =BOTTOM)
f6 = Frame(window)
f6.pack(side=BOTTOM)
photo = PhotoImage(file="images.png")
l = Label(f1,text="Bank Misr , plan your loan application",image=photo)
l.pack()
variable = tkinter.StringVar()
variable.set("selec your jop")

select_option = tkinter.OptionMenu(
    f1,
    variable,
    "doctor",
    "engineer",
    "teacher",
)
select_option.pack()
l2 = Label(f2,text="enter loan amount:",bg="yellow",font=("Aerial 16 bold italic"),pady=5)
l2.pack()
E2 =Entry(f3,bd=5,bg="yellow",font=("Aerial 16 bold italic"))
E2.pack()
l3 = Label(f2,text="enter loan years:",bg="light blue",font=("Aerial 16 bold italic"),pady=5)
l3.pack()
E3 = Entry(f3,bd=5,font=("Aerial 16 bold italic"),bg='light blue')
E3.pack()
B1 = Button(f5,text="Calculate",command=Calculate,font=("Aerial 10 bold italic"))
B1.pack()
B2 = Button(f4,text="clear",command=clear,font=("Aerial 10 bold italic"))
B2.pack(side=RIGHT)
B3 = Button(f4,text="exit",command=EXIT,font=("Aerial 10 bold italic"))
B3.pack(side=LEFT)
output_label = Label(f6,font=("Aerial 16 bold italic"),bg="light green")
output_label.pack()
window.mainloop()
