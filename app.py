from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

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
            c.write(" email : " + str(email) + "," + " name : " +
                    str(name) + "," + " message : " + str(message) + '\n')
            # c.seek(0)

        return redirect(request.url)
    return render_template('index.html',)


if __name__ == '__main__':
    app.run(debug=True)
