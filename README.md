# FileReaderApp
Flask application that renders HTML content from text files.

1) Run app.py
2) Go to http://localhost:5000/

URL structure: http://localhost:5000/files/[FILENAME]/?startln=[START]&endln=[END]<br>
Optional URL query parameters:<br>
FILENAME: str  (e.g. file1.txt)<br>
START: int     (index of line start)<br>
END: int       (index of line end - should be higher than START
