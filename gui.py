import sql
import tkinter as tk 
from tkinter import ttk
import time
### Window Config ###
root = tk.Tk()
root.title("Database")
root.geometry("400x600")
root.resizable(True, True)
#####################
def destroy():
    for child in root.winfo_children():
        child.destroy()
    
    #remove any grid weights
    for i in range(0, 3):
        root.rowconfigure(i, weight=0)
        root.columnconfigure(i, weight=0)

def create_db():

    def button(dbname):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.create_db(dbname)
        tk.Label(root, text="Database created successfully").grid(row=0, column=0)
        menu()
        ttk.Button(root, text="Back", command=menu).grid(row=1, column=1)

    destroy()

    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.ttk.Button(root, text="Create Database", command=lambda: button(dbname.get())).grid(row=1, column=1)
    
    menu()

def create_table():
    
    def button(dbname, table_name, structure):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.create_table(dbname, table_name, structure)
        tk.Label(root, text="Table created successfully").grid(row=0, column=0)
    
        menu()

    for child in root.winfo_children():
        child.destroy()

    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the structure: ").grid(row=2, column=0)
    structure = tk.Entry(root)
    structure.grid(row=2, column=1)
    tk.ttk.Button(root, text="Create Table", command=lambda: button(dbname.get(), table_name.get(), structure.get())).grid(row=4, column=1)
    
    menu()

def create_column():
    
    def button(dbname, table_name, column_name, column_type):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.create_column(dbname, table_name, column_name, column_type)
        tk.Label(root, text="Column created successfully").grid(row=0, column=0)
    
        menu()

    for child in root.winfo_children():
        child.destroy()

    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the name of the column: ").grid(row=2, column=0)
    column_name = tk.Entry(root)
    column_name.grid(row=2, column=1)
    tk.Label(root, text="Enter the column type: ").grid(row=3, column=0)
    column_type = tk.Entry(root)
    column_type.grid(row=3, column=1)
    tk.ttk.Button(root, text="Create Column", command=lambda: button(dbname.get(), table_name.get(), column_name.get(), column_type.get())).grid(row=4, column=1)
    
    menu()

