from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
   return render_template(
		"index.html",
		#cpuUsage=cpu_Usage,
		#cpuTemp=cpu_Temperature
		)



if __name__ == "__main__":
   app.run(debug=False)