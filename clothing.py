import sqlite3 
import tkinter as tk


root=tk.Tk()
root.title('Clothing advisor')
root.geometry('400x600')

conn=sqlite3.connect('clothing.db')

cur=conn.cursor()


def delete():
    conn=sqlite3.connect('clothing.db')
    cur=conn.cursor()  

    cur.execute('DELETE FROM clothing WHERE oid=')

    conn.commit()
    conn.close()

def submit():
    conn=sqlite3.connect('clothing.db')
    cur=conn.cursor()

    cur.execute("""INSERT INTO clothing VALUES (:date,:temperature,:wind,:rain,:sun,:trousers,:shirt,:jacket,:shoes,:hat)""",
            {
                'date':date.get(),
                'temperature':temperature.get(),
                'wind':wind.get(),
                'rain':rain.get(),
                'sun':sun.get(),
                'trousers':trousers.get(),
                'shirt':shirt.get(),
                'jacket':jacket.get(),
                'shoes':shoes.get(),
                'hat':hat.get()
            })

    conn.commit()
    conn.close()
    
    
    date.delete(0,tk.END)
    temperature.delete(0,tk.END)
    wind.delete(0,tk.END)
    rain.delete(0,tk.END)
    sun.delete(0,tk.END)
    trousers.delete(0,tk.END)
    shirt.delete(0,tk.END)
    jacket.delete(0,tk.END)
    shoes.delete(0,tk.END)
    hat.delete(0,tk.END)


def query():
    conn=sqlite3.connect('clothing.db')
    cur=conn.cursor()
    #Select all and Index/Key      
    cur.execute('SELECT *,oid FROM clothing')
    records=cur.fetchall()
    print_records=''
    for record in records:
        print_records+=str(record[0]) + ', ' +str(record[1]) + ', ' +str(record[2]) + '\t\t' +str(record[10]) + '\n'

    query_label=tk.Label(root, text=print_records)
    query_label.grid(row=16,column=0,columnspan=2)
    conn.commit()
    conn.close()

'''
cur.execute("""CREATE TABLE clothing (
    date text,
    temperature integer,
    wind text,
    rain integer,
    sun integer,
    trousers text,
    shirt text,
    jacket text,
    shoes text, 
    hat integer)""") 
'''

date=tk.Entry(root, width=30)
date.grid(row=0,column=1,padx=20,pady=(10,0))

temperature=tk.Entry(root, width=30)
temperature.grid(row=1,column=1)

wind=tk.Entry(root, width=30)
wind.grid(row=2,column=1)

rain=tk.Entry(root, width=30)
rain.grid(row=3,column=1)

sun=tk.Entry(root, width=30)
sun.grid(row=4,column=1)

trousers=tk.Entry(root, width=30)
trousers.grid(row=5,column=1)

shirt=tk.Entry(root, width=30)
shirt.grid(row=6,column=1)

jacket=tk.Entry(root, width=30)
jacket.grid(row=7,column=1)

shoes=tk.Entry(root, width=30)
shoes.grid(row=8,column=1)

hat=tk.Entry(root, width=30)
hat.grid(row=9,column=1)

delete_box=tk.Entry(root, width=30)
delete_box.grid(row=13,column=1,pady=5)


date_label=tk.Label(root,text='Date')
date_label.grid(row=0,column=0,pady=(10,0))

temp_label=tk.Label(root,text='Temperature')
temp_label.grid(row=1,column=0)

wind_label=tk.Label(root,text='Wind')
wind_label.grid(row=2,column=0)

rain_label=tk.Label(root,text='Rain')
rain_label.grid(row=3,column=0)

sun_label=tk.Label(root,text='Sun')
sun_label.grid(row=4,column=0)

trousers_label=tk.Label(root,text='Trousers')
trousers_label.grid(row=5,column=0)

shirt_label=tk.Label(root,text='Shirt')
shirt_label.grid(row=6,column=0)

jacket_label=tk.Label(root,text='Jacket')
jacket_label.grid(row=7,column=0)

shoes_label=tk.Label(root,text='Shoes')
shoes_label.grid(row=8,column=0)

hat_label=tk.Label(root,text='Hat')
hat_label.grid(row=9,column=0)

delete_box_label=tk.Label(root,text='Select Key')
delete_box_label.grid(row=13,column=0,pady=5)

sub_button=tk.Button(root,text='Add Conditions To Database',command=submit)
sub_button.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=107)

query_button=tk.Button(root,text='Clothing',command=query)
query_button.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=157)

delete_button=tk.Button(root,text='Delete Selected Data',command=delete)
delete_button.grid(row=15,column=0,columnspan=2,pady=10,padx=10,ipadx=125)

conn.commit()


conn.close()

root.mainloop()