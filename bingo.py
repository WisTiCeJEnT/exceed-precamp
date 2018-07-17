from flask import Flask, request
import random

app = Flask(__name__)
lis = list(range(1,31))
count = 1
@app.route('/')
def root():
    global lis
    lis = list(range(1,31))
    return "<h2>Are you ready?<h/2>"

@app.route('/reset', methods = ['GET', 'POST'])
def reset():
    global lis
    global count 
    count += 1
    lis = list(range(1,31))
    return "<h1>"+"Reseted"+"</h1>" +"<h5>Game "+str(count)+" ready.</h5>" 

@app.route('/random', methods = ['GET', 'POST'])
def rand():
    global lis
    r = random.randint(0,len(lis)-1)
    return "<h1>"+str(lis.pop(r))+"</h1>"+"<h5>There are "+str(len(lis))+" number(s) left.</h5>"
    


if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)

