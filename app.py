from flask import Flask,redirect,request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///BooksDataBase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), unique=True, nullable=False)

    author = db.Column(db.String(100), nullable=False)

    category = db.Column(db.String(100), nullable=False)

    price = db.Column(db.Integer, nullable=False)

    quantity = db.Column(db.Integer, nullable=False)

# Books dummy data
book1 = Book(
    title="Python Basics",
    author="Muhammad Ibraheem",
    category="Programming",
    price=1200,
    quantity=10
)

book2 = Book(
    title="Learning Flask",
    author="Miguel Grinberg",
    category="Programming",
    price=1800,
    quantity=8
)

book3 = Book(
    title="Mastering JavaScript",
    author="John Doe",
    category="Programming",
    price=1700,
    quantity=12
)

book4 = Book(
    title="HTML & CSS Design",
    author="Jon Duckett",
    category="Web Development",
    price=1500,
    quantity=15
)

book5 = Book(
    title="React for Beginners",
    author="Sarah Johnson",
    category="Programming",
    price=2200,
    quantity=7
)

book6 = Book(
    title="Node.js Essentials",
    author="David Miller",
    category="Programming",
    price=2100,
    quantity=9
)

book7 = Book(
    title="Express.js Guide",
    author="Chris Lee",
    category="Programming",
    price=1900,
    quantity=6
)

book8 = Book(
    title="MongoDB Complete",
    author="Andrew Kim",
    category="Database",
    price=2000,
    quantity=11
)

book9 = Book(
    title="SQL Fundamentals",
    author="James Brown",
    category="Database",
    price=1600,
    quantity=10
)

book10 = Book(
    title="Data Structures in C++",
    author="Bjarne Stroustrup",
    category="Programming",
    price=2500,
    quantity=5
)

book11 = Book(
    title="Algorithms Made Easy",
    author="Aditya Bhargava",
    category="Programming",
    price=2300,
    quantity=9
)

book12 = Book(
    title="Java Programming",
    author="Herbert Schildt",
    category="Programming",
    price=2400,
    quantity=6
)

book13 = Book(
    title="C Programming",
    author="Dennis Ritchie",
    category="Programming",
    price=1800,
    quantity=14
)

book14 = Book(
    title="Operating Systems",
    author="Abraham Silberschatz",
    category="Computer Science",
    price=3000,
    quantity=4
)

book15 = Book(
    title="Computer Networks",
    author="Andrew Tanenbaum",
    category="Networking",
    price=3200,
    quantity=5
)

book16 = Book(
    title="Artificial Intelligence",
    author="Stuart Russell",
    category="AI",
    price=3500,
    quantity=6
)

book17 = Book(
    title="Machine Learning Basics",
    author="Tom Mitchell",
    category="AI",
    price=3300,
    quantity=8
)

book18 = Book(
    title="Deep Learning",
    author="Ian Goodfellow",
    category="AI",
    price=4200,
    quantity=3
)

book19 = Book(
    title="Cyber Security Essentials",
    author="William Stallings",
    category="Cyber Security",
    price=2800,
    quantity=7
)

book20 = Book(
    title="Ethical Hacking",
    author="Kevin Beaver",
    category="Cyber Security",
    price=2900,
    quantity=5
)

book21 = Book(
    title="Linux Administration",
    author="Brian Ward",
    category="Operating System",
    price=2600,
    quantity=10
)

book22 = Book(
    title="Git & GitHub",
    author="Scott Chacon",
    category="Version Control",
    price=1400,
    quantity=12
)

book23 = Book(
    title="Software Engineering",
    author="Ian Sommerville",
    category="Software Engineering",
    price=3400,
    quantity=4
)

book24 = Book(
    title="Clean Code",
    author="Robert C. Martin",
    category="Programming",
    price=3600,
    quantity=6
)

book25 = Book(
    title="Design Patterns",
    author="Erich Gamma",
    category="Programming",
    price=3900,
    quantity=5
)

book26 = Book(
    title="Python Projects",
    author="Eric Matthes",
    category="Programming",
    price=2100,
    quantity=11
)

book27 = Book(
    title="Flask Web Development",
    author="Miguel Grinberg",
    category="Web Development",
    price=2800,
    quantity=9
)

book28 = Book(
    title="Django Unleashed",
    author="Andrew Pinkham",
    category="Web Development",
    price=2900,
    quantity=8
)

book29 = Book(
    title="PHP & MySQL",
    author="Luke Welling",
    category="Web Development",
    price=2200,
    quantity=7
)

book30 = Book(
    title="Bootstrap 5",
    author="Mark Otto",
    category="Web Development",
    price=1600,
    quantity=13
)

