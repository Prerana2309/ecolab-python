from dbutils import result_as_dict

def get_all_books(cursor):
    cursor.execute('select * from Books')
    results=cursor.fetchall()
    for res in results:
            print(res)

def get_books_by_id(cursor, id):
    cursor.execute("SELECT * FROM books WHERE id = ?", (id,))
    result = cursor.fetchall()
    for book in result:
        print(book)

def remove_book(cursor,id):
    cursor.execute('DELETE FROM books WHERE id= ?', (id,))

def add_book(cursor, id, title, author, price):
    cursor.execute("EXEC ADD_BOOK ?,?,?,?", (id, title, author, price))

def get_books_by_author_id(cursor,a_id):
    cursor.execute('select * from Books where authorid=?',a_id)
    results=result_as_dict(cursor)
    for res in results:
            print(res)

def get_books_review(cursor,id):
    cursor.execute('''SELECT B.title,B.details, R.rating, R.review_text 
                      FROM Reviews R
                      JOIN Books B ON R.bookid = B.id
                      WHERE R.reviewid = ?''',id)
    results=result_as_dict(cursor)
    for res in results:
            print(res)

def add_book_review(cursor,r_id,b_id,u_id,rating,review_text):
    cursor.execute('insert into Reviews(reviewid,bookid,userid,rating,review_text) VALUES (?,?,?,?,?)',r_id,b_id,u_id,rating,review_text)
    