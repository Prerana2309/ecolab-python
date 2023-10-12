from dbutils import result_as_dict

def get_all_authors(cursor):
    cursor.execute("SELECT name FROM authors")
    result = result_as_dict(cursor)
    print(result)

def remove_author(cursor,author_id):
    cursor.execute("DELETE FROM authors WHERE id = ?", (author_id,))
    return cursor.rowcount > 0

def add_author(cursor):
    author_id = input("Enter author's id: ")
    author_name = input("Enter author's name: ")
    author_bio = input("Enter author's biography: ")
    cursor.execute("INSERT INTO authors (author_id,author_name,author_bio) VALUES (?, ?, ?)", (author_id, author_name, author_bio))

def get_author_by_id(cursor,author_id):
        cursor.execute("SELECT * FROM authors WHERE author_id = ?", (author_id,))
        result = cursor.fetchone()
        for author in result:
            print(author)

def update_author(cursor,author_id,author_name=None,author_bio=None):
    if author_name != None and author_bio!=None:
        cursor.execute('UPDATE Authors SET name=?,bio=? WHERE authorid=?',author_name,author_bio,author_id)
        print(f'{author_id} is updated with name {author_name} and bio {author_bio}')
    elif author_name==None and author_bio!=None:
        cursor.execute('UPDATE Authors SET bio=? WHERE authorid=?',author_bio,author_id)
        print(f'{author_id} is updated with bio {author_bio}')
    elif author_bio==None and author_name!=None:
        cursor.execute('UPDATE Authors SET name=? WHERE authorid=?',author_name,author_id)
        print(f'{author_id} is updated with name {author_name} ')

def get_author_review(cursor,author_id):
    cursor.execute('''SELECT B.title, R.rating, R.review_text 
                      FROM Reviews R
                      JOIN Books B ON R.bookid = B.bookid
                      WHERE B.authorid = ?''',author_id)
    results=result_as_dict(cursor)
    for res in results:
            print(res)