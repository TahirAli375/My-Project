import sqlite3
import streamlit as st
import datetime as dt
k=dt.datetime.now()

# Database connection setup
conn = sqlite3.connect('user_books.db', check_same_thread=False)
c = conn.cursor()

# Create the books table if it doesn't exist
c.execute('''
Create Table if not exists books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL
)
''')

# Check and populate initial data
c.execute('SELECT COUNT(*) FROM books')
if c.fetchone()[0] == 0:
    books = [
        ('To Kill a Mockingbird', 'Harper Lee'),
        ('1984', 'George Orwell'),
        ('Pride and Prejudice', 'Jane Austen'),
        ('The Great Gatsby', 'F. Scott Fitzgerald'),
        ('Moby-Dick', 'Herman Melville'),
        ('High School English Grammar and Composition', 'Wren & Martin'),
        ('Exploring The World of English', 'Saadat Ali Shah'),
        ('Discovering The World of English', 'World Times'),
        ('Additional Mathematics', 'Hoo Soo Thong'),
        ('The Catcher in the Rye', 'J.D. Salinger'),
        ('The Hobbit', 'J.R.R. Tolkien'),
        ('Fahrenheit 451', 'Ray Bradbury'),
        ('Jane Eyre', 'Charlotte Brontë'),
        ('Brave New World', 'Aldous Huxley'),
        ('The Lord of the Rings', 'J.R.R. Tolkien'),
        ('Animal Farm', 'George Orwell'),
        ('The Chronicles of Narnia', 'C.S. Lewis'),
        ('The Alchemist', 'Paulo Coelho'),
        ('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling'),
        ('The Da Vinci Code', 'Dan Brown')
    ]
    c.executemany('INSERT INTO books (title, author) VALUES (?, ?)', books)
    conn.commit()

# Function to search for a book
def search_book(title):
    c.execute('SELECT * FROM books WHERE UPPER(title) LIKE UPPER(?)', (f'%{title}%',))
    return c.fetchall()

# Function to save registration info
def save_registration(book_name, name, fname, cnic,From_Date,To_Date):
    with sqlite3.connect('book.db', check_same_thread=False) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        Create Table if not exists Registrations (
            book_Name TEXT,
            Name TEXT,
            FName TEXT,
            CNIC INTEGER,
            From_Date TEXT,
            To_Date TEXT
        )
        ''')
        cursor.execute('INSERT INTO Registrations (book_Name, Name, FName, CNIC,From_Date,To_Date) VALUES (?, ?, ?, ?,?,?)', 
                      (book_name, name, fname, cnic,From_Date,To_Date))
        conn.commit()

# Streamlit interface
st.title('Welcome to :red[Digital Library]')
st.subheader(":blue[Let\'s Enter the World of Books! 📗📖📚]")

# Search section
book_title = st.text_input('Enter the title of the book you are looking for:', 
                           placeholder='Book Name')

if st.button('Search'):
    if book_title:
        results = search_book(book_title)
        if results:
            book_list = [f"{book[1]} by {book[2]}" for book in results]
            st.success(f"Books found: {', '.join(book_list)}")
        else:
            st.warning("Book not found")
    else:
        st.warning("Please enter a book title to search")
# Registration section (optional)
st.subheader("Register for a book You want to borrow! 📚")
book_name = st.selectbox('Select a book to register:', [book[1] for book in c.execute('SELECT * FROM books').fetchall()])
name = st.text_input('Enter your name:')
fname = st.text_input('Enter your father\'s name:')
cnic = st.number_input('Enter your CNIC number:')
From_Date=st.date_input('From:',k.date())
To_Date=st.date_input('To:')

if st.button('Register'):
    if name and fname and cnic:
        save_registration(book_name, name, fname, cnic,From_Date,To_Date)
        st.success("Registration successful!")
    else:
        st.warning("Please fill in all the fields")
