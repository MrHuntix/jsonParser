from tkinter import filedialog
import tkinter as tk
from jsonParser import Parser

root = tk.Tk()
root.withdraw()
file=filedialog.askopenfilename()
print('path: ',file)

p=Parser('eqn.json')

print("Expression from json:\n",p.get_infix(),'\n')

##p.print_prefix()

p.get_x()

