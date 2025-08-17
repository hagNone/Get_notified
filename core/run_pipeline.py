from scraper import fetch_all_events

# Function to run the event fetching process     
def run():
    # Fetch events from both Unstop and Hack2Skill
    events = fetch_all_events()
    # Print the fetched events
    for event in events:
        print(f" [{event['platform']}] {event['title']}")
        print(f"{event['url']}\n")

# Entry point for the script
if __name__ == "__main__":
    run()
