from pymongo.mongo_client import MongoClient

class MongoDB_Python:
    def __init__(self):
        self.conn = MongoClient('localhost', 27017)
        self.db = self.conn.TestDB   
        self.cursor = self.db['teste_db.crud-db']
        
    def create(self, query={}):
        self.cursor.insert(query)
        
    def read(self, query={}):
        for value in self.cursor.find(query):
            print(value)
        
    def update(self, query_1={}, query_2={}):
        self.cursor.update(query_1, query_2)
    
    def delete(self):
        for i in self.cursor.find():
            self.cursor.remove(i)

if __name__ == '__main__':
    mongo = MongoDB_Python()

    for x in range(3):
        reg = {'_id':x, 'x':x, 'list':['first', 'second', 'third','fourth', 'fifth']}
        mongo.create(reg)
        
    print('Leia antes do update')
    mongo.read()
    
    mongo.update({'x':0, 'list':'first'}, {'$set':{'list.$':'primeiro'}})
    
    mongo.update({'x':1}, {"$addToSet":{'list':{'$each':['fifth', 'sixth', 'seventh']}}})

    mongo.update({'x':2}, {'$pull':{'list':'fifth'}})
    
    print('Leia depois do update')
    mongo.read()
    
    mongo.delete()