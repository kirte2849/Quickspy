import pymongo
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
class Functions(object):

    def __init__(self,path):
        self.mongo = pymongo.MongoClient(path)
        self.db = None
        self.col = None

#=============================[数据库操作]=====================================#
    def load_db_names(self):#加载数据库名称
        return self.mongo.list_database_names()

    def create_db(self,db_list):#创建数据库
        try:
            db_name = askstring('','你想要创建的数据库的名字:')
            db = self.mongo[db_name]
            col = db['None']
            col.insert_one({'None':'None'})
            messagebox.showinfo('成功','成功创建数据库"%s"'%db_name)
            db_list.insert(0,db_name)
        except Exception as e:
            messagebox.showerror('Error',e)

    def delete_db(self,db_list,col_list):#删除数据库
        try:
            db_name = db_list.get('active')
            boolvalue = messagebox.askokcancel('警告','是否删除数据库%s,这样做会失去宝贵的数据'%db_name)
            print(boolvalue)
            if boolvalue:
                self.mongo.drop_database(db_name)
                db_list.delete(db_list.index('active'))
                messagebox.showinfo('删除成功','Database %s 已删除'%db_name)
                col_list.delete(0,last='end')
        except Exception as e:
            messagebox.showerror('Error',e)
            
#=============================[集合操作]=======================================#
    def load_col_names(self,db_list):#加载集合名称
        db = self.mongo[db_list.get('active')]
        return db.list_collection_names()

    def create_col(self,db_list,col_list):#创建集合
        try:
            db = self.mongo[db_list.get('active')]
            col_name = askstring('','你想要创建的集合的名字:')
            col = db[col_name]
            col.insert_one({'None':'None'})
            messagebox.showinfo('成功','成功创建集合"%s"'%col_name)
            col_list.insert(0,col_name)
        except Exception as e:
            messagebox.showerror('Error',e)

    def delete_col(self,db_list,col_list):#删除集合
        try:
            db_name = db_list.get('active')
            col_name = col_list.get('active')
            boolvalue = messagebox.askokcancel('警告','是否删除集合%s,这样做会失去宝贵的数据'%col_name)
            print(boolvalue)
            if boolvalue:
                self.mongo[db_name][col_name].drop()
                col_list.delete(col_list.index('active'))
                messagebox.showinfo('删除成功','集合 %s 已删除'%col_name)
        except Exception as e:
            messagebox.showerror('Error',e)
#=============================[数据操作]=======================================#
    def load_data(self,db_list,col_list,data_text):#读取数据
        db=self.mongo[db_list.get('active')]
        col_name = col_list.get('active')
        if len(col_name) == 0:
            return
        col=db[col_list.get('active')]
        data_text.delete(1.0,'end')
        for data in col.find():
            data_text.insert('end',data)
            data_text.insert('end','\n')

    def delete(self,col):#删除数据
        pass

    def commit(self,input_text,data_text,db_list,col_list):#写入数据
        datas = input_text.get(1.0,'end')
        print(datas)
        print(type(datas))
        if datas=='\n':
            messagebox.showerror('Error','输入不能为空')
            return
        db=self.mongo[db_list.get('active')]
        col=db[col_list.get('active')]
        data=[]
        try:
            for i in datas.split('\n'):
                kv = i.split(':')
                if kv != ['']:
                    temp = kv[0],kv[1]
                    data.append(temp)
            col.insert_one(dict(data))
            data_text.insert('end',dict(data))
            self.revoke(input_text)
            self.load_data(db_list,col_list,data_text)
        except IndexError:
            messagebox.showerror('Error','输入不合法,请按照例子输入')
        except Exception as e:
            messagebox.showerror('Error',e)            

    def revoke(self,input_text):
        input_text.delete(1.0,'end')

#=============================[其他功能]=======================================#
    def get_help(self):#打开帮助文档
        pass
