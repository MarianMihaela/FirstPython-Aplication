from tkinter import *

class Grapic(object):
    def __init__(self, title):
        self.__root = Tk()
        self.__root.title(title)
        self.__root.geometry("800x600+100+100")
        self.__table_header = Frame(self.__root,height = 200, width = 200,bg = "GREEN",borderwidth=22)
        self.__table_header.pack(side=TOP,padx=5,pady=5,fill=BOTH)
        self.__table_rows = []
        self.__id_label = Label(self.__table_header, text='Id Angajat').pack(side=LEFT,padx=10,pady=10)
        self.__nume_label = Label(self.__table_header, text='Numne').pack(side=LEFT,padx=10,pady=10)
        self.__salar_label = Label(self.__table_header, text='Salariu').pack(side=LEFT,padx=10,pady=10)
        self.__edit_label = Label(self.__table_header, text='Edit').pack(side=LEFT,padx=10,pady=10)
        self.__remove_label = Label(self.__table_header, text='Remove').pack(side=LEFT,padx=10,pady=10)


    def fill_data(self, angajati):
        Idx = 0
        for angajat in angajati:
            if Idx > 0:
                pack_after = self.__table_rows[Idx-1]
            else:
                pack_after = self.__table_header
            self.__table_rows.append(Frame(self.__table_header,height = 100, width = 100,bg = "RED",borderwidth=22))
            self.__table_rows[Idx].pack(anchor=E,padx=5,pady=5,fill=X)
            id = Label(self.__table_rows[Idx], text=angajat[0])
            id.pack(padx=10,pady=10,side=LEFT)
            nume = Entry(self.__table_rows[Idx])
            nume.insert(0, angajat[1])
            nume.pack(padx=10,pady=10,side=LEFT)
            salar = Entry(self.__table_rows[Idx], textvariable=angajat[2])
            salar.pack(padx=10,pady=10,side=LEFT)
            salar.insert(0, angajat[2])
            Idx+=1

    def start(self):
        self.__root.mainloop()

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


