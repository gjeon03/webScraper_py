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
	results = soup.find_all("h2", {"class": "jobTitle"})
	for result in results:
		title = result.find_all("span")
		for title_item in title:
			if title_item.get("title") is not None:
				jobs.append(title_item.get("title"))
				print(title_item.get("title"))
	return jobs