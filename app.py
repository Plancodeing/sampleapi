
import os
from flask import Flask, flash, request, redirect, render_template




app=Flask(__name__)




@app.route('/')
def upload_form():
    return render_template('selecttype.html')
@app.route('/home.html')
def upload_form2():
    return render_template('home.html')
 



if __name__ == "__main__":
    app.run()
