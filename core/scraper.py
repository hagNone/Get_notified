import requests

"""Function to scrape events from Unstop"""
def fetch_unstop_events(per_page=20):
    # PUBLIC API URL for Unstop competitions
    url = "https://unstop.com/api/public/opportunity/search-result"
    
    # PArameters for the API requests
    params = {
        "opportunity": "competitions",
        "page": 1,
        "per_page": per_page,
        "oppstatus": "open",
        "domain": 2,
        "course": 6,
        "specialization": "Artificial Intelligence and Machine Learning Engineering",
        "usertype": "students",
        "passingOutYear": 2026
    }

    # Headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json",
        "Referer": "https://unstop.com/",
        "Cookie": "_ga=GA1.1.1118182141.1752814661; country=IN; unLang=en"
    }

    # Fetaching data from the Unstop API
    try:
        res = requests.get(url, headers=headers, params=params)
        res.raise_for_status()
        competitions = res.json().get("data", {}).get("data", [])

        print(" Unstop Events")
        for i, comp in enumerate(competitions, 1):
            title = comp.get('title', 'No Title')
            org = comp.get('organisation', {}).get('name', 'Unknown Org')
            link = f"https://unstop.com{comp.get('seo_url', '')}"
            tags = [tag['name'] for tag in comp.get('filters', [])]
            banner = comp.get('banner_mobile', {}).get('image_url', '')

            print(f"\n Competition #{i}")
            print(f" Title: {title}")
            print(f" Organization: {org}")
            print(f" Link: {link}")
            print(f" Tags: {', '.join(tags) if tags else 'None'}")
            if banner:
                print(f" Banner: {banner}")

    except Exception as e:
        print(" Unstop error:", e)


# Function to scrape events from Hack2Skill
def fetch_hack2skill_events():
    url = "https://vision.hack2skill.com/api/v1/innovator/public/event/public-list"
    # Parameters for the API requests
    params = {
        "page": 1,
        "records": 20,
        "search": "",
        "start": "2023-07-18T05:29:41.122Z",
        "end": "2026-07-18T05:29:41.122Z"
    }
    # Headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    # Fetching data from the Hack2Skill API
    try:
        res = requests.get(url, headers=headers, params=params)
        res.raise_for_status()
        events = res.json().get("data", [])

        print("\n🔷 Hack2Skill Events")
        for i, event in enumerate(events, 1):
            title = event.get('title', 'No Title')
            link = f"https://hack2skill.com/events/{event.get('eventUrl', '')}"
            tags = [event.get('mode'), event.get('participation'), event.get('flag')]
            banner = event.get('thumbnail', '')

            print(f"\n Event #{i}")
            print(f" Title: {title}")
            print(f" Link: {link}")
            print(f" Tags: {', '.join(filter(None, tags))}")
            if banner:
                print(f" Banner: {banner}")

    except Exception as e:
        print(" Hack2Skill error:", e)

# Function to fetch all events from both Unstop and Hack2Skill
def fetch_all_events():
    return fetch_unstop_events() + fetch_hack2skill_events()