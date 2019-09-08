from tkinter import *
from vscroll import *

class Grapic(object):
    def __init__(self, title, db_connection):
        self.__db = db_connection
        self.__root = Tk()
        self.__root.title(title)
        self.__root.geometry("800x600+100+100")
        self.__menubar = Menu(self.__root)
        self.__menubar.add_command(label="Add Emploee", command=self.__add_emploee)
        self.__menubar.add_command(label="Salaries -5%", command=self.__edit_salaries)
        self.__root.config(menu=self.__menubar)
        self.__table = Frame(self.__root, height = 200, width = 200,bg = "BLUE",borderwidth=22)
        self.__table.pack(side=TOP,padx=2,pady=2,fill=BOTH)
        self.__table_header = Frame(self.__table,height = 100, width = 100,bg = "GREEN",borderwidth=22)
        self.__table_header.pack(side=TOP,padx=5,pady=5,fill=BOTH)
        self.__table_rows = []
        self.__cnp_label = Label(self.__table_header, text='CNP').pack(side=LEFT,padx=30, pady=5)
        self.__nume_label = Label(self.__table_header, text='Nume').pack(side=LEFT,padx=50,pady=5)
        self.__salar_label = Label(self.__table_header, text='Salariu').pack(side=LEFT,padx=30,pady=5)
        self.__edit_label = Label(self.__table_header, text='Edit').pack(side=LEFT,padx=60,pady=5)
        self.__remove_label = Label(self.__table_header, text='Remove').pack(side=LEFT,padx=0,pady=5)
        self.__table_content = VerticalScrolledFrame(self.__table, height = 400, width = 200,bg = "BLUE",borderwidth=22)
        self.__table_content.pack(side=BOTTOM,fill=X)


    def __add_emploee(self):
        self.__add = Tk()
        self.__add.title("Adding emploee")
        self.__add.geometry("650x250+100+100")
        self.__add_table = Frame(self.__add, height = 200, width = 200,bg = "YELLOW",borderwidth=22)
        self.__add_table.pack(side=TOP,padx=2,pady=2,fill=BOTH)
        self.__add_table_header = Frame(self.__add_table, height = 40, width = 40,bg = "GREEN",borderwidth=22)
        self.__add_table_header.pack(side=TOP,padx=5,pady=5,fill=BOTH)
        self.__add_cnp_label = Label(self.__add_table_header, text='CNP')
        self.__add_cnp_label.pack(side=LEFT)
        self.__add_nume_label = Label(self.__add_table_header, text='Nume')
        self.__add_nume_label.pack(side=LEFT,padx=120,pady=5)
        self.__add_salar_label = Label(self.__add_table_header, text='Salariu')
        self.__add_salar_label.pack(side=LEFT,padx=0,pady=5)
        self.__add_emploee_data = Frame(self.__add_table, height = 40, width = 40,bg = "RED",borderwidth=22)
        self.__add_emploee_data.pack(side=BOTTOM,fill=X)
        self.__add_cnp = Entry(self.__add_emploee_data)
        self.__add_cnp.pack(padx=10,pady=10,side=LEFT)
        self.__add_nume = Entry(self.__add_emploee_data)
        self.__add_nume.pack(padx=10,pady=10,side=LEFT)
        self.__add_salar = Entry(self.__add_emploee_data)
        self.__add_salar.pack(padx=10,pady=10,side=LEFT)
        self.__add_btn = Button(self.__add_emploee_data, text='Add')
        self.__add_btn.configure(command=lambda button=self.__add_btn: self.__on_add(button))
        self.__add_btn.pack(side=LEFT,padx=30,pady=5)


    def __edit_salaries(self):
        for row in self.__table_rows:
            salar = round(float(row.children['!entry2'].get()), 2)
            salar -= salar*0.05  # 5% decrease
            salar = round(salar, 2)  # flaot with 2 decimals only
            cnp = row.children['!label'].cget('text')
            nume = row.children['!entry'].get()
            self.__db.update_emploee((cnp,nume,salar))
        # re-draw the table data
        for table_row in self.__table_rows:
            table_row.destroy()
        self.__table_rows = []
        self.fill_data(self.__db.select_all_employees())


    def fill_data(self, angajati):
        Idx = 0
        for angajat in angajati:
            self.__table_rows.append(Frame(self.__table_content, height = 40, width = 40,bg = "RED",borderwidth=22))
            self.__table_rows[Idx].pack(side=BOTTOM,fill=X,pady=1)
            cnp = Label(self.__table_rows[Idx], text=angajat[0])
            cnp.pack(padx=10,pady=10,side=LEFT)
            nume = Entry(self.__table_rows[Idx])
            nume.delete(0, 'end')
            nume.insert(0, angajat[1])
            nume.pack(padx=30,pady=10,side=LEFT)
            salar = Entry(self.__table_rows[Idx], textvariable=angajat[2])
            salar.pack(padx=10,pady=10,side=LEFT)
            salar.delete(0, 'end')
            salar.insert(0, angajat[2])
            update_btn = Button(self.__table_rows[Idx], text='Update')
            update_btn.configure(command=lambda button=update_btn: self.__on_update(button))
            update_btn.pack(side=LEFT,padx=5,pady=5)
            delete_btn = Button(self.__table_rows[Idx], text='Delete')
            delete_btn.configure(command=lambda button=delete_btn: self.__on_delete(button))
            delete_btn.pack(side=LEFT,padx=30,pady=5)
            Idx+=1


    def start(self):
        self.__root.mainloop()

    def __on_update(self, btn_instance):
        nume = btn_instance.master.children['!entry'].get()
        salar = btn_instance.master.children['!entry2'].get()
        cnp = btn_instance.master.children['!label'].cget('text')
        self.__db.update_emploee((cnp,nume,salar))

    def __on_delete(self, btn_instance):
        del_cnp = btn_instance.master.children['!label'].cget('text')
        self.__db.delete_emploee(del_cnp)
        # re-draw the table data
        for table_row in self.__table_rows:
            table_row.destroy()
        self.__table_rows = []
        self.fill_data(self.__db.select_all_employees())


    def __on_add(self, btn_instance):
        add_cnp = btn_instance.master.children['!entry'].get()
        add_nume = btn_instance.master.children['!entry2'].get()
        add_salar = btn_instance.master.children['!entry3'].get()
        self.__db.insert_emploee((add_cnp, add_nume, add_salar))
        btn_instance.master.master.master.destroy()   # close window
        # re-draw the table data
        for table_row in self.__table_rows:
            table_row.destroy()
        self.__table_rows = []
        self.fill_data(self.__db.select_all_employees())

#entry = Entry(root, width=10)
#entry.pack(side=TOP,padx=10,pady=10)
#
#def onok():
#    x, y = entry.get().split('x')
#    for row in range(int(y)):
#        for col in range(int(x)):
#            print((row, col))
#
#Button(root, text='OK', command=onok).pack(side=LEFT)
#Button(root, text='CLOSE').pack(side= RIGHT)


