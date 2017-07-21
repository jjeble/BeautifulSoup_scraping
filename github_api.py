import requests,json
from collections import Counter
from dateutil.parser import parse
url = "https://api.github.com/users/jjeble/repos"
repos = json.loads(requests.get(url).text)
dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

last_5_repo = sorted(repos,key = lambda r:r["created_at"],reverse = True)[:5]

last_5_lang = [repo["language"] for repo in last_5_repo]

print(month_counts)
print(weekday_counts)
print(last_5_lang)
