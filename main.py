'''
╔╗╔╗╔══╗╔══╗╔═══╗╔╗───
║║║║║╔═╝║╔╗║║╔═╗║║║───
║║║║║║──║║║║║╚═╝║║╚══╗
║║╔║║║──║║║║║╔══╝║╔═╗║
║╚╝║║║──║╚╝║║║───║╚═╝║
╚══╝╚╝──╚══╝╚╝───╚═══╝

╔╗──╔╗╔══╗╔╗╔══╗╔══╗╔╗╔╗╔╗──╔╗
║║──║║║╔╗║║║║╔═╝║╔═╝║║║║║║──║║
║╚╗╔╝║║╚╝║║╚╝║──║║──║║║║║╚╗╔╝║
║╔╗╔╗║║╔╗║║╔╗║──║║──║║╔║║╔╗╔╗║
║║╚╝║║║║║║║║║╚═╗║╚═╗║╚╝║║║╚╝║║
╚╝──╚╝╚╝╚╝╚╝╚══╝╚══╝╚══╝╚╝──╚╝
'''

from flask import Flask, render_template, request, redirect
from feedback_mail import send_mail

app = Flask(__name__)


@app.errorhandler(404)
def not_found_page(e):
    return render_template('not_found.html')


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/feedback", methods=['POST', 'GET'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        try:
            send_mail(name, email, message)
            return render_template('successfully.html')
        except:
            return 'Error with sending message!'
    else:
        return render_template('feedback.html')


@app.route('/maps')
def maps():
    return render_template('maps.html')


if __name__ == '__main__':
    app.run(debug=True)

