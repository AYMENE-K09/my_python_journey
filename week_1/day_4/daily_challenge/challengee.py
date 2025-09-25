import math

class Pagination():
    def __init__(self, items = [], page_size = 10):
        self.page_size = page_size
        self.items = items
        self.current_idx = 0
        self.Total_n_of_pages = math.ceil(len(self.items) / page_size)

    
    def get_visible_items(self):
        if self.current_idx == 0:
            self.current_idx += 1
        start_idx = (self.current_idx - 1) * self.page_size
        end_idx = min(start_idx + self.page_size, len(self.items))
        for i in range(start_idx, end_idx):
            print(self.items[i])


p = Pagination("abcdefghijklmnopqrstuvwxyz", 4)
p.get_visible_items()
'''
page_size = 4
current_idx = 2
items = [0,1,2,3,4,5,6,7,8,9]
if current_idx == 0:
    current_idx += 1
start_idx = (current_idx - 1) * page_size
end_idx = min(start_idx + page_size, len(items))
for i in range(start_idx, end_idx):
    print(items[i])
    '''