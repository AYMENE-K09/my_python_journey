import math
class Pagination():
    def __init__(self, items, page_size = 10):
        self.items = items
        self.page_size = page_size # items displayed by page
        if self.items is None:
            self.items = list(items)
        self.current_idx = 0
        self.Total_N_of_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
            self.start_index = (self.current_idx - 1) * self.page_size
            self.end_index = min((self.start_index + self.page_size), len(self.items))
            for i in range(self.start_index, self.end_index):
                print(self.items[i])


    def go_to_page(self ,page_num):
        self.page_num = page_num
        if  0 >= page_num or page_num > self.Total_N_of_pages:
            print("page not found")

        else:
            self.current_idx = page_num
            self.start_index = (self.current_idx - 1) * self.page_size
            self.end_index = min((self.start_index + self.page_size), len(self.items))
            for i in range(self.start_index, self.end_index):
                print(self.items[i])
            
            
    def first_page(self):
        self.start_index = (1 - 1) * self.page_size
        self.end_index = min((self.start_index + self.page_size), len(self.items))
        for i in range(self.start_index, self.end_index):
            print(self.items[i])

    def last_page(self):
        self.start_index = (self.Total_N_of_pages - 1) * self.page_size
        self.end_index = min((self.start_index + self.page_size), len(self.items))
        for i in range(self.start_index, self.end_index):
            print(self.items[i])

    def next_page(self):
        if self.current_idx < self.Total_N_of_pages:
            self.current_idx += 1
            self.start_index = (self.current_idx - 1) * self.page_size
            self.end_index = min((self.start_index + self.page_size), len(self.items))
            for i in range(self.start_index, self.end_index):
                print(self.items[i])
        
        else:
            print("page not found")

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
            self.start_index = (self.current_idx - 1) * self.page_size
            self.end_index = min((self.start_index + self.page_size), len(self.items))
            for i in range(self.start_index, self.end_index):
                print(self.items[i])
        
        else:
            print("page not found")


my_list = Pagination("abcdefghijklmnopqrstuvwyxz", 4)
my_list.get_visible_items()
