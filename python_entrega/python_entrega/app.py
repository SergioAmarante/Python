from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])

def home():
    
    if(request.method == "GET"):
      return render_template("index.html")
    else:
      if (request.form["num1"] !="" and request.form["num2"] !=""):
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        
        if (request.form["opera"] == "soma"):
          soma = int(num1) + int(num2)
          opera = "Soma"
          return render_template("index.html",operador=opera,resultado=str(soma))
          

        elif (request.form["opera"] == "subt"):
          subt = int(num1) - int(num2)
          opera = "Subtração"
          return render_template("index.html",operador=opera,resultado=str(subt))
        
        elif (request.form["opera"] == "mult"):
          mult = int(num1) * int(num2)
          opera = "Multiplicação"
          return render_template("index.html",operador=opera,resultado=str(mult))
        
        else:
          divi = int(num1) // int(num2)
          opera = "Divisão"
          return render_template("index.html",operador=opera,resultado=str(divi))
            
      else:
       return render_template("index.html",alerta="informar um numero valido")
   

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

app.run(port=8080, debug=True)
