_userName = ''
_currentBook = ''

def set_user(name):
    global _userName
    _userName = name

def get_user():
    return _userName

def set_currentBook(currentBook):
    global _currentBook
    _currentBook = currentBook

def get_currentBook():
    return _currentBook
