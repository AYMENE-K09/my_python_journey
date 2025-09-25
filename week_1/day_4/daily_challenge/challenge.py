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
            my_current_page = []
            for i in range(start_idx, end_idx):
                my_current_page.append(self.items[i])
            return my_current_page

    def go_to_page(self, page_num):
        if page_num == 0:
            raise ValueError("Page not found")
        
        self.current_idx = page_num

    def first_page(self):
        self.current_idx = 1

    def last_page(self):
        self.current_idx = self.Total_n_of_pages

    def next_page(self):
        if self.current_idx != self.Total_n_of_pages:
            self.current_idx += 1

    def previous_page(self):
        if self.current_idx != 1:
            self.current_idx -= 1

    # def__str__
alphabet = "abcdefghijklmnopqrstuvwxyz"
p = Pagination(alphabet, 4)
print(p.get_visible_items())