book31 = Book(
    title="Vue.js Essentials",
    author="Evan You",
    category="Programming",
    price=2300,
    quantity=6
)

book32 = Book(
    title="Angular in Action",
    author="Jeremy Wilken",
    category="Programming",
    price=2400,
    quantity=5
)

book33 = Book(
    title="Kotlin for Android",
    author="Antonio Leiva",
    category="Mobile Development",
    price=2500,
    quantity=8
)

book34 = Book(
    title="Android Studio Guide",
    author="John Horton",
    category="Mobile Development",
    price=2600,
    quantity=6
)

book35 = Book(
    title="Swift Programming",
    author="Apple Inc.",
    category="Mobile Development",
    price=2700,
    quantity=7
)

book36 = Book(
    title="Cloud Computing",
    author="Rajkumar Buyya",
    category="Cloud",
    price=3500,
    quantity=4
)

book37 = Book(
    title="AWS Fundamentals",
    author="John Culkin",
    category="Cloud",
    price=3000,
    quantity=9
)

book38 = Book(
    title="Docker Deep Dive",
    author="Nigel Poulton",
    category="DevOps",
    price=3200,
    quantity=5
)

book39 = Book(
    title="Kubernetes Basics",
    author="Brendan Burns",
    category="DevOps",
    price=3400,
    quantity=4
)

book40 = Book(
    title="REST API Design",
    author="Leonard Richardson",
    category="Web Development",
    price=2100,
    quantity=10
)

book41 = Book(
    title="Data Science Handbook",
    author="Jake VanderPlas",
    category="Data Science",
    price=3600,
    quantity=5
)

book42 = Book(
    title="Statistics for Beginners",
    author="Robert Johnson",
    category="Mathematics",
    price=1700,
    quantity=12
)

book43 = Book(
    title="Linear Algebra",
    author="Gilbert Strang",
    category="Mathematics",
    price=2800,
    quantity=6
)

book44 = Book(
    title="Discrete Mathematics",
    author="Kenneth Rosen",
    category="Mathematics",
    price=3100,
    quantity=7
)

book45 = Book(
    title="Computer Graphics",
    author="Donald Hearn",
    category="Computer Science",
    price=2900,
    quantity=5
)

book46 = Book(
    title="Compiler Design",
    author="Alfred Aho",
    category="Computer Science",
    price=3300,
    quantity=4
)

book47 = Book(
    title="Digital Logic Design",
    author="Morris Mano",
    category="Electronics",
    price=2500,
    quantity=8
)

book48 = Book(
    title="Microprocessors",
    author="Ramesh Gaonkar",
    category="Electronics",
    price=2700,
    quantity=6
)

book49 = Book(
    title="Internet of Things",
    author="Arshdeep Bahga",
    category="Technology",
    price=3000,
    quantity=7
)

book50 = Book(
    title="Blockchain Basics",
    author="Daniel Drescher",
    category="Technology",
    price=3200,
    quantity=5
)





# Create Database
with app.app_context():
    db.create_all()

    if Book.query.count() == 0:
        db.session.add_all([
            book1, book2, book3, book4, book5,
            book6, book7, book8, book9, book10,
            book11, book12, book13, book14, book15,
            book16, book17, book18, book19, book20,
            book21, book22, book23, book24, book25,
            book26, book27, book28, book29, book30,
            book31, book32, book33, book34, book35,
            book36, book37, book38, book39, book40,
            book41, book42, book43, book44, book45,
            book46, book47, book48, book49, book50
        ])
        db.session.commit()


@app.route("/")
def home():
    books = Book.query.all()
    return render_template("index.html", books=books)

# add book
@app.route("/add", methods=["GET", "POST"])
def add_book():

    if request.method == "POST":

        title = request.form["title"]
        author = request.form["author"]
        category = request.form["category"]
        price = request.form["price"]
        quantity = request.form["quantity"]

        new_book = Book(
            title=title,
            author=author,
            category=category,
            price=price,
            quantity=quantity
        )

        db.session.add(new_book)
        db.session.commit()

        return redirect("/")

    return render_template("add_book.html")

# 
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_book(id):

    book = Book.query.get_or_404(id)

    if request.method == "POST":
        book.title = request.form["title"]
        book.author = request.form["author"]
        book.category = request.form["category"]
        book.price = request.form["price"]
        book.quantity = request.form["quantity"]

        db.session.commit()

        return redirect("/")

    return render_template("edit_book.html", book=book)


@app.route("/delete/<int:id>")
def delete_book(id):

    book = Book.query.get_or_404(id)

    db.session.delete(book)
    db.session.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)