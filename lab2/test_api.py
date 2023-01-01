import pip._vendor.requests as requests
from types import NoneType
from models.directory import Directory 

class TestAPI:
    parent_dir = Directory('root', 100)
    inner_dir = Directory('inner_dir', 50, parent_dir)

    #directory
    def test_read_dir(self):
        response = requests.get("http://localhost:5000/directory?name=root")
        assert response.status_code == 201
        assert response.json().get('message') == 'Directory was read successfully.'
        assert response.json().get('directory').get('DIR_MAX_ELEMS') == 100
        assert response.json().get('directory').get('count_elems') == 0 
        assert type(eval((response.json().get('directory').get('parent')))) is NoneType 
    
    def test_create_dir(self):
        response = requests.post("http://localhost:5000/directory?parent=root&name=child&max_elems=8")
        assert response.status_code == 201
        assert response.json().get('message') == 'Directory created successfully.'
        assert response.json().get('directory').get('DIR_MAX_ELEMS') == 8
        assert response.json().get('directory').get('count_elems') == 0 
        assert not type(response.json().get('directory').get('parent')) is NoneType 
        response = requests.post("http://localhost:5000/directory?parent=root&name=child&max_elems=8")
        assert response.status_code == 400
        assert response.json().get('message') == 'Directory already exists.'

    def test_move_dir(self):
        response = requests.patch("http://localhost:5000/directory?name=child&parent=root")
        assert response.status_code == 201
        assert response.json().get('message') == 'Directory moved successfully.'
        assert response.json().get('directory').get('parent') == "root"

    def test_delete_dir(self):
        response = requests.delete("http://localhost:5000/directory&name=child")
        assert response.status_code == 201
        assert response.json().get('message') == 'Directory deleted successfully.'
        response = requests.delete("http://localhost:5000/directory?name=child")
        assert response.status_code == 400
        assert response.json().get('message') == 'Directory was not deleted.'
    
    #buffer file
    def test_create_buf_file(self):
        response = requests.post("http://localhost:5000/bufferfile?parent=root&max_size=100&name=bufferfile")
        assert response.status_code == 201
        assert response.json().get('message') == 'File created successfully.'
        assert isinstance(response.json().get('file').get('info'), list)
        assert response.json().get('file').get('MAX_BUF_FILE_SIZE') == 100
        assert not type(response.json().get('file').get('parent')) is NoneType 
        response = requests.post("http://localhost:5000/bufferfile?parent=root&max_size=100&name=bufferfile")
        assert response.status_code == 400
        assert response.json().get('message') == 'File already exists.'

    def test_read_buf_file(self):
        response = requests.get("http://localhost:5000/bufferfile&name=bufferfile")
        assert response.status_code == 201
        assert response.json().get('message') == 'File was read successfully.'
        assert isinstance(response.json().get('file').get('info'), list)
        assert response.json().get('file').get('MAX_BUF_FILE_SIZE') == 100
        assert type(response.json().get('file').get('parent')) is str 

    def test_move_buf_file(self):
        response = requests.patch("http://localhost:5000/bufferfile?parent=root&name=bufferfile")
        assert response.status_code == 201
        assert isinstance(response.json().get('file').get('info'), list)
        assert response.json().get('file').get('MAX_BUF_FILE_SIZE') == 100
        assert response.json().get('file').get('parents') == "root"

    def test_push_buf_file(self):
        response = requests.patch("http://localhost:5000/bufferfile?name=bufferfile&append=test_text")
        assert response.status_code == 201
        assert response.json().get('message') == 'Line added successfully.'

    def test_consume_buf_file(self):
        response = requests.patch("http://localhost:5000/bufferfile?name=bufferfile&consume=true")
        assert response.status_code == 201
        assert response.json().get('message') == 'Line consumed successfully.'

    def test_delete_buf_file(self):
        response = requests.delete("http://localhost:5000/bufferfile?name=bufferfile")
        assert response.status_code == 201
        assert response.json().get('message') == 'File deleted successfully.'
        response = requests.delete("http://localhost:5000/bufferfile?name=bufferfile")
        assert response.status_code == 400
        assert response.json().get('message') == 'File was not deleted.'

    #binary file
    def test_create_bin_file(self):
        response = requests.post("http://localhost:5000/binaryfile?name=binaryfile&parent=root&info=test")
        assert response.status_code == 201
        assert response.json().get('message') == 'File created successfully.'
        assert response.json().get('file').get('info') == 'test' 
        assert not type(response.json().get('file').get('parent')) is NoneType 
        response = requests.post("http://localhost:5000/binaryfile?name=binaryfile&parent=root&info=test")
        assert response.status_code == 400
        assert response.json().get('message') == 'File already exists.'

    def test_read_bin_file(self):
        response = requests.get("http://localhost:5000/binaryfile?name=binaryfile")
        assert response.status_code == 201
        assert response.json().get('message') == 'File was read successfully.'
        assert response.json().get('file').get('info') == 'test' 
        assert type(response.json().get('file').get('parent')) is str 

    def test_move_bin_file(self):
        response = requests.patch("http://localhost:5000/binaryfile?name=binaryfile&parent=root")
        assert response.status_code == 201
        assert response.json().get('message') == 'File moved successfully.'
        assert response.json().get('file').get('parent') == "root"

    def test_delete_bin_file(self):
        response = requests.delete("http://localhost:5000/binaryfile?name=binaryfile")
        assert response.status_code == 201
        assert response.json().get('message') == 'File deleted successfully.'
        response = requests.delete("http://localhost:5000/binaryfile?name=binaryfile")
        assert response.status_code == 400
        assert response.json().get('message') == 'File was not deleted.'

    #log text file
    def test_create_log_text_file(self):
        response = requests.post("http://localhost:5000/logtextfile?name=logtextfile&parent=root&info=test")
        assert response.status_code == 201
        assert response.json().get('message') == 'File created successfully.'
        assert response.json().get('file').get('info') == 'test' 
        assert not type(response.json().get('file').get('parent')) is NoneType 
        response = requests.post("http://localhost:5000/logtextfile?name=logtextfile&parent=root&info=test")
        assert response.status_code == 400
        assert response.json().get('message') == 'File already exists.'

    def test_read_log_text_file(self):
        response = requests.get("http://localhost:5000/logtextfile?name=logtextfile")
        assert response.status_code == 201
        assert response.json().get('message') == 'File was read successfully.'
        assert response.json().get('file').get('info') == 'test' 
        assert type(response.json().get('file').get('parent')) is str 

    def test_move_log_text_file(self):
        response = requests.patch("http://localhost:5000/logtextfile?name=logtextfile&parent=root")
        assert response.status_code == 201
        assert response.json().get('message') == 'File moved successfully.'
        assert response.json().get('file').get('parent') == "root"

    def test_append_log_text_file(self):
        response = requests.patch("http://localhost:5000/logtextfile?name=logtextfile&append=test1")
        assert response.status_code == 201
        assert response.json().get('message') == 'Line added successfully.'

    def test_delete_log_text_file(self):
        response = requests.delete("http://localhost:5000/logtextfile?name=logtextfile")
        assert response.status_code == 200
        assert response.json().get('message') == 'File deleted successfully.'
        response = requests.delete("http://localhost:5000/logtextfile?name=logtextfile")
        assert response.status_code == 400
        assert response.json().get('message') == 'File was not deleted.'