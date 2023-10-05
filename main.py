from flask import Flask, render_template, request,make_response
import logging
import sys

# Create a Flask web application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__name__)
logs = []

# Define a route for the homepage
@app.route('/')
def root():
    return render_template("index.html")

@app.route('/logger', methods=['GET', 'POST'])
def logger_page():
    log_message ='This a log message'
    logger.info('This is a log message!')
    
    if request.method == 'POST' and 'log_message' in request.form:
        log_message = request.form.get('log_message')
        logger.info(log_message)
        # Render the HTML page
        return render_template('logger.html', logs=log_message)
    
    return render_template("logger.html", logs=log_message)
# Run the application
if __name__ == '__main__':
    app.run(debug=True)
