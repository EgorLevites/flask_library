from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from classes import db, User, Student, Book
import functions

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'secret-key-goes-here'
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
CORS(app)

# Create tables within the application context
with app.app_context():
    db.create_all()

# Route examples
app.add_url_rule('/add_student', methods=['POST'], view_func=functions.add_student)
app.add_url_rule('/all_students', methods=['GET'], view_func=functions.get_students)
app.add_url_rule('/add_book', methods=['POST'], view_func=functions.add_book)
app.add_url_rule('/all_books', methods=['GET'], view_func=functions.get_books)
app.add_url_rule('/update_book/<int:book_id>', methods=['PUT'], view_func=functions.update_book)
app.add_url_rule('/update_student/<int:student_id>', methods=['PUT'], view_func=functions.update_student)
app.add_url_rule('/del_book/<int:book_id>', methods=['DELETE'], view_func=functions.delete_book)
app.add_url_rule('/del_student/<int:student_id>', methods=['DELETE'], view_func=functions.delete_student)
app.add_url_rule('/loan_book/<int:book_id>', methods=['PUT'], view_func=functions.loan_book)
app.add_url_rule('/return_book/<int:book_id>', methods=['PUT'], view_func=functions.return_book)
app.add_url_rule('/loaned_books/<int:student_id>', methods=['GET'], view_func=functions.get_loaned_books)

if __name__ == '__main__':
    app.run(debug=True)
