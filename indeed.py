import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&l=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&limit={LIMIT}"

def extract_indeed_pages():
	resul = requests.get(URL)
	soup = BeautifulSoup(resul.text, "html.parser")
	pagination = soup.find("div", {"class":"pagination"})
	links = pagination.find_all('a')
	pages = []
	for link in links[:-1]:
		pages.append(int(link.string))
	max_page = pages[-1]
	return max_page

def extract_indeed_jobs(last_page):
	jobs = []
	#for page in range(last_page):
	result = requests.get(f"{URL}&start={0 * LIMIT}")
	soup = BeautifulSoup(result.text, "html.parser")
	results = soup.find_all("div", {"class": "job_seen_beacon"})
	for result in results:
		title = result.find("h2", {"class": "jobTitle"})
		for title_item in title.find_all("span"):
			if title_item.get("title") is not None:
				title = title_item.get("title")
		company = result.find("span", {"class": "companyName"})
		if company is None:
			company = "No company name"
		elif company.find("a") is not None:
			company = str(company.find("a").string)
		else:
			company = str(company.string)
		print(f"*{title}*, *{company}*")
	return jobs