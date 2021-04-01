# FileReaderApp
Flask application that renders HTML content from text files.

1) Run app.py
2) Go to http://localhost:5000/

URL structure: http://localhost:5000/files/[FILENAME]/?startln=[START]&endln=[END]
Optional URL query parameters:
FILENAME: str  (e.g. file1.txt)
START: int     (index of line start)
END: int       (index of line end - should be higher than START
