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
        if isinstance(data,'dict'):
            self.table.insert_one(data)
        elif isinstance(data,'list'):
            self.table.insert_many(data)
        else:
            print('%s is illegal...')
        return


    def find(self,data,model=normal,field=None,regex=None):#待修改
        if model=="re" and regex!=None and field!=None:
            query = {field:{"$regex":regex}}
            return self.table.find(query)
        return self.table.find(data)
        

    def find(self,data):#待修改
        x = self.table.find(data)
        return    


    def delete(self,data):#待修改
        if isinstance(data,'dict'):
            self.table.delete_one(data)
        elif isinstance(data,'list'):
            self.table.delete_many(data)
        print('已删除%s条数据.'%x.deleted_count)
        return 
    
    def update(self,old,new):
        new_data = {'$set':new}
        x = self.table.update_many(old_data,new_data)
        print('已更新%s条数据.'%x.modified_count)
        return