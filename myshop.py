from tkinter import *
from tkinter import messagebox as msg
from  tkinter import ttk
import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='myshop'
    )
cursor=db.cursor()
a=Tk()
a.title("Product")
a.geometry('900x800')
a.configure(bg='white')
la_head=Label(a,text='FRESH MART',bg='white',fg='#d627b6',font=('Times New Roman',20,'bold'))
la_head.pack()
img_new=PhotoImage(file='new1.png')
img_shop=PhotoImage(file='main.png')
img_view=PhotoImage(file='list1.png')
img_update=PhotoImage(file='update1.png')
img_del=PhotoImage(file='del.png')
img_search=PhotoImage(file='search1.png')
img_search1=PhotoImage(file='search.png')

def clear():
    en.delete(0,END)
global product
def add():
    global product
    def clear1():
        en_no.delete(0,END)
        en_name.delete(0,END)
        en_price.delete(0,END)
        en_details.delete(0,END)
    b=Toplevel(a)
    b.geometry('600x400')
    b.configure(bg='white')
    l_head=Label(b,text='ADD PRODUCTS',bg='white',font=('Arial',30)).place(x=20,y=10)
    la_prno=Label(b,text='Product Number',bg='white',font=('Times New Roman',16)).place(x=20,y=90)
    la_prname=Label(b,text='Product Name',bg='white',font=('Times New Roman',16)).place(x=20,y=150)
    la_prprice=Label(b,text='Product Price',bg='white',font=('Times New Roman',16)).place(x=20,y=200)
    la_prdetails=Label(b,text='Product Detail',bg='white',font=('Times New Roman',16)).place(x=20,y=260)
    en_no=Entry(b,width=15,font=('arial',15),bd=0)
    en_name=Entry(b,width=15,font=('arial',15),bd=0)
    en_price=Entry(b,width=15,font=('arial',15),bd=0)
    en_details=Entry(b,width=15,font=('arial',15),bd=0)
    en_no.place(x=200,y=90)
    en_name.place(x=200,y=140)
    en_price.place(x=200,y=190)
    en_details.place(x=200,y=250)
    Frame(b,width=180,height=2,bg='yellow').place(x=200,y=116)
    Frame(b,width=180,height=2,bg='yellow').place(x=200,y=166)
    Frame(b,width=180,height=2,bg='yellow').place(x=200,y=216)
    Frame(b,width=180,height=2,bg='yellow').place(x=200,y=278)
    myshop=[]
    def process():
        no=Entry.get(en_no)
        name=Entry.get(en_name)
        price=Entry.get(en_price)
        details=Entry.get(en_details)
        pr_total=[no,name,price,details]
        myshop.append(pr_total)
        sql = "insert into products1 (no,name,price,details) values (%s,%s,%s,%s) "
        val = (no,name,price,details)
        cursor.execute(sql,val)  
        db.commit()
        print(myshop)
        clear1()
    btn_sub=Button(b,text='submit',bg='black',fg='white',activeforeground='black',activebackground='white',command=process)
    btn_sub.place(x=150,y=300)
def view():
    global myshop
    c=Toplevel(a)
    cursor.execute('select * from products1')
    val=cursor.fetchall()
    x=ttk.Treeview(c,selectmode='browse')
    x["columns"]=("1","2","3","4")
    x['show']='headings'
    x.column("1",width=200,anchor='c')
    x.column("2",width=200,anchor='c')
    x.column("3",width=200,anchor='c')
    x.column("4",width=200,anchor='c')
    x.heading("1",text="number")
    x.heading("2",text="name")
    x.heading("3",text="price")
    x.heading("4",text="details")
    for dt in val:
        x.insert('','end',values=(dt[0],dt[1],dt[2],dt[3]))
    x.pack()

