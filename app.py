from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

path = "simple.txt"


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":

        req = request.form

        name = req.get("name")
        email = req["email"]
        message = request.form["message"]
        print(req)
        with open(path, "a+") as c:
            c.write(" email : " + str(email) + " name : " +
                    str(name) + " message : " + str(message) + '\n')
            c.seek(0)

        return redirect(request.url)
    return render_template('index.html',)


if __name__ == '__main__':
    app.run(debug=True)


#path_1 = "simple.txt"
#
#
# def read_file_content(path):
#
#    with open(path_1, "r+") as c:
#        c.write(first + '\n')
#        c.write(second + '\n')
#        c.seek(0)
#        c.read()
#
# read_file_content(path_1)
