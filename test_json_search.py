# Fill the Python code in this file
import unittest
from recursive_json_search import *
from test_data import *
class json_search_test(unittest.TestCase):
    '''test module to test search function in
    `recursive_json_search.py`'''
    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([]!=json_search(key1,data))
    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([]==json_search(key2,data))
    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(json_search(key1,data),list)
    def test_rbac_enforcement_operator_cannot_read_apikey(self):
   	 result = json_search("apiKey", data, role="operator")
   	 self.assertEqual([], result)
    def test_least_privilege_viewer_cannot_read_ip_address(self):
    	result = json_search("managementIpAddress", data, role="viewer")
    	self.assertEqual([], result)
    def test_default_deny_none_or_unknown_role(self):
    	result_none = json_search("apiKey", data)
    	result_unknown = json_search("issueSummary", data, role="guest")
    	self.assertEqual([], result_none)
    	self.assertEqual([], result_unknown)
if __name__ == '__main__':
    unittest.main()
