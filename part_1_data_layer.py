

import json
import os, re, glob
MY_PATH = '/home/klobie/'

class Visitor:
    
    def __init__(self, full_name, age, date_of_visit, time_of_visit, comments, visitor_assistant, id=None):
        
        self.full_name = full_name
        self.age = age 
        self.date_of_visit = date_of_visit
        self.time_of_visit = time_of_visit
        self.comments = comments
        self.visitor_assistant = visitor_assistant
        
    def generate_id(self):

        #search through a directory for all visitor objects
        files_in_directory = os.listdir(MY_PATH)
        #find maximum id numbers in files
        for files in files_in_directory:
            visitor_id = re.findall(r"((?<=visitor_)\d(?=\.json))", files) 
            last_id = max(visitor_id)
            id = last_id + 1
        
        return id 
        
    def save(self):
        """saves the visitor as a json file"""

        visitor_dictionary = {'full_name':self.full_name, 'age':self.age, 'date_of_visit':self.date_of_visit, 'Time of visit':self.time_of_visit, 'comments':self.comments, 'visitor_assistant':self.visitor_assistant}
        
        with open(f"{MY_PATH}/visitor_{id}.json", "w+") as dumped_data_file:
            visitor_details = json.dump(visitor_dictionary, dumped_data_file)

        return visitor_details
        

    def load(self, id):           
                
        # search for json file in all directories in \"visitor_{some_number}.json\" format.
        files = glob.glob(MY_PATH + f'/**/*{id}.json', recursive=True)
        visitor_file = [x for x in files if f'visitor_{id}.json' in x]
                        
        #open visitor file and load as a python object
        with open(visitor_file, 'r') as loaded_data_file:
            visitor_details = json.load(loaded_data_file)

        return Visitor(**visitor_details)
       
                
if __name__ == "__main__":
    
       
    Alice = Visitor("Alice Smith", 12, "12/4/2019", "12:45", "forgot her shoes", "Maxwell, 1")
    Alice.save()
    Mike = Visitor('Mike Smith', 32, "12/04/2018", "12:47", "Alice's husband", "Maxwell", 2)
    Mike.save()
    Alice.age = 21
    Alice.comments = 'hello nurse'
    print(Alice.save())
    Alice.age = 45
    Alice.save()

    Mike.load(2)
    Mike.comments = "had a great time" 
    Mike.save()
    
    
    


       

        




        
            
        

   


 


    








        
            