def insert_data():
    
    def button(dbname , table_name, values):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.insert_data(dbname, table_name, values)
        tk.Label(root, text="Data inserted successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
     
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the values: ").grid(row=2, column=0)
    values = tk.Entry(root)
    values.grid(row=2, column=1)
    tk.ttk.Button(root, text="Insert Data", command=lambda: button(dbname.get(), table_name.get(), values.get())).grid(row=4, column=1)
    
    menu()

def update_data():
    
    def button(dbname, table_name, column_names, column_values, condition):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.update_data(dbname , table_name, column_names, column_values, condition)
        tk.Label(root, text="Data updated successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the values: ").grid(row=2, column=0)
    values = tk.Entry(root)
    values.grid(row=2, column=1)
    tk.Label(root, text="Enter the where clause: ").grid(row=3, column=0)
    where_clause = tk.Entry(root)
    where_clause.grid(row=3, column=1)
    tk.Label(root, text="Enter the column names: ").grid(row=4, column=0)
    column_names = tk.Entry(root)
    column_names.grid(row=4, column=1)
    tk.Label(root, text="Enter the column values: ").grid(row=5, column=0)
    column_values = tk.Entry(root)
    column_values.grid(row=5, column=1)
    tk.ttk.Button(root, text="Update Data", command=lambda: button(dbname.get(), table_name.get(), column_names.get(), column_values.get(), where_clause.get())).grid(row=4, column=1)
    
    menu()

def delete_data():
    
    def button(dbname, table_name, condition):
    
        for child in root.winfo_children():
            child.destroy()
        sql.delete_data(dbname, table_name, condition)
        tk.Label(root, text="Data deleted successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the where clause: ").grid(row=2, column=0)
    where_clause = tk.Entry(root)
    where_clause.grid(row=2, column=1)
    tk.ttk.Button(root, text="Delete Data", command=lambda: button(dbname.get(), table_name.get(), where_clause.get())).grid(row=4, column=1)
    
    menu()

def add_primary_key():
    
    def button(dbname, table_name, column_name):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.add_primary_key(dbname, table_name, column_name)
        tk.Label(root, text="Primary key added successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
     
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the name of the column: ").grid(row=2, column=0)
    column_name = tk.Entry(root)
    column_name.grid(row=2, column=1)
    tk.ttk.Button(root, text="Add Primary Key", command=lambda: button(dbname.get(), table_name.get(), column_name.get())).grid(row=4, column=1)
    
    menu()

def delete_primary_key():
    
    def button(dbname, table_name):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.delete_primary_key(dbname, table_name)
        tk.Label(root, text="Primary key deleted successfully").grid(row=0, column=0)
    
        menu()

    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.ttk.Button(root, text="Delete Primary Key", command=lambda: button(dbname.get(), table_name.get())).grid(row=4, column=1)
    
    menu()

def drop_db():
    
    def button(dbname):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.drop_db(dbname)
        tk.Label(root, text="Database dropped successfully").grid(row=0, column=0)
    
        menu()

    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.ttk.Button(root, text="Drop Database", command=lambda: button(dbname.get())).grid(row=4, column=1)
    
    menu()

def drop_table():
    
    def button(dbname, table_name):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.drop_table(dbname, table_name)
        tk.Label(root, text="Table dropped successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.ttk.Button(root, text="Drop Table", command=lambda: button(dbname.get(), table_name.get())).grid(row=4, column=1)
    
    menu()

def drop_column():
    
    def button(dbname, table_name, column_name):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.drop_column(dbname, table_name, column_name)
        tk.Label(root, text="Column dropped successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the name of the column: ").grid(row=2, column=0)
    column_name = tk.Entry(root)
    column_name.grid(row=2, column=1)
    tk.ttk.Button(root, text="Drop Column", command=lambda: button(dbname.get(), table_name.get(), column_name.get())).grid(row=4, column=1)
    
    menu()

def show_table():

    def button(dbname):
    
        for child in root.winfo_children():
            child.destroy()
    
        result = sql.show_table(dbname)

        tk.Label(root, text="Table: ").grid(row=0, column=0)
        result_box = tk.Text(root, height=len(result), width=50)
        result_box.grid(row=1, column=0)

        for i in range(len(result)):
            result_box.insert(tk.END, result[i])
            result_box.insert(tk.END, "\n")

        tk.Label(root, text="Table shown successfully").grid(row=len(result)+1, column=0)  
        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.ttk.Button(root, text="Show Table", command=lambda: button(dbname.get())).grid(row=4, column=1)

    menu()

def show_databases():
    
    for child in root.winfo_children():
        child.destroy()
    
    result = sql.show_databases()

    tk.Label(root, text="Databases: ").grid(row=0, column=0)
    result_box = tk.Text(root, height=len(result), width=50)
    result_box.grid(row=1, column=0)

    for i in range(len(result)):
        result_box.insert(tk.END, result[i])
        result_box.insert(tk.END, "\n")
    
    tk.Label(root, text="Databases displayed successfully").grid(row=len(result), column=0)

    menu()

def describe():
    
    def button(dbname, table_name):
    
        for child in root.winfo_children():
            child.destroy()
    
        result = sql.describe(dbname, table_name)

        tk.Label(root, text="Result: ").grid(row=0, column=0)
        result_box = tk.Text(root, height=len(result), width=50)
        result_box.grid(row=1, column=0)

        for i in range(len(result)):

            result_box.insert(tk.END, result[i])
            result_box.insert(tk.END, "\n")
        
        tk.Label(root, text="Table described successfully").grid(row=len(result)+1, column=0)

        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.ttk.Button(root, text="Describe Table", command=lambda: button(dbname.get(), table_name.get())).grid(row=4, column=1)
    
    menu()

def aggregate():
    
    def button(dbname, table_name, column_name, aggregate_function):
    
        for child in root.winfo_children():
            child.destroy()
    
        result = sql.aggregate(dbname, table_name, column_name, aggregate_function)

        tk.Label(root, text="Result: ").grid(row=0, column=0)
        result_box = tk.Text(root, height=len(result), width=50)
        result_box.grid(row=1, column=0)

        for i in range(len(result)):
            result_box.insert(tk.END, result[i])
            result_box.insert(tk.END, "\n")
        
        tk.Label(root, text="Aggregate performed successfully").grid(row=len(result)+1, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
     
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the name of the column: ").grid(row=2, column=0)
    column_name = tk.Entry(root)
    column_name.grid(row=2, column=1)
    tk.Label(root, text="Enter the aggregate function: ").grid(row=3, column=0)
    function = tk.Entry(root)
    function.grid(row=3, column=1)
    tk.ttk.Button(root, text="Aggregate", command=lambda: button(dbname.get(), table_name.get(), column_name.get(), function.get())).grid(row=4, column=1)
    
    menu()

def select():
    
    def button(dbname, table_name, column_names, value):
    
        for child in root.winfo_children():
            child.destroy()
    
        result = sql.select(dbname, table_name, column_names, value)

        tk.Label(root, text="Result: ").grid(row=0, column=0)
        result_box = tk.Text(root, height=len(result), width=50)
        result_box.grid(row=1, column=0)

        for i in range(len(result)):
            result_box.insert(tk.END, result[i])
            result_box.insert(tk.END, "\n")
        
        tk.Label(root, text="Select performed successfully").grid(row=len(result)+1, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.Label(root, text="Enter the name of the column: ").grid(row=2, column=0)
    column_name = tk.Entry(root)
    column_name.grid(row=2, column=1)
    tk.Label(root, text="Enter the where clause of the column: ").grid(row=3, column=0)
    value = tk.Entry(root)
    value.grid(row=3, column=1)
    tk.ttk.Button(root, text="Select", command=lambda: button(dbname.get(), table_name.get(), column_name.get(), value.get())).grid(row=4, column=1)
    
    menu()

def truncate_table():
    
    def button(dbname, table_name):
    
        for child in root.winfo_children():
            child.destroy()
    
        sql.truncate_table(dbname, table_name)
        tk.Label(root, text="Table truncated successfully").grid(row=0, column=0)
    
        menu()
    
    for child in root.winfo_children():
        child.destroy()
    
    tk.Label(root, text="Enter the name of the database: ").grid(row=0, column=0)
    dbname = tk.Entry(root)
    dbname.grid(row=0, column=1)
    tk.Label(root, text="Enter the name of the table: ").grid(row=1, column=0)
    table_name = tk.Entry(root)
    table_name.grid(row=1, column=1)
    tk.ttk.Button(root, text="Truncate Table", command=lambda: button(dbname.get(), table_name.get())).grid(row=4, column=1)
    
    menu()

def menu():

    menu = tk.Menu(root)
    
    root.config(menu=menu)
    
    subMenu = tk.Menu(menu)
    menu.add_cascade(label=" Create", menu=subMenu)
    subMenu.add_command(label="Database", command=create_db)
    subMenu.add_command(label="Table", command=create_table)
    subMenu.add_command(label="Column", command=create_column)
    
    subMenu = tk.Menu(menu)
    menu.add_cascade(label="Drop", menu=subMenu)
    subMenu.add_command(label="Database", command=drop_db)
    subMenu.add_command(label="Table", command=drop_table)
    subMenu.add_command(label="Column", command=drop_column)
    subMenu.add_command(label="Truncate", command=truncate_table)
    
    subMenu = tk.Menu(menu)
    menu.add_cascade(label="Query", menu=subMenu)
    subMenu.add_command(label="Aggregate", command= aggregate)
    subMenu.add_command(label="Select", command= select)
    
    subMenu = tk.Menu(menu)
    menu.add_cascade(label="Schema", menu=subMenu)
    subMenu.add_command(label="Show Tables", command= show_table)
    subMenu.add_command(label="Show Databases", command= show_databases)
    subMenu.add_command(label="Describe", command= describe)

    subMenu = tk.Menu(menu)
    menu.add_cascade(label="DML", menu=subMenu)
    subMenu.add_command(label="Add Primary Key", command= add_primary_key)
    subMenu.add_command(label="Delete Primary Key", command= delete_primary_key)
    subMenu.add_command(label="Insert", command= insert_data)
    subMenu.add_command(label="Update", command= update_data)
    subMenu.add_command(label="Delete", command= delete_data)

    subMenu = tk.Menu(menu)
    menu.add_cascade(label="Exit", menu=subMenu)
    subMenu.add_command(label="Exit", command=root.quit)

    return menu

def main():
    #create tiles for each submenu by dividing the screen into 2x3 grid
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    #create a frame for each tile
    frame1 = tk.Frame(root, bg="red")
    frame1.grid(row=0, column=0, sticky="nsew")
    frame2 = tk.Frame(root, bg="blue")
    frame2.grid(row=0, column=1, sticky="nsew")
    frame3 = tk.Frame(root, bg="green")
    frame3.grid(row=0, column=2, sticky="nsew")
    frame4 = tk.Frame(root, bg="yellow")
    frame4.grid(row=1, column=0, sticky="nsew")
    frame5 = tk.Frame(root, bg="orange")
    frame5.grid(row=1, column=1, sticky="nsew")
    frame6 = tk.Frame(root, bg="purple")
    frame6.grid(row=1, column=2, sticky="nsew")

    #create a label for each frame
    label1 = tk.Label(frame1, text="Create", bg="red")
    label1.pack(fill="both", expand=True)
    label2 = tk.Label(frame2, text="Drop", bg="blue")
    label2.pack(fill="both", expand=True)
    label3 = tk.Label(frame3, text="Query", bg="green")
    label3.pack(fill="both", expand=True)
    label4 = tk.Label(frame4, text="Schema", bg="yellow")
    label4.pack(fill="both", expand=True)
    label5 = tk.Label(frame5, text="DML", bg="orange")
    label5.pack(fill="both", expand=True)
    label6 = tk.Label(frame6, text="Exit", bg="purple")
    label6.pack(fill="both", expand=True)

    #create a button for each label
    button1 = tk.ttk.Button(label1, text="Database", command=create_db)
    button1.pack(fill="both", expand=True)
    button2 = tk.ttk.Button(label1, text="Table", command=create_table)
    button2.pack(fill="both", expand=True)
    button3 = tk.ttk.Button(label1, text="Column", command=create_column)
    button3.pack(fill="both", expand=True)

    button4 = tk.ttk.Button(label2, text="Database", command=drop_db)
    button4.pack(fill="both", expand=True)
    button5 = tk.ttk.Button(label2, text="Table", command=drop_table)
    button5.pack(fill="both", expand=True)
    button6 = tk.ttk.Button(label2, text="Column", command=drop_column)
    button6.pack(fill="both", expand=True)
    button7 = tk.ttk.Button(label2, text="Truncate", command=truncate_table)
    button7.pack(fill="both", expand=True)

    button8 = tk.ttk.Button(label3, text="Aggregate", command=aggregate)
    button8.pack(fill="both", expand=True)
    button9 = tk.ttk.Button(label3, text="Select", command=select)
    button9.pack(fill="both", expand=True)

    button10 = tk.ttk.Button(label4, text="Show Tables", command=show_table)
    button10.pack(fill="both", expand=True)
    button11 = tk.ttk.Button(label4, text="Show Databases", command=show_databases)
    button11.pack(fill="both", expand=True)
    button12 = tk.ttk.Button(label4, text="Describe", command=describe)
    button12.pack(fill="both", expand=True)

    button13 = tk.ttk.Button(label5, text="Add Primary Key", command=add_primary_key)
    button13.pack(fill="both", expand=True)
    button14 = tk.ttk.Button(label5, text="Delete Primary Key", command=delete_primary_key)
    button14.pack(fill="both", expand=True)
    button15 = tk.ttk.Button(label5, text="Insert", command=insert_data)
    button15.pack(fill="both", expand=True)
    button16 = tk.ttk.Button(label5, text="Update", command=update_data)
    button16.pack(fill="both", expand=True)
    button17 = tk.ttk.Button(label5, text="Delete", command=delete_data)
    button17.pack(fill="both", expand=True)

    button18 = tk.ttk.Button(label6, text="Exit", command=root.quit)
    button18.pack(fill="both", expand=True)

    return main

menu()
main()
root.mainloop()
