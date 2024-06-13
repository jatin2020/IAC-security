import unittest
from detect_clickops_events import identify_operation

class TestClickOps(unittest.TestCase):

    
    def test_clickops_read(self):
         #test to check if the json file is read operation
        json_data = "test_cases/json_files/read_operation_test.json"
        result = identify_operation(json_data)
        print ("Read ops :", result)
    
    def test_clickops_readclickops(self):
         #test to check if the json file is read operation
        json_data = "test_cases/json_files/read_clickops.json"
        result = identify_operation(json_data)
        print ("Read clickops :", result)
    
    def test_clickops_write(self):
         #test to check if the json file is read operation
        json_data = "test_cases/json_files/write_operation_test.json"
        result = identify_operation(json_data)
        print ("Write ops :", result)
    
    def test_clickops(self):
         #test to check if the json file is clickops
        json_data = "test_cases/json_files/clickops.json"
        result = identify_operation(json_data)
        print (result)
    
    def test_clickops_useragent(self):
         #test to check if the json file doesnot contain user agent 
        json_data = "test_cases/json_files/no_useragent_test.json"
        result = identify_operation(json_data)
        print (result)

if __name__ == "__main__":
    unittest.main()

