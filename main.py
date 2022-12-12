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
            return redirect('/')
        except:
            return 'Error with sending message!'
    else:
        return render_template('feedback.html')


if __name__ == '__main__':
    app.run(debug=True)

