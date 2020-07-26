from gui_settings import Settings
from functions import Functions as Func
from tkinter import *


class MongoDB_GUI(object):

    def __init__(self,root):
        self.root = root
        self.func = Func(Settings.MongoDB_Path)

    def set_root_window(self):
        self.root.title(Settings.root_window_Title)
        self.root.geometry(Settings.root_window_Size)
        self.root["bg"] = Settings.root_window_BackgroundColor

    def set_menu(self):
        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar,tearoff=0)
        self.helpmenu = Menu(self.menubar,tearoff=0)

        self.filemenu.add_command(label='Exit',command=self.root.quit)
        self.helpmenu.add_command(label='For Help',command=self.func.get_help)
        #待添加
        self.menubar.add_cascade(label='File',menu=self.filemenu)
        self.menubar.add_cascade(label='帮助',menu=self.helpmenu)
        self.root.config(menu=self.menubar)

    def set_text(self):
        self.input_text = Text(self.root,width=60,height=18,undo=True)
        self.data_text = Text(self.root,height=43)#,state='disabled'

        self.input_text.place(x=0,y=298,anchor='nw')
        self.data_text.place(x=430,y=25,anchor='nw')

    def set_label(self):
        self.db_label = Label(self.root,text='数据库',bg='white',font=('Arial',12),)
        self.col_label = Label(self.root,text='集合',bg='white',font=('Arial',12))
        self.data_label = Label(self.root,text='数据',bg='white',font=('Arial',12))
        self.input_label = Label(self.root,text='在这里输入:',bg='white',font=('Arial',15))
        self.example_label = Label(self.root,text='例子:name:LiHua\nage:18',bg='white',font=('Arial',10))

        self.db_label.place(x=30,y=0,anchor='nw')
        self.col_label.place(x=180,y=0,anchor='nw')
        self.data_label.place(x=700,y=0,anchor='nw')
        self.input_label.place(x=0,y=268,anchor='nw')
        self.example_label.place(x=320,y=257,anchor='nw')
        
    def set_listbox(self):
        self.db_list = Listbox(self.root)
        self.col_list = Listbox(self.root)
        self.load_db_list()
        self.load_col_list()

        self.db_list.bind('<Double-Button-1>',lambda e:self.load_col_list())
        self.col_list.bind('<Double-Button-1>',lambda e:self.func.load_data(self.db_list,self.col_list,self.data_text))

    def load_db_list(self):
        for db_name in self.func.load_db_names():
            self.db_list.insert(0,db_name)

        self.db_list.place(x=0,y=25,anchor='nw')

    def load_col_list(self):
        self.col_list.delete(first=0,last='end')
        for col in self.func.load_col_names(self.db_list):
            self.col_list.insert(0,col)

        self.col_list.place(x=150,y=25,anchor='nw')

    def set_button(self):
        self.b_create_db = Button(self.root,width=15,height=1,text='创建数据库',command=lambda:self.func.create_db(self.db_list))
        self.b_delete_db = Button(self.root,width=15,height=1,text='删除数据库',command=lambda:self.func.delete_db(self.db_list,self.col_list))
        self.b_create_col = Button(self.root,width=15,height=1,text='创建集合',command=lambda:self.func.create_col(self.db_list,self.col_list))
        self.b_delete_col = Button(self.root,width=15,height=1,text='删除集合',command=lambda:self.func.delete_col(self.db_list,self.col_list))
        self.b_commit_data = Button(self.root,width=25,height=2,text='提交',command=lambda:self.func.commit(self.input_text,self.data_text,self.db_list,self.col_list))
        self.b_delete_data = Button(self.root,width=25,height=2,text='撤销',command=lambda:self.func.revoke(self.input_text))

        self.b_create_db.place(x=300,y=25,anchor='nw')
        self.b_delete_db.place(x=300,y=70,anchor='nw')
        self.b_create_col.place(x=300,y=135,anchor='nw')
        self.b_delete_col.place(x=300,y=180,anchor='nw')
        self.b_commit_data.place(x=5,y=537,anchor='nw')
        self.b_delete_data.place(x=239,y=537,anchor='nw')
        
    def set_all(self):
        self.set_root_window()
        self.set_menu()
        self.set_text()
        self.set_label()
        self.set_listbox()
        self.set_button()

if __name__ == '__main__':
    root = Tk()
    GUI = MongoDB_GUI(root)
    GUI.set_all()
    root.mainloop()
        
