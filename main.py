from flask import Flask, render_template, request, redirect
from so import get_jobs as get_so_jobs

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/report")
def report():
	word = request.args.get('word')
	if word:
		word = word.lower()
		existingJobs = db.get(word)
		if existingJobs:
			jobs = existingJobs
		else:
			jobs = get_so_jobs(word)
			db[word] = jobs
	else:
		return redirect("/")
	return render_template("report.html", 
	searchinhBy=word,
	resultsNumber=len(jobs),
	jobs=jobs
	)

app.run()