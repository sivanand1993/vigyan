API_KEY = "mysecret123"  # In real-world apps, store this securely!


from flask import Flask, request, jsonify, abort

app = Flask(__name__)

from functools import wraps


def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        key = request.headers.get('x-api-key')
        if key != API_KEY:
            abort(401, description="Invalid or missing API Key")
        return f(*args, **kwargs)
    return decorated_function

# Simulated in-memory "database"
books_db = {
    1: {"title": "1984", "author": "George Orwell"},
    2: {"title": "To Kill a Mockingbird", "author": "Harper Lee"}
}

# GET all books
@app.route('/books', methods=['GET'])
# @require_api_key
def get_books():
    return jsonify(books_db)

# GET a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
@require_api_key
def get_book(book_id):
    book = books_db.get(book_id)
    if book:
        return jsonify(book)
    else:
        abort(404, description="Book not found")

# POST a new book
@app.route('/books', methods=['POST'])
@require_api_key
def add_book():
    if not request.json or 'title' not in request.json or 'author' not in request.json:
        abort(400, description="Missing title or author in request")

    new_id = max(books_db.keys()) + 1
    books_db[new_id] = {
        "title": request.json['title'],
        "author": request.json['author']
    }
    return jsonify({new_id: books_db[new_id]}), 201

# DELETE a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
@require_api_key
def delete_book(book_id):
    if book_id in books_db:
        deleted = books_db.pop(book_id)
        return jsonify({"deleted": deleted})
    else:
        abort(404, description="Book not found")

# PUT - Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
@require_api_key
def update_book(book_id):
    if book_id not in books_db:
        abort(404, description="Book not found")

    data = request.json
    if not data:
        abort(400, description="Request must be JSON")

    title = data.get('title', '').strip()
    author = data.get('author', '').strip()

    if not title or not author:
        abort(400, description="Both title and author are required and cannot be empty")

    books_db[book_id] = {"title": title, "author": author}
    return jsonify({book_id: books_db[book_id]})


# Error handlers
@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)

