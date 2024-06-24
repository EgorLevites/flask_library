
# Library Management System

## Description
The Library Management System is a web application designed to manage library resources efficiently. It allows users to add, loan, return, and delete books and students. The system also provides functionalities to view all books, students, and loaned books by a specific student.

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   flask run
   ```

## Usage
Open your web browser and go to `http://127.0.0.1:5000` to access the Library Management System.

## Endpoints
The application provides the following API endpoints:

- **Add Student:**
  ```http
  POST /add_student
  ```

- **Add Book:**
  ```http
  POST /add_book
  ```

- **Loan Book:**
  ```http
  PUT /loan_book/<book_id>
  ```

- **Return Book:**
  ```http
  PUT /return_book/<book_id>
  ```

- **Delete Student:**
  ```http
  DELETE /del_student/<student_id>
  ```

- **Delete Book:**
  ```http
  DELETE /del_book/<book_id>
  ```

- **Show All Books:**
  ```http
  GET /all_books
  ```

- **Show All Students:**
  ```http
  GET /all_students
  ```

- **Show Loaned Books by Student:**
  ```http
  GET /loaned_books/<student_id>
  ```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License.
