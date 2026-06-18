# Find book in library using book id (without dictionary)
book_ids = [1, 2, 3, 4, 5]
book_titles = ["Book 1", "Book 2", "Book 3", "Book 4", "Book 5"]

def find_book_by_id(book_ids, book_titles, book_id):
    for i in range(len(book_ids)):
        if book_ids[i] == book_id:
            return book_titles[i]
    return None

result = find_book_by_id(book_ids, book_titles, 3)
print(result)