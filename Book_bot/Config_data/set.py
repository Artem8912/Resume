# Модуль,, содержащий функцию, рабивающую книгу на страницы
from Service.file_handling import _get_part_text,book

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 5
with open('book/book.txt','r') as f:
    print(f.read())
def prepare_book(path: str) -> None:
    with open(path,'r') as f:
        text = str(f.read())
        n=len(text)/PAGE_SIZE
        for i in range(1,n+1):
            book[i] = _get_part_text(text,i*PAGE_SIZE,PAGE_SIZE)
         