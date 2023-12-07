from flask import Flask,jsonify,request
import mysql.connector
class my_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="123454321",database="book_database")
            self.cur=self.con.cursor(dictionary=True)   
            print("Connection successful")
        except:
            print("Connection error")
       
    def reterive_all(self):
        self.cur.execute("SELECT * From books")
        result=self.cur.fetchall()
        if len(result)>0:
            return jsonify(result)
        else:
            return "No Data Found"
    

    def add_new_book(self,input_data):
        if len(input_data)==3 and 'id' in input_data and 'author' in input_data and 'genre' in input_data:
         book_name=input_data['id']
         author=input_data['author']
         genre=input_data['genre']
         book = (book_name,author,genre)

         check_query = "SELECT id FROM books WHERE id = %s AND author = %s AND genre = %s"
         self.cur.execute(check_query, (book_name, author, genre))
         existing_book = self.cur.fetchone()
         if existing_book:
            return "Already exists"
         else:
             insert_query = "INSERT INTO books (id, author, genre) VALUES (%s, %s, %s)"
             self.cur.execute(insert_query,book)
             self.con.commit()
             return "New book added successfully into the database"
        else:
         return "Invalid input."
    
    def update_book(self,input_data):
         check_query = "SELECT id FROM books WHERE id = %s"
         self.cur.execute(check_query, (input_data['id'],))
         existing_book = self.cur.fetchone()
         if existing_book:
            update_query = "UPDATE books SET author = %s, genre = %s WHERE id = %s"
            book_data = (input_data['author'], input_data['genre'], input_data['id'])
            self.cur.execute(update_query, book_data)
            self.con.commit()
            return "Book updated successfully"
         else:
            return "Book not found"
     
          
       
         

app = Flask(__name__)
obj = my_model()

@app.route('/api/books', methods=['GET'])
def get():
    return obj.reterive_all()

@app.route('/api/books', methods=['POST'])
def add():
   return obj.add_new_book(request.form)
   
@app.route('/api/books/<string:id>', methods=['PUT'])
def update(id):
    input_data=request.form
    if len(input_data)==3 and 'id' in input_data and 'author' in input_data and 'genre' in input_data:
         input_data = {
        'id': id,
        'author': input_data['author'],
        'genre': input_data['genre']
    }
         return obj.update_book(input_data)
    else:
          return "Invalid input"
   