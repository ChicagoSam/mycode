# Xavier's School for Gifted Youngsters!

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

leader= "Prof X"
availmutants= ["cyclops","wolverine","jean grey","beast"]

@app.route("/")
def landing():
    return render_template("mutants.html", 
                           hero= leader,
                           mutant_list= availmutants
                          )

# add a new mutant to duty roster
@app.route("/xmen", methods=["POST"])
def grabnewmutant():
    # grab the name of the new mutant
    # add that name to the list above
    mutant_name= request.form.get("mutantvar") # <-- grab the value of a variable off a FORM

    # mutant = hero the user typed in
    availmutants.append(mutant_name)

    # every route must ALWAYS return something!
    return redirect("/")

# Remove a mutant from the duty roster
@app.route("/removemutant", methods=["POST"])
def removemutant():
    mutant_to_remove = request.form.get("mutant_to_remove")
    if mutant_to_remove in availmutants:
        availmutants.remove(mutant_to_remove)
    return redirect("/")

app.run(host="0.0.0.0", port=2224, debug=True)