def update():
    def clear_update():
        en_no_update.delete(0, END)
        en_name_update.delete(0, END)
        en_price_update.delete(0, END)
        en_details_update.delete(0, END)

    def fetch_data():
        product_no = en_no_update.get()
        cursor.execute('SELECT * FROM products1 WHERE no = {}'.format(product_no))
        product = cursor.fetchone()
        if product:
            en_name_update.insert(0, product[1])
            en_price_update.insert(0, product[2])
            en_details_update.insert(0, product[3])
        else:
            msg.showerror("Error", "Product not found")

    def update_data():
        product_no = en_no_update.get()
        product_name = en_name_update.get()
        product_price = en_price_update.get()
        product_details = en_details_update.get()
        cursor.execute('UPDATE products1 SET name = %s, price = %s, details = %s WHERE no = %s',
                       (product_name, product_price, product_details, product_no))
        db.commit()
        msg.showinfo("Success", "Product updated successfully")
        clear_update()

    update_window = Toplevel(a)
    update_window.geometry('600x400')
    update_window.configure(bg='white')
    Label(update_window, text='UPDATE PRODUCT', bg='white', font=('Arial', 30)).place(x=20, y=10)
    Label(update_window, text='Product Number', bg='white', font=('Times New Roman', 16)).place(x=20, y=90)
    Label(update_window, text='Product Name', bg='white', font=('Times New Roman', 16)).place(x=20, y=150)
    Label(update_window, text='Product Price', bg='white', font=('Times New Roman', 16)).place(x=20, y=200)
    Label(update_window, text='Product Detail', bg='white', font=('Times New Roman', 16)).place(x=20, y=260)
    en_no_update = Entry(update_window, width=15, font=('arial', 15), bd=0)
    en_name_update = Entry(update_window, width=15, font=('arial', 15), bd=0)
    en_price_update = Entry(update_window, width=15, font=('arial', 15), bd=0)
    en_details_update = Entry(update_window, width=15, font=('arial', 15), bd=0)
    en_no_update.place(x=200, y=90)
    en_name_update.place(x=200, y=140)
    en_price_update.place(x=200, y=190)
    en_details_update.place(x=200, y=250)
    Frame(update_window, width=180, height=2, bg='yellow').place(x=200, y=116)
    Frame(update_window, width=180, height=2, bg='yellow').place(x=200, y=166)
    Frame(update_window, width=180, height=2, bg='yellow').place(x=200, y=216)
    Frame(update_window, width=180, height=2, bg='yellow').place(x=200, y=278)

    btn_fetch = Button(update_window, text='Fetch', bg='black', fg='white', command=fetch_data)
    btn_fetch.place(x=350, y=85)

    btn_update = Button(update_window, text='Update', bg='black', fg='white', command=update_data)
    btn_update.place(x=250, y=300)

def delete():
    global product
    global en
    en1 = en.get()
    
    # Display confirmation messagebox
    confirm = msg.askokcancel("Confirmation", "Are you sure you want to delete this item?")
    if confirm:
        cursor.execute('select * from products1 where no = {}'.format(en1))
        deleted_item = cursor.fetchone()  # Fetch the item before deletion
        cursor.execute('delete from products1 where no = {}'.format(en1))
        db.commit()
        clear()

def search():
    global en  
    en_1 = en.get()  
    cursor.execute('select * from products1 where no = {}'.format(en_1))
    v = cursor.fetchall()
    clear()
    for i in v:
        print(i)
        msg.showinfo('answer', i)
    
img_width = img_new.width()
img_height = img_new.height()

btn_new = Button(a, image=img_new, bd=0, command=add)
btn_new.place(x=20, y=110, width=img_width, height=img_height)

btn_view = Button(a, image=img_view, bd=0, command=view)
btn_view.place(x=20, y=190, width=img_width, height=img_height)

btn_update = Button(a, image=img_update, bd=0, command=update)
btn_update.place(x=20, y=270, width=img_width, height=img_height)

btn_del = Button(a, image=img_del, bd=0, command=delete)
btn_del.place(x=25, y=350, width=img_width, height=img_height)

btn_search = Button(a, image=img_search, bd=0, command=search)
btn_search.place(x=25, y=430, width=img_width, height=img_height)

btn_search1 = Button(a, image=img_search1, bd=0, command=search)
btn_search1.place(x=840, y=60, width=img_width, height=img_height)

en=Entry(a,width=15,font=("arial",16),highlightthickness=5,bd=0,highlightcolor='red')
en.config(highlightbackground='skyblue',highlightcolor='#d61313')
en.place(x=650,y=60)
main_pic=Label(a,image=img_shop)
main_pic.place(x=200,y=100)
a.mainloop()

