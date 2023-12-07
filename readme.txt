Flask Book Database RESTful API

Overview:
This Flask-based RESTful API manages a book database, allowing users to perform CRUD operations (Create, Read, Update, Delete). It interacts with a MySQL database to store and retrieve book information.

Dependencies:
- Python 3.12
- Flask
- mysql-connector-python

Setup Instructions:
1. Ensure Python 3.12 is installed on your system.
2. Install Flask using pip:
    $ pip install Flask
3. Install mysql-connector-python:
    $ pip install mysql-connector-python

Database Configuration:
- The application assumes a MySQL database named 'book_database' is set up on 'localhost'.
- Database connection parameters: 
    - Host: localhost
    - User: root
    - Password: 123454321
    - Database: book_database

Running the Application:
1. Clone/download the repository containing the Flask application code.
2. Navigate to the directory containing the code.
3. Run the Flask application by executing the script containing the code in your terminal:
    $ python app.py
4. The application will start a server on http://localhost:5000/

I have created a database named Books which have three columns one is book_id = book_name as primary key, author, genre

API Documentation:

1. GET /api/books
    - Description: Retrieve all books from the database.
    - Request Method: GET
    - Expected Response Format: JSON array containing book objects.
    - Example Response:
        [
            {
                "id": "Book Name 1",
                "author": "Author Name",
                "genre": "Genre Type"
            },
            {
                "id": "Book Name 2",
                "author": "Another Author",
                "genre": "Fiction"
            },
            ...
        ]

2. POST /api/books
    - Description: Add a new book to the database.
    - Request Method: POST
    - Request Payload Format: JSON object containing 'author' and 'genre'.
    - Example Request:
        {
            "id": book_name
            "author": "New Author",
            "genre": "Sci-Fi"
        }
    - Expected Response: "New book added successfully into the database" or error messages.

3. PUT /api/books/<id>
    - Description: Update book details based on the provided ID (book name).
    - Request Method: PUT
    - Request URL Parameter: <id> - Name of the book to be updated.
    - Request Payload Format: JSON object containing 'author' and 'genre'.
    - Example Request:
        {
            "author": "Updated Author",
            "genre": "Updated Genre"
        }
    - Expected Response: "Book updated successfully" or  error messages.

Class: my_model
- This class interacts with the MySQL database and provides methods for CRUD operations:
    - retrieve_all(): Retrieves all books from the database.
    - add_new_book(input_data): Adds a new book to the database.
    - update_book(input_data): Updates book details based on input data.

