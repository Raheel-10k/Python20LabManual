class LibraryItem:
    library_items = []


    def __init__(self, item_type, item_name, item_id, item_count=0):
        self.item_type = item_type
        self.item_name = item_name
        self.item_id = item_id
        self.item_count = item_count

        item_data = {
            'item_type': self.item_type,
            'item_name': self.item_name,
            'item_id': self.item_id,
            'item_count': self.item_count
        }

        if self.item_type == 'book':
            self.author_name = input("Enter author's name for the book: ")
            item_data['author_name'] = self.author_name
        elif self.item_type == 'journal':
            self.publisher_name = input("Enter publisher's name for the journal: ")
            item_data['publisher_name'] = self.publisher_name
        elif self.item_type == 'dvd':
            self.director_name = input("Enter director's name for the DVD: ")
            item_data['director_name'] = self.director_name
        else:
            raise ValueError("Invalid item_type. Please retry with 'book', 'journal', or 'dvd'.")

        self.library_items.append(item_data)

    def display_info(self):
        for item_data in self.library_items:
            print("Information about library items:")
            for key, value in item_data.items():
                print(f"{key}: {value}")
            print("\n")

    def check_out(self, item_name):
        for item_data in self.library_items:
            if item_data['item_name'] == item_name:
                if item_data['item_count'] > 0:
                    print(f"Checking out {item_name}")
                    item_data['item_count'] -= 1
                else:
                    print(f"All copies of {item_name} are checked out.")
                return
        
        print(f"{item_name} not found in the library.")

    def check_in(self, item_name):
        for item_data in self.library_items:
            if item_data['item_name'] == item_name:
                print(f"Checking in {item_name}")
                item_data['item_count'] += 1
                return
        
        self.__init__(self.item_type, item_name, len(self.library_items) + 1, item_count=1)


class Book(LibraryItem):
    def __init__(self, item_name, item_id):
        super().__init__('book', item_name, item_id)


class DVD(LibraryItem):
    def __init__(self, item_name, item_id):
        super().__init__('dvd', item_name, item_id)


class Journal(LibraryItem):
    def __init__(self, item_name, item_id):
        super().__init__('journal', item_name, item_id)


book = Book('The Great Gatsby', 1)      #item_name and item_id
dvd = DVD('Inception', 2)
journal = Journal('Scientific American', 3)

book.check_in('The Great Gatsby')       #plus 1 to item_count
book.check_in('The Great Gatsby')
book.check_in('The Great Gatsby')
book.check_in('The Great Gatsby')
book.check_in('The Great Gatsby')
book.display_info()
book.check_out('The Great Gatsby')
book.display_info()
book.display_info()

dvd.check_in('Inception')
dvd.display_info()

journal.check_out('Scientific American')
journal.display_info()
