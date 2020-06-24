import unittest
from client import sym

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = sym.SymClient()
        self.client.login('test_user', 'test_pwd')
        
    @unittest.skip('register pass')
    def test_register(self):
        self.client.register('test_company', 'test_user', 'test_pwd')

    @unittest.skip('login pass')
    def test_login(self):
        self.client.login('test_user', 'test_pwd')

    @unittest.skip('upload_data_label pass')
    def test_upload_data_label(self):
        schema_id = self.client.upload_data_label_schema('../openplatform/tools/test.toml')
        print(schema_id)

    @unittest.skip('test_request_buffer_data pass')
    def test_request_buffer_data(self):
        self.client.request_buffer_data(1273600184722538496, "2020-05-01", "2020-06-30", 0)

    @unittest.skip('test_push_data_label pass')
    def test_push_data_label(self):
        res = self.client.push_data_label(1275804353319559168, {"data":"a"})
        print(res)

    @unittest.skip('test_upload_model_label pass')
    def test_upload_model_label(self):
        res = self.client.upload_model_label_schema('../openplatform/tools/test.toml')
        print(res)

    @unittest.skip('test_request_data_label pass')
    def test_request_data_label(self):
        res = self.client.request_data_label(1275004877172531200, "2020-05-01", "2020-06-30", 0)
        print(res)

    @unittest.skip('test_request_model_label pass')
    def test_request_model_label(self):
        res = self.client.request_model_label(1275012792373637120, "2020-05-01", "2020-06-30", 0)
        print(res)

    def test_push_model_label(self):
        res = self.client.push_model_label( 1275012792373637120, {"test":"item"})
        print(res)

if __name__ == "__main__":
    unittest.main()