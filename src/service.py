from util import singleton
from repository import ItemRepository

@singleton
class Service():
    def __init__(self):
        self.repo = ItemRepository()

    def create_item(self, item):
        return self.repo.create_item(item)
    
    def read_items(self, skip: int = 0, limit: int = 10):
        return self.repo.read_items(skip, limit)
    
    def read_item(self, item_id):
        return self.repo.read_item(item_id)
    
    def update_item(self, item_id, item):
        return self.repo.update_item(item_id, item)
    
    def delete_item(self, item_id):
        return self.repo.delete_item(item_id)

