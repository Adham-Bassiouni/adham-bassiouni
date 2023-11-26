from flask import Flask, render_template
site =Flask(__name__)
@site.route("/")
def home():
    return render_template("Adham.html")
@site.route("/site1")
def site1():
    return render_template("site1.html")
@site.route("/site2")
def site2():
    return render_template("site2.html")
@site.route("/site3")
def site3():
    return render_template("site3.html")
@site.route("/site4")
def site4():
    return render_template("site4.html")


if __name__=="__main__":
    site.run(debug = True , port = 500)
    