

import json
import os, re, itertools
MY_PATH = '/home/klobie/'

class Visitor:
    
    def __init__(self, full_name, age, date_of_visit, time_of_visit, comments, visitor_assistant, id=None):
        
        self.id = id
        self.full_name = full_name
        self.age = age 
        self.date_of_visit = date_of_visit
        self.time_of_visit = time_of_visit
        self.comments = comments
        self.visitor_assistant = visitor_assistant
        
    def generate_id(self):
        """generate an id, relative to the last recorded id"""       

        #search through a directory for all visitor objects
        files_in_directory = os.listdir(MY_PATH)
        visitor_id_list= []

        #find list of id numbers in files_in_directory
        for file_name in files_in_directory:
            if re.findall(r"((?<=visitor_)\d(?=\.json))", file_name): 
                pattern = re.findall(r"((?<=visitor_)\d(?=\.json))", file_name)
                visitor_id_list.append(pattern)
        
        #flatten visitor_id_list
        visitor_id = list(itertools.chain.from_iterable(visitor_id_list))
        
        #get the maximum number and add it to 1         
        last_recorded_id = max(visitor_id, key=lambda x:int(x))
        id = int(last_recorded_id) + 1 

        return id
                        
    def save(self):

        """"generates an id for the visiotor if there is no id and dumps the visitor as a json file"""
        
        self.id = self.id or self.generate_id()
        
        visitor_dictionary = {'full_name':self.full_name, 'age':self.age, 'date_of_visit':self.date_of_visit, 'time_of_visit':self.time_of_visit, 'comments':self.comments, 'visitor_assistant':self.visitor_assistant, 'id':self.id}
        
        with open(f"{MY_PATH}/visitor_{self.id}.json", "a+") as dumped_data_file:
            json.dump(visitor_dictionary, dumped_data_file)
        
                
    def load(self, id):           
                
        # search for json file in all directories in \"visitor_{some_number}.json\" format.
        # files_in_directory = os.listdir(MY_PATH) 
        visitor_file = (f'{MY_PATH}/visitor_{self.id}.json')
                        
        #open visitor file and load as a python object
        with open(visitor_file, 'r') as loaded_data_file:
            visitor_details = json.load(loaded_data_file)
            
        return Visitor(**visitor_details)
       
                
if __name__ == "__main__":
    
       
    Samantha = Visitor("Samantha Smith", 12, "12/4/2019", "12:45", "this is the umpteeth try", "Maxwell",1)
    
    Samantha.save()
    Mike = Visitor("Mike Smith", 32, "12/04/2018", "12:47", "Samantha's husband", "Maxwell")
    Mike.save()

    Samantha.age = 21
    Samantha.comments = 'hello nurse'
    Samantha.save()

    # Mike.load(2)
    # Mike.comments = "had a great time" 

    # print(Mike.save())
    
    
    


       

        




        
            
        

   


 


    








        
            

