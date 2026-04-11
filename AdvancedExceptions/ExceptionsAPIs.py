import sqlite3

from IPython.core.pylabtools import retina_figure


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

def fetch_blogs():
    try:
        # connect to the database
        con = sqlite3.connect('blogs.db')
        cur = con.cursor()

        # execute query
        cur.execute("SELECT * FROM blogs")
        # fetch the data and turn it into a dict
        result = list(map(blog_lst_to_json() , cur.fetchall()))

        return result
    # Not recommended
    except Exception as e:
        print(e)
        return []

    finally:
        # Close the database connection
        con.close()


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
