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
	for page in range(last_page):
		result = requests.get(f"{URL}&start={page * LIMIT}")
		print(result.status_code)