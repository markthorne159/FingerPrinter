#!python2

import os
from flask import Flask,render_template,request

class FPrint():

    def Create(self):

        F_Printer = Flask(__name__)
        port = int(os.environ["PORT"])#9999

        @F_Printer.route('/',methods=["GET"])
        def main():

            #Do finger-printing work here?
            Name = os.name
            print (Name)
            print (request.headers.get("User-Agent"))
            print(request)

            #Render the main page.
            return render_template("index.html")


        F_Printer.run(port=port,host="0.0.0.0")


F = FPrint()
F.Create()
