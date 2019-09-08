from db_handler import *
from interface import *

a = AngajatDB("C:\Repos\FirstPython-Aplication\PythonApplication1\database\demodb.db")

i = Grapic("Yay", a)

i.fill_data(a.select_all_employees())

i.start()
