from flask import Flask
app = Flask(__name__)
from flask_sql_alchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///data.db'
db = SQLAlchemy(app)

class Book(dm.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), unique=False, nullable=False)
    publisher =db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f"{self.name} - {self.description}"
@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Books.query.all()

    output = []
    for book in books:
        book_data = {'book_name': book.name, 'author': author.name, 'publisher': publisher.name}

        output.append(book_data)

    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"name": book.name, "author": author.name, "publisher": publisher.name}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(name=request.json['book_name'], author=request.json['author'], publisher=request.json['author'])
    db.session.add(book)
    db.session.commit()
    return{'id': book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return{"message": "yeet!@"} 