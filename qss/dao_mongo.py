import pymongo
import settings


class Client:
    def __init__(self, path):
        self.mongo = pymongo.MongoClient(path)
        self.db = self.mongo[settings.DB_NAME]
        self.table = self.db[settings.DB_TB_NAME]
    
    def rget(self):#待修改
        """get items randomly"""
        x = self.table.find()
        return next(x)

    def re(self,field,exp):#待修改
        x = self.table.find({field:{"$regex":exp}})
        return
    
    def insert(self,data):#待修改
        x = self.table.insert_many(data)
        return

    def find(self,data):#待修改
        x = self.table.find(data)
        return    

    def delete(self,data):#待修改
        x = self.table.delete_many(data)
        print('已删除%s条数据.'%x.deleted_count)
        return
