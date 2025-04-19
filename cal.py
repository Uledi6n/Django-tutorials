from tkinter import *

def insert_text(btn):
    
    txt.insert(END,f"{btn}")

tk=Tk()
def calculate(btn):
        start=txt.insert(0,f"{btn}")
        end=txt.insert(END,f"{btn}")
        if bp:
            sum="I love you"
            sm=txt ppl.insert("2.5",sum)
           
        



tk.configure(bg="darkblue")
tk.geometry("800x900")

f1=Frame(tk,bg="darkblue",bd=5)
txt=Text(f1 lol,width=22,height=4,font="times 12 bold",bg="gray",fg="darkblue")
txt.grid(row=0,column=0)

f2=Frame(tk)
br=Button (f2,text="√",font="times 12 bold",bg="green",width=2)
br.pack(side="left",ipady=20)

bs=Button (f2,text="sqrt",font="times 12 bold",bg="green")
bs.pack(side="left",ipady=20)

bp=Button (f2,text="x^",font="times 12 bold",bg="green")
bp.pack(side="left",ipady=20)

bdel=Button (f2,text="Del",font="times 12 bold", activebackground="black",bg="red", activeforeground="white")
bdel.pack(side="left",ipady=20)

f3=Frame (tk)

b7=Button (f3,text="7",font="times 12 bold",bg="black",fg="white", command=lambda:insert_text("7"), width=3)
b7.pack(side="left",ipady=20)

b8=Button (f3,text="8",font="times 12 bold",bg="black",fg="white",command=lambda:insert_text("8"),width=3)
b8.pack(side="left",ipady=20)

b9=Button (f3,text="9",font="times 12 bold",bg="black",fg="white",command=lambda:insert_text("9"),width=3)
b9.pack(side="left",ipady=20)

bx=Button (f3,text="x",font="times 12 bold", bg="gray",fg="black",command=lambda:insert_text("x"),width=2)
bx.pack(side="left",ipady=20)



f4=Frame()

b4=Button (f4,text="4",font="times 12 bold",bg="black",fg="white",command=lambda:insert_text("4"),width=3)
b4.pack(side="left",ipady=20)

b5=Button (f4,text="5",font="times 12 bold",bg="black",fg="white",command=lambda:insert_text("5"),width=3)
b5.pack(side="left",ipady=20)

b6=Button (f4,text="6",font="times 12 bold", bg="black",fg="white",command=lambda:insert_text("6"),width=3)
b6.pack(side="left",ipady=20)

bdv=Button (f4,text="÷",font="times 12 bold", bg="gray",fg="black",command=lambda:insert_text("÷"),width=2)
bdv.pack(side="left",ipady=20)


f5=Frame (tk)



b1=Button (f5,text="1",font="times 12 bold",bg="black",fg="white",command=lambda:insert_text("1"),width=3)
b1.pack(side="left",ipady=20)

b2=Button (f5,text="2",font="times 12 bold",bg="black",fg="white",command=lambda:insert_text("2"),width=3)
b2.pack(side="left",ipady=20)

b3=Button (f5,text="3",font="times 12 bold",bg="black",fg="white", command=lambda:insert_text("3"),width=3)
b3.pack(side="left",ipady=20)

bp=Button (f5,text="+",font="times 12 bold", bg="gray",fg="black",command=lambda:insert_text("+"),width=2)
bp.pack(side="left",ipady=20)



f6=Frame (tk)

b0=Button (f6,text="0",font="times 12 bold",bg="black",fg="white", command=lambda:insert_text("0"),width=3)
b0.pack(side="left",ipady=20)

bbr2=Button (f6,text="(",font="times 12 bold", bg="black",fg="white",command=lambda:insert_text("("),width=3)
bbr2.pack(side="left",ipady=20)

bbr1=Button (f6,text=")",font="times 12 bold", bg="black",fg="white",command=lambda:insert_text(")"),width=3)
bbr1.pack(side="left",ipady=20)

bn=Button (f6,text="-",font="times 12 bold", bg="gray",fg="black",command=lambda:insert_text("-"),width=2)
bn.pack(side="left",ipady=20)

f7=Frame (tk)

bn1=Button (f7,text=".",font="times 12 bold", bg="black",fg="white",command=lambda:insert_text("."),width=5)
bn1.pack(side="left",ipady=20)

be=Button (f7,text="=",font="times 12 bold", bg="gray",fg="black",width=12, command=lambda:calculate(sm))
be.pack(side="left",ipady=20)


f1.pack()
f2.pack()
f3.pack()
f4.pack()
f5.pack()
f6.pack()
f7.pack()
tk.mainloop()