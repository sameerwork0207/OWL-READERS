from flask import Flask, render_template, request

app = Flask(__name__)

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class BookClub:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre):
        book = Book(title, author, genre)
        self.books.append(book)

    def recommend_books(self, genre):
        genre_books = [book for book in self.books if book.genre.lower() == genre.lower()]
        return genre_books

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        genre = request.form['genre']
        recommended_books = club.recommend_books(genre)
        return render_template('index.html', genre=genre, books=recommended_books)
    return render_template('index.html')


if __name__ == '__main__':
    club = BookClub()

    # Add 50 books to the club
    books_to_add = [
    ("To Kill a Mockingbird", "Harper Lee", "Fiction"),
    ("1984", "George Orwell", "Dystopian Fiction"),
    ("Pride and Prejudice", "Jane Austen", "Romance"),
    ("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
    ("Moby-Dick", "Herman Melville", "Adventure"),
    ("The Catcher in the Rye", "J.D. Salinger", "Coming-of-age"),
    ("Animal Farm", "George Orwell", "Satire"),
    ("Jane Eyre", "Charlotte Brontë", "Gothic"),
    ("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy"),
    ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy"),
    ("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
    ("The Chronicles of Narnia", "C.S. Lewis", "Fantasy"),
    ("A Tale of Two Cities", "Charles Dickens", "Historical Fiction"),
    ("The Hunger Games", "Suzanne Collins", "Science Fiction"),
    ("Gone with the Wind", "Margaret Mitchell", "Historical Fiction"),
    ("The Alchemist", "Paulo Coelho", "Fantasy"),
    ("The Da Vinci Code", "Dan Brown", "Mystery"),
    ("Brave New World", "Aldous Huxley", "Dystopian Fiction"),
    ("The Picture of Dorian Gray", "Oscar Wilde", "Gothic Fiction"),
    ("Wuthering Heights", "Emily Brontë", "Gothic Fiction"),
    ("Dracula", "Bram Stoker", "Gothic Horror"),
    ("Frankenstein", "Mary Shelley", "Gothic Science Fiction"),
    ("The Odyssey", "Homer", "Epic"),
    ("The Iliad", "Homer", "Epic Poetry"),
    ("Anna Karenina", "Leo Tolstoy", "Realistic Fiction"),
    ("Crime and Punishment", "Fyodor Dostoevsky", "Philosophical Fiction"),
    ("One Hundred Years of Solitude", "Gabriel García Márquez", "Magical Realism"),
    ("The Bell Jar", "Sylvia Plath", "Semi-autobiographical Novel"),
    ("The Road", "Cormac McCarthy", "Post-apocalyptic"),
    ("Lord of the Flies", "William Golding", "Allegory"),
    ("Les Misérables", "Victor Hugo", "Historical Novel"),
    ("Siddhartha", "Hermann Hesse", "Spiritual Fiction"),
    ("The Grapes of Wrath", "John Steinbeck", "Social Realism"),
    ("The Handmaid's Tale", "Margaret Atwood", "Dystopian"),
    ("A Clockwork Orange", "Anthony Burgess", "Dystopian Fiction"),
    ("The Scarlet Letter", "Nathaniel Hawthorne", "Romance"),
    ("Catch-22", "Joseph Heller", "Satire"),
    ("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction"),
    ("The Shining", "Stephen King", "Horror"),
    ("The Stand", "Stephen King", "Post-apocalyptic"),
    ("The Road Less Traveled", "M. Scott Peck", "Self-help"),
    ("The Sun Also Rises", "Ernest Hemingway", "Modernist Novel"),
    ("Infinite Jest", "David Foster Wallace", "Postmodern Literature"),
    ("The Fountainhead", "Ayn Rand", "Philosophical Fiction"),
    ("A Song of Ice and Fire", "George R.R. Martin", "Fantasy"),
    ("The Name of the Wind", "Patrick Rothfuss", "Fantasy"),
    ("The Princess Bride", "William Goldman", "Fantasy"),
    ("The Shadow of the Wind", "Carlos Ruiz Zafón", "Gothic Mystery"),
    ("The Girl with the Dragon Tattoo", "Stieg Larsson", "Crime Fiction"),
    ("The Brothers Karamazov", "Fyodor Dostoevsky", "Philosophical Fiction"),
    ("The Count of Monte Cristo", "Alexandre Dumas", "Adventure"),
    ("War and Peace", "Leo Tolstoy", "Historical Fiction"),
    ("Don Quixote", "Miguel de Cervantes", "Satire"),
    ("The Divine Comedy", "Dante Alighieri", "Epic Poetry"),
    ("The Metamorphosis", "Franz Kafka", "Absurdist Fiction"),
    ("The Stranger", "Albert Camus", "Philosophical Fiction"),
    ("A Farewell to Arms", "Ernest Hemingway", "War Novel"),
    ("For Whom the Bell Tolls", "Ernest Hemingway", "War Novel"),
    ("The Old Man and the Sea", "Ernest Hemingway", "Adventure"),
    ("Lolita", "Vladimir Nabokov", "Literary Fiction"),
    ("Slaughterhouse-Five", "Kurt Vonnegut", "Satire"),
    ("Beloved", "Toni Morrison", "Historical Fiction"),
    ("Invisible Man", "Ralph Ellison", "Social Commentary"),
    ("Blood Meridian", "Cormac McCarthy", "Western"),
    ("Of Mice and Men", "John Steinbeck", "Tragedy"),
    ("American Psycho", "Bret Easton Ellis", "Satire"),
    ("Mrs. Dalloway", "Virginia Woolf", "Modernist Novel"),
    ("To the Lighthouse", "Virginia Woolf", "Modernist Novel"),
    ("Heart of Darkness", "Joseph Conrad", "Adventure"),
    ("The Canterbury Tales", "Geoffrey Chaucer", "Classic"),
    ("The Handmaid's Tale", "Margaret Atwood", "Dystopian"),
    ("The Trial", "Franz Kafka", "Philosophical Fiction")
        # Add more books here...
        # Add your books here...
    ]

    for book_info in books_to_add:
        club.add_book(*book_info)

    app.run(debug=True)