from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal Shelter in MongoDB"""
    def __init__(self, username, password):
        #init to connect to mongodb without auth
        #self.client = MongoClient('mongodb://localhost:47122')
        self.client = MongoClient('mongodb://' + username +":" + password + '@localhost:47122/AAC')
        #connect with auth
        self.database = self.client['AAC']
        
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True
        else: 
            raise Exception("Nothing to save because data parameter is really empty")
            
    def get_all(self, data):
        myCursor = self.database.animals.find(data, {'_id':False}) ## return a cursor with apointer to a list of results
        return myCursor
    
    def read(self, data):
        if data is None:
            return self.database.animals.find_one()
        else:
            return self.database.animals.find_one(data) ## returns only one document