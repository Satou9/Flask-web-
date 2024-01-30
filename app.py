from flask import Flask, render_template

app = Flask(__name__)

PRODUCTS = [
    {
        'id': 1,
        'title': 'Blush',
        'price': '20',

    },
    {
        'id': 2,
        'title': 'Eyeshadow',
        'price': '30',

    }, 
    {
        'id': 3,
        'title': 'Highlighter',
        'price': '40',

    },
]

#from .view import view
#from .auth import auth


#app.register_blueprint(view, url_prefix='/')
#app.register_blueprint(auth, url_prefix='/')

 
@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS)




if __name__ == '__main__':
    app.run(debug=True)
