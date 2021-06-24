from flask import Flask
app=Flask(__name__)



@app.route('/')
def highlow():
    return "<h1>Guess a number between 0 and 9</h1> <img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif width=200px> "
@app.route('/<int:number>')
def another(number):
    ar=number
    import random as rd
    rn=rd.randint(1,7)
    if (ar==rn):
        return "<p>Number Matched</p> <img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif width=200px>"
    elif ar>rn:

        return "<p>Number Higher</p> <img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif width=200px>"
    else:

        return "<p>Number Lower</p> <img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif width=200px>"
if __name__=="__main__":
    app.run(debug=True)