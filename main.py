from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def root():
    return """ 
   <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Hello World</title>
            
           <!-- Google tag (gtag.js) -->
            <script async src="https://www.googletagmanager.com/gtag/js?id=G-QY0W6CSL6X"></script>
            <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());

            gtag('config', 'G-QY0W6CSL6X');
            </script>
        </head>
        <body>
            <h1>Hello World</h1>
            <button id="analyticsButton">Click</button>

            <script>
                document.getElementById("analyticsButton").addEventListener("click", function () {
                    gtag('event', 'button_click', {
                        'event_category': 'Button',
                        'event_label': 'Button Clicked'
                    });
                });
            </script>
        </body>
        </html>
    """

# def hello_world(): 
#     prefix_google = """
#     <!-- Google tag (gtag.js) -->
#     <script async 
#     src="https://www.googletagmanager.com/gtag/js?id=G-QY0W6CSL6X"></script>
#     <script>
#         window.dataLayer = window.dataLayer || []; 
#         function gtag(){dataLayer.push(arguments);} 
#         gtag('js', new Date());
#         gtag('config', 'G-QY0W6CSL6X'); 
#     </script>
#       """
#     return prefix_google + "Hello World"

# def hello_world():
#     return 'Hello World'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
