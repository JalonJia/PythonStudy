"""
TODO: 操作 Excel
"""

from tkinter import Tk
from time import sleep
from tkinter import messagebox
#from TkMessageBox import showwarning #Python2 
import win32com

warn = lambda app: messagebox(app, '退出？')
RANGE = range(3, 8)

def excel():
    app = 'excel'
    xl = win32com.client.DispatchEx('%s.Application' % app)
    ss = xl.Workbooks.Add()
    sh = ss.ActiveSheet
    xl.Visible = True
    sleep(1)
    
    sh.Cells(1, 1).Value = 'Python-to-%s Demo' % app
    sleep(1)
    
    for i in RANGE:
        sh.Cells(i, 1).Value = 'Line %d' % i
        sleep(1)
    sh.Cells(i+2, 1).Value = 'Finished!'
    
    warn(app)
    ss.Close(False)
    xl.Application.quit()
    
if __name__ == '__main__':
    Tk().withdraw()
    excel()
    
    
    