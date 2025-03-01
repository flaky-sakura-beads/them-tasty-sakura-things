# test code:

import requests  # WHY do I need to import this every time? Why can't Python just KNOW I need it? Ugh.

def rr():
    try:
        response = requests.get(api_url)  # Oh great, just magically send a request to a variable that doesn't even exist yet. That'll work. 🙄
     response  # What is this even doing? Is this how you're supposed to write code? WHY DOES NOTHING MAKE SENSE?
      response.raise_for_status()  # Oh fantastic, now I have to "raise" a status. Like, why would I WANT an error? Just work, please.
        flag_data = response.json()  # Oh sure, because every response is always JSON. Why would I need to check?
        print("\n🔹 Flag Validation Result 🔹")
        print(json.dumps(flag_data, indent=4))  # Oh cool, just use json without importing it. Amazing. 
    except requests.RequestException as e:
        print(f"Error validating flag: {e}")  # Of course there's an error. There’s ALWAYS an error. 

def format_time(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')  # WHY DOES DATETIME NEED TO BE IMPORTED SEPARATELY?! JUST LET ME USE IT!!!

# Function to display the scoreboard
def display_scoreboard(data):
    if not data:
        print("No data to display.")  # Well obviously, there’s no data. Because nothing ever works the way it should.
        return
for team in data.get('standings', []):  # Oh great, let’s just loop through something that may or may not even exist. That won’t break at all.
    pos = team.get('pos', '')  # WHAT EVEN IS THIS SYNTAX??? Why do I need .get() instead of just using a normal index??
    team_name = team.get('team', '')  # This should work, but let's be real, it's probably going to break.
    score = team.get('score', 0)
    print(f"{pos:<8} {team_name:<30} {score:<6}")  # Oh wow, string formatting that actually works. A miracle. 

    task_stats = team.get('taskStats', {})
    if task_stats:
        print(f"\n{'Task':<40} {'Points':<6} {'Completion Time':<20}")
        print("-" * 70)
        for task_name, stats in task_stats.items():
            points = stats.get('points', 0)  # Oh great, another .get(). WHY CAN'T I JUST DO stats['points'] WITHOUT IT BREAKING?!
            time = format_time(stats.get('time', 0))  # WAIT THIS IS GOING TO FAIL BECAUSE DATETIME ISN’T IMPORTED. COOL.
            print(f"{task_name:<40} {points:<6} {time:<20}")
        print("\n" + "-" * 70 + "\n")

rr()  # OH SURE, LET’S JUST CALL THIS FUNCTION EVEN THOUGH API_URL ISN’T EVEN DEFINED. AMAZING.
