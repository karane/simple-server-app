import MySQLdb
from util import singleton
from models import Item
from urllib.parse import urlparse
import os

@singleton
class ItemRepository:
    def __init__(self):
        database_url = os.environ.get('DATABASE_URL')
        db_config = self._parse_url(database_url)

        self.conn = MySQLdb.connect(**db_config)

    def _parse_url(self, url):
        parsed_url = urlparse(url)
        db_config = {
            'host': parsed_url.hostname,
            'user': parsed_url.username,
            'passwd': parsed_url.password,
            'db': parsed_url.path[1:],
        }

        return db_config


    # Route to create an item
    def create_item(self, item: Item):
        cursor = self.conn.cursor()
        query = "INSERT INTO items (name, description) VALUES (%s, %s)"
        cursor.execute(query, (item.name, item.description))
        self.conn.commit()
        item.id = cursor.lastrowid
        cursor.close()
        return item


    # Endpoint to retrieve a list of items
    def read_items(self, skip: int = 0, limit: int = 10):
        cursor = self.conn.cursor()
        query = "SELECT id, name, description FROM items LIMIT %s, %s"
        cursor.execute(query, (skip, limit))
        items = cursor.fetchall()
        cursor.close()
        return [{"id": item[0], "name": item[1], "description": item[2]} for item in items]
    
    # Route to read an item
    def read_item(self, item_id: int):
        cursor = self.conn.cursor()
        query = "SELECT id, name, description FROM items WHERE id=%s"
        cursor.execute(query, (item_id,))
        item = cursor.fetchone()
        cursor.close()
        if item is None:
            return None
        
        return {"id": item[0], "name": item[1], "description": item[2]}

    # Route to update an item
    def update_item(self, item_id: int, item: Item):
        cursor = self.conn.cursor()
        query = "UPDATE items SET name=%s, description=%s WHERE id=%s"
        cursor.execute(query, (item.name, item.description, item_id))
        self.conn.commit()
        cursor.close()
        item.id = item_id
        return item

    # Route to delete an item
    def delete_item(self, item_id: int):
        cursor = self.conn.cursor()
        query = "DELETE FROM items WHERE id=%s"
        cursor.execute(query, (item_id,))
        self.conn.commit()
        cursor.close()
        return {"id": item_id}
