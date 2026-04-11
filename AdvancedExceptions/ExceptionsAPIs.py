import sqlite3

# Creating context manager to db connection
# (creation and destruction of the connection)
class SQLite:
    def __init__(self, file='application.db'):
        self.file = file
    def __enter__(self):
        # Connecting to the database
        self.conn = sqlite3.connect(self.file)
        # Returning a cursor to execute queries
        return self.conn.cursor()
    def __exit__(self, type, value, traceback):
        # Closing connection when the block is exited,
        # even if an exception is raised
        self.conn.close()

class NotFoundError(Exception):
    pass

class NotAuthorizedError(Exception):
    pass

def blog_lst_to_json(item):
    return {
            'id': item[0],
            'title': item[1],
            'content': item[2],
            'public': item[3],
        }

# Implementing context manager to handle database connection and exceptions
def fetch_blogs():
    try:
        with SQLite('blogs.db') as cur:
            # execute query
            cur.execute("SELECT * FROM blogs")
            # fetch the data and turn it into a dict
            result = list(map(blog_lst_to_json() , cur.fetchall()))

            return result
    # Not recommended
    except Exception as e:
        print(e)
        return []


def fetch_blog(id: str):
    try:
        # connect to the database
        con = sqlite3.connect('blogs.db')
        cur = con.cursor()

        # execute query
        cur.execute("SELECT * FROM blogs where id = ?", (id,))
        result = cur.fetchone()

        if result in None:
            raise NotFoundError(f'Unable to found blog with if {id}.')

        # fetch the data and turn it into a dict
        data = blog_lst_to_json(result)
        # Checking if the blog is public
        if not data['public']:
            raise NotAuthorizedError(f'Blog with id {id} is not public.')

        return data
    except sqlite3.OperationalError as e:
        print(e)
        raise NotFoundError(f'Unable to found blog with if {id}.')
    finally:
        # Close the database connection
        con.close()
