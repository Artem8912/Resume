# Модуль с функциями, отвечающими за качественное отображение страницы книги

import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    punct_sym =[',','.','?','!',':',';']
    
    text_part = list(text)
    text=list(text)
    text_part=text_part[start:start+size]
    b=set(punct_sym)
    c=set(text_part)
    a= b.intersection(c)
    if a!=set() and len(text)>1:
        if text_part[len(text_part)-1] not in punct_sym:                                 
            while (text_part[len(text_part)-1] not in punct_sym):
                   text_part.pop()
        if text_part[len(text_part)-1]  in punct_sym: 
            while text[start+len(text_part)] in punct_sym:
                   text_part.append(text[start+len(text_part)])
        if text_part[0]  in punct_sym: 
            while text_part[0]  in punct_sym:
                   text_part.pop(0) 
        return ''.join(text_part)
                  
    else:
               print('В тексте отсутствуют необходимые символы')


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path,'r',encoding='utf-8') as f:
        text = f.read()
        n=len(text)//PAGE_SIZE
        print(n)
        start=0
       
        for i in range(0,n):
            
            book[i+1] = _get_part_text(text,start,PAGE_SIZE) 
            start+=len(book[i+1])
            book[i+1]=book[i+1].lstrip().rstrip()
            
       
        book[n+1] = text[start:len(text)].lstrip().rstrip()
        
    print(book)


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))