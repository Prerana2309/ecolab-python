import pyodbc as db
import utils
from dbutils import result_as_dict
from authors import *
from books import *
from users import *

def main():
    driver='{ODBC Driver 18 for SQL Server}'
    server=r'localhost\SQLEXPRESS'
    database='booksdb'
    encrypt='no'
    trusted_Connection='yes'
    connection_string=f'''
        DRIVER={driver};
        SERVER={server};
        DATABASE={database};
        Trusted_Connection={trusted_Connection};
        encrypt={encrypt};
    '''
    with db.connect(connection_string) as connection:
        print('connection successful')
        cursor = connection.cursor()
        print(cursor) 
        
        
        cursor.execute('select * from book_summary')
        result = result_as_dict(cursor)
        print(result)

        command_mapping = {
            'get_all_books':get_all_books,
            'get_books_by_id':get_books_by_id,
            'remove_book': remove_book,
            'add_book': add_book,
            'get_books_by_author_id': get_books_by_author_id,
            'get_books_review': get_books_review,
            'add_book_review': add_book_review,
            'add_author': add_author,
            'get_all_authors': get_all_authors,
            'update_author': update_author,
            'get_author_review':get_author_review,
            'get_all_users':get_all_users,
            'add_new_user': add_new_user,
            'get_user_review':get_user_review,
            'quit': exit,
            'exit': exit
        }

        while True:
            user_input = input('db> ')
            command_parts = user_input.split()
            if command_parts[0] in command_mapping:
                command_name = command_parts[0]
                arguments = command_parts[1:]
                command_function = command_mapping[command_name]
                command_function(cursor, *arguments)
            else:
                print('Invalid command')


if __name__ == '__main__':
    main()
