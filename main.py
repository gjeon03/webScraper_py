import requests

indeed_resul = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch")

print(indeed_resul.text)