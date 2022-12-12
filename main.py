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

from flask import Flask, render_template
from feedback_mail import send_mail

app = Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/feedback")
def feedback():
    return render_template('feedback.html')


if __name__ == '__main__':
    app.run(debug=True)

