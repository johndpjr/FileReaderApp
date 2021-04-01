# Owner: John Powell
# File Reader Flask Application
from flask import Flask, redirect, url_for, render_template, request, abort
import os

DEFAULT_FILENAME = 'file1.txt'

def read_file(filepath: str, query_params: dict) -> list:
    """Returns a list of lines from the text file using optional
    start and end line numbers from query_params.
    """

    # Get start and end line #'s from query_params (if they exist)
    if 'startln' in query_params:
        startln = query_params['startln']
    else:
        startln = 0  # Default to line 0 (index 0)
    if 'endln' in query_params:
        endln = query_params['endln']
    else:
        endln = -1  # Default to the last line (index -1)
    
    # Type-check params to ensure usability for list splicing
    try:
        startln, endln = int(startln), int(endln)
    except ValueError:
        abort(redirect(url_for('handle_exception', name='ValueError')))

    # Negative values for startln increases complexity and are unnecessary
    if startln < 0:
        abort(redirect(url_for('handle_exception', name='StartIndexError')))
    if endln <= startln and endln != -1:
        abort(redirect(url_for('handle_exception', name='EndIndexError')))

    # Attempt to open file using UTF-8 encoding
    try:
        with open(filepath, encoding='utf-8') as f:
            lines = f.readlines()
    # Otherwise encoding is in UTF-16-BE-BOM
    except UnicodeError:
        with open(filepath, encoding='utf-16') as f:
            lines = f.readlines()

    # Catch accessing list indexes beyond the range
    if startln >= len(lines):
        abort(redirect(url_for('handle_exception', name='OutOfRangeError')))
    if endln == -1:  # Return lines from start to end of file
        return lines[startln:]
    return lines[startln:endln]


app = Flask(__name__)

# Redirect to /files/ (and thus DEFAULT_FILENAME)
@app.route('/')
def index():
    return redirect(url_for('render_file'))

# Main app route (GET)
# From this endpoint, all files can be accessed
@app.route('/files/', defaults={'filename': DEFAULT_FILENAME})
@app.route('/files/<filename>/', methods=['GET'])
def render_file(filename):
    """Returns rendered HTML content from file (if file exists)."""

    filepath = f'files/{filename}'
    # Get optional URL query parameters
    query_params = request.args
    # Only attempt to open file if it exists
    if os.path.exists(filepath):
        lines = read_file(filepath, query_params)
        return render_template('file_view.html', lines=lines)
    # Raise 404 if file does not exist
    else:
        return raise_404(404)

@app.route('/error/<name>')
def handle_exception(name):
    return render_template('error_details.html', name=name)

@app.errorhandler(404)
def raise_404(error):
    return render_template('404.html'), 404


# This ensures code block only executes when this script is run.
if __name__ == '__main__':
    app.run(host='localhost', port=5000)