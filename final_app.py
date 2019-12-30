from flask import Flask, render_template, json
import mysql.connector
from flask import Flask, render_template, json

app = Flask(__name__)

database = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="xxxxxxxxxx",
  database="anychart_db"
)

mycursor = database.cursor()

@app.route("/pie")
def chart_1():
	mycursor.execute("SELECT name, value FROM fruits ORDER BY value DESC LIMIT 5")
	data = mycursor.fetchall()
	chart = {
		"chart": {
			"type": "pie",
			"title": "Top 5 fruits",
			"data": data,
			"container": "container"
		}
	}
	return render_template("index.html", title = "Anychart Python template", chartData = json.dumps(chart))


@app.route("/bar")
def chart_2():
	mycursor.execute("SELECT name, value FROM fruits ORDER BY value DESC LIMIT 5")
	data = mycursor.fetchall()
	chart = {
		"chart": {
                         "container": "container",
                         "series":[
                          {"enabled":True,
                            "seriesType":"column",
                            "data": data
                         }],
			"title": "Top 5 fruits",
			"type":"column"
		}
	}
	return render_template("index.html", title = "Anychart Python template", chartData = json.dumps(chart))

if __name__ == "__main__": 
	app.run()