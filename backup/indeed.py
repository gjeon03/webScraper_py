import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&l=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&limit={LIMIT}"


def get_last_pages():
	resul = requests.get(URL, stream=True)
	soup = BeautifulSoup(resul.text, "html.parser")
	pagination = soup.find("div", {"class": "pagination"})
	links = pagination.find_all('a')
	pages = []
	for link in links[:-1]:
		pages.append(int(link.string))
	max_page = pages[-1]
	return max_page


def extract_job(html):
	title = html.find("h2", {"class": "jobTitle"})
	for title_item in title.find_all("span"):
		if title_item.get("title") is not None:
			title = title_item.get("title")
	company = html.find("span", {"class": "companyName"})
	if company is None:
		company = "No company name"
	elif company.find("a") is not None:
		company = str(company.find("a").string)
	else:
		company = str(company.string)
	location = html.find("div", {"class": "companyLocation"})
	if location is None:
		location = "No location information"
	else:
		location = location.string
	job_id = html.parent["data-jk"]
	return {
		'title': title,
		'company': company,
		'location': location,
		'link': f"https://kr.indeed.com/%EC%B1%84%EC%9A%A9%EB%B3%B4%EA%B8%B0?jk={job_id}"
	}


def extract_jobs(last_page):
	jobs = []
	for page in range(last_page):
		print(f"Scrapping Indeed: Page {page}")
		result = requests.get(f"{URL}&start={page * LIMIT}")
		soup = BeautifulSoup(result.text, "html.parser")
		results = soup.find_all("div", {"class": "slider_container"})
		for result in results:
			job = extract_job(result)
			jobs.append(job)
	return jobs

def get_jobs():
	last_pages = get_last_pages()
	jobs = extract_jobs(last_pages)
	return jobs
