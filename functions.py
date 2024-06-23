from flask import request, jsonify
from classes import db, Student, Book

def add_student():
    data = request.get_json()
    if not data or not 'name' in data or not 'city' in data or not 'age' in data:
        return jsonify({"message": "Invalid data"}), 400
    new_student = Student(name=data['name'], city=data['city'], age=data['age'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student created successfully"}), 201

def get_students():
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name, "city": student.city, "age": student.age} for student in students])

def add_book():
    data = request.get_json()
    if not data or not 'name' in data or not 'author' in data or not 'published' in data:
        return jsonify({"message": "Invalid data"}), 400
    new_book = Book(name=data['name'], author=data['author'], published=data['published'], student_id=data.get('student_id', 0))
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book created successfully"}), 201

def get_books():
    books = Book.query.all()
    return jsonify([{"id": book.id, "name": book.name, "author": book.author, "published": book.published, "student_id": book.student_id} for book in books])

def update_book(book_id):
    data = request.get_json()
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    if 'name' in data:
        book.name = data['name']
    if 'author' in data:
        book.author = data['author']
    if 'published' in data:
        book.published = data['published']
    if 'student_id' in data:
        book.student_id = data['student_id']

    db.session.commit()
    return jsonify({"message": "Book updated successfully"}), 200

def update_student(student_id):
    data = request.get_json()
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"message": "Student not found"}), 404

    if 'name' in data:
        student.name = data['name']
    if 'city' in data:
        student.city = data['city']
    if 'age' in data:
        student.age = data['age']

    db.session.commit()
    return jsonify({"message": "Student updated successfully"}), 200

def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    if book.student_id != 0:
        return jsonify({"message": "Cannot delete book as it is currently loaned out"}), 400

    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"}), 200

def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"message": "Student not found"}), 404

    # Check if the student has any loaned books
    if Book.query.filter_by(student_id=student_id).count() > 0:
        return jsonify({"message": "Cannot delete student as they have loaned books"}), 400

    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully"}), 200

def loan_book(book_id):
    data = request.get_json()
    if not data or 'student_id' not in data:
        return jsonify({"message": "Invalid data"}), 400

    book = Book.query.get(book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    if book.student_id != 0:
        return jsonify({"message": "Book is already loaned out"}), 400

    student = Student.query.get(data['student_id'])
    if not student:
        return jsonify({"message": "Student not found"}), 404

    book.student_id = data['student_id']
    db.session.commit()
    return jsonify({"message": "Book loaned successfully"}), 200



def return_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    if book.student_id == 0:
        return jsonify({"message": "Book is not currently loaned out"}), 400

    book.student_id = 0
    db.session.commit()
    return jsonify({"message": "Book returned successfully"}), 200

def get_loaned_books(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"message": "Student not found"}), 404

    loaned_books = Book.query.filter_by(student_id=student_id).all()
    return jsonify([{"id": book.id, "name": book.name, "author": book.author, "published": book.published, "student_id": book.student_id} for book in loaned_books])
