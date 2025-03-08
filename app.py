from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'  # База данных SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель для отзывов
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(500), nullable=False)

# Создание базы данных
with app.app_context():
    db.create_all()

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Страница с продуктами
@app.route('/products')
def products():
    return render_template('products.html')

# Страница "О нас"
@app.route('/about')
def about():
    return render_template('about.html')

# Страница "Преимущества"
@app.route('/advantages')
def advantages():
    return render_template('advantages.html')

# Страница "Отзывы"
@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    if request.method == 'POST':
        # Добавление нового отзыва
        author = request.form['author']
        text = request.form['text']
        new_review = Review(author=author, text=text)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('reviews'))

    # Получение всех отзывов из базы данных
    reviews = Review.query.all()
    return render_template('reviews.html', reviews=reviews)

# Страница "Контакты"
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)