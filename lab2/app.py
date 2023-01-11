from flask import Flask, request, jsonify
from models.directory import Directory
from models.binary_file import BinaryFile
from models.log_text_file import LogTextFile
from models.buffer_file import BufferFile

app = Flask(__name__)

root = Directory('root', 100)
deleted_list = []

@app.route('/directory', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def directory():
   if request.method == 'POST':
      if any(x.name == request.args.get('name') for x in root.list) or request.args.get('name') == 'root':
         return jsonify({
         "message": "Directory already exists.",
      }), 400
      dir = Directory(request.args.get('name'), request.args.get('max_elems'), root)
      return jsonify({
         "message": "Directory created successfully.",
         "directory": {
            "parent": str(dir.parent),
            "name": str(dir.name),
            "DIR_MAX_ELEMS": int(dir.DIR_MAX_ELEMS),            
            "count_elems": int(dir.count_elems),
            "list": str(dir.list)     
         }
      }), 201
      
   elif request.method == 'GET':
      if any(dir.name == request.args.get('name') for dir in root.list) or request.args.get('name') == 'root':
         if request.args.get('name') == 'root':
            dir = root
         else:
            dir = next(x for x in root.list if x.name == request.args.get('name'))
         return jsonify({
         "message": "Directory was read successfully.",
         "directory": {
            "parent": str(dir.parent),
            "name": str(dir.name),
            "DIR_MAX_ELEMS": int(dir.DIR_MAX_ELEMS),            
            "count_elems": int(dir.count_elems),
            "list": str(dir.list)  
         }
      }), 200
      return jsonify({
         "message": "Directory doesn't exist.",
         }), 400

   elif request.method == 'PATCH':
      if any(dir.name == request.args.get('name') for dir in root.list):
         dir = next(x for x in root.list if x.name == request.args.get('name'))
         dir.move(root)
         return jsonify({
         "message": "Directory moved successfully.",
         "directory": {
            "parent": str(dir.parent.name),
            "name": str(dir.name),
            "DIR_MAX_ELEMS": int(dir.DIR_MAX_ELEMS),            
            "count_elems": int(dir.count_elems),
            "list": str(dir.list)    
         }
      }), 200
      return jsonify({
         "message": "Directory doesn't exist.",
         }), 400 

   else:
      if request.args.get('name') not in deleted_list and any(dir.name == request.args.get('name') for dir in root.list):
         dir = next(x for x in root.list if x.name == request.args.get('name'))
         del dir
         deleted_list.append(request.args.get('name'))
         return jsonify({
         "message": "Directory deleted successfully.",
         }), 200
      return jsonify({
         "message": "Directory was not deleted.",
         }), 400


@app.route('/binaryfile', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def binaryfile():
   if request.method == 'POST':
      if any(x.name == request.args.get('name') for x in root.list):
         return jsonify({
         "message": "File already exists.",
      }), 400
      file = BinaryFile(root, request.args.get('name'), request.args.get('info'))
      return jsonify({
         "message": "File created successfully.",
         "file": {
            "parent": str(file.parent.name),
            "name": str(file.name),
            "info": str(file.info)   
         }
      }), 201

   elif request.method == 'GET':
      if any(file.name == request.args.get('name') for file in root.list):
         file = next(x for x in root.list if x.name == request.args.get('name'))
         return jsonify({
         "message": "File was read successfully.",
         "file": {
            "parent": str(file.parent.name),
            "name": str(file.name),
            "info": str(file.info)    
         }
      }), 200
      return jsonify({
         "message": "File doesn't exist.",
         }), 400

   elif request.method == 'PATCH':
      if any(file.name == request.args.get('name') for file in root.list):
         file = next(x for x in root.list if x.name == request.args.get('name'))
         file.move(root)
         return jsonify({
         "message": "File moved successfully.",
         "file": {
            "parent": str(file.parent.name),
            "name": str(file.name),
            "info": str(file.info)     
         }
      }), 200
      return jsonify({
         "message": "File doesn't exist.",
         }), 400 

   else:
      if request.args.get('name') not in deleted_list and any(file.name == request.args.get('name') for file in root.list):
         file = next(x for x in root.list if x.name == request.args.get('name'))
         del file
         deleted_list.append(request.args.get('name'))
         return jsonify({
         "message": "File deleted successfully.",
         }), 200
      return jsonify({
         "message": "File was not deleted.",
         }), 400


@app.route('/logtextfile', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def logtextfile():
   if request.method == 'POST':
      if any(x.name == request.args.get('name') for x in root.list):
         return jsonify({
         "message": "File already exists.",
      }), 400
      file = LogTextFile(root, request.args.get('name'), request.args.get('info'))
      return jsonify({
         "message": "File created successfully.",
         "file": {
            "parent": str(file.parent.name),
            "name": str(file.name),
            "info": str(file.info)  
         }
      }), 201

   elif request.method == 'GET':
      if any(file.name == request.args.get('name') for file in root.list):
         file = next(x for x in root.list if x.name == request.args.get('name'))
         return jsonify({
         "message": "File was read successfully.",
         "file": {
            "parent": str(file.parent.name),
            "name": str(file.name),
            "info": str(file.info)  
         }
      }), 200
      return jsonify({
         "message": "File doesn't exist.",
         }), 400

   elif request.method == 'PATCH':
      if any(file.name == request.args.get('name') for file in root.list):
         file = next(x for x in root.list if x.name == request.args.get('name'))
         if request.args.get('parent'):
            file.move(root)
            return jsonify({
            "message": "File moved successfully.",
            "file": {
               "parent": str(file.parent.name),
               "name": str(file.name),
               "info": str(file.info)  
            }
         }), 200
         if request.args.get('append'):
            file.append_line(request.args.get('append'))
            return jsonify({
            "message": "Line added successfully.",
            "file": {
               "parent": str(file.parent.name),
               "name": str(file.name),
               "info": str(file.info)   
            }
         }), 201
         return jsonify({
         "message": "Bad request.",
         }), 400 
      return jsonify({
         "message": "File doesn't exist.",
         }), 400 

   else:
      if request.args.get('name') not in deleted_list and any(file.name == request.args.get('name') for file in root.list):
         file = next(x for x in root.list if x.name == request.args.get('name'))
         del file
         deleted_list.append(request.args.get('name'))
         return jsonify({
         "message": "File deleted successfully.",
         }), 200
      return jsonify({
         "message": "File was not deleted.",
         }), 400


@app.route('/bufferfile', methods=['POST', 'GET', 'PATCH', 'DELETE'])
def bufferfile():
   if request.method == 'POST':
      if any(x.name == request.args.get('name') for x in root.list):
         return jsonify({
         "message": "File already exists.",
      }), 400
      file = BufferFile(root, request.args.get('max_size'), request.args.get('name'))
      return jsonify({
         "message": "File created successfully.",
         "file": {
            "parent": str(file.parent),
            "name": str(file.name),
            "MAX_BUF_FILE_SIZE": int(file.MAX_BUF_FILE_SIZE),
            "info": list(file.info )  
         }
      }), 201

   elif request.method == 'GET':
      if any(file.name == request.args.get('name') for file in root.list):
         file = next(x for x in root.list if x.name == request.args.get('name'))
         return jsonify({
         "message": "File was read successfully.",
         "file": {
            "parent": str(file.parent),
            "name": str(file.name),
            "MAX_BUF_FILE_SIZE": int(file.MAX_BUF_FILE_SIZE),
            "info": list(file.info )  
         }
      }), 200
      return jsonify({
         "message": "File doesn't exist.",
         }), 400

   elif request.method == 'PATCH':
      if any(file.name == request.args.get('name') for file in root.list):
         file = next(x for x in root.list if x.name == request.args.get('name'))
         if request.args.get('parent'):
            file.move(root)
            return jsonify({
            "message": "File moved successfully.",
            "file": {
               "parent": str(file.parent.name),
               "name": str(file.name),
               "MAX_BUF_FILE_SIZE": int(file.MAX_BUF_FILE_SIZE),
               "info": list(file.info)  
            }
         }), 200
         if request.args.get('append'):
            file.push(request.args.get('append'))
            return jsonify({
            "message": "Line added successfully.",
            "file": {
               "parent": str(file.parent.name),
               "name": str(file.name),
               "MAX_BUF_FILE_SIZE": int(file.MAX_BUF_FILE_SIZE),
               "info": list(file.info)  
            }
         }), 201
         if request.args.get('consume'):
            if len(file.info) > 0:
               file.consume()
            return jsonify({
            "message": "Line consumed successfully.",
            "file": {
               "parent": str(file.parent.name),
               "name": str(file.name),
               "MAX_BUF_FILE_SIZE": int(file.MAX_BUF_FILE_SIZE),
               "info": list(file.info)   
            }
         }), 200
         return jsonify({
         "message": "Bad request.",
         }), 400 
      return jsonify({
         "message": "File doesn't exist.",
         }), 400 

   else:
      if request.args.get('name') not in deleted_list and any(file.name == request.args.get('name') for file in root.list):
         file = next(x for x in root.list if x.name == request.args.get('name'))
         del file
         deleted_list.append(request.args.get('name'))
         return jsonify({
         "message": "File deleted successfully.",
         }), 200
      return jsonify({
         "message": "File was not deleted.",
         }), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0')