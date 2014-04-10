# Flask Hello World

from flask import Flask

app=Flask(__name__)

# add error handling
app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")

# dynamic route

@app.route("/test")
@app.route("/test/<search_query>")



def hello_world():
	return "Hello, world???!!!"

def search(search_query):
	return search_query

def search():
	return "Hello"
	
if __name__=="__main__":
	app.run()
