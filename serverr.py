# python assignment 1
# request scoreboard data from ctf website
import requests
import json
from datetime import datetime

def fetch_ctf_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def validate_flag(api_key):
    api_url = f"http://sakura.apoorvctf.xyz:5050/?apiKey={api_key}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        flag_data = response.json()
        print("\n🔹 Flag Validation Result 🔹")
        print(json.dumps(flag_data, indent=4))
    except requests.RequestException as e:
        print(f"Error validating flag: {e}")

def format_time(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def display_scoreboard(data):
    if not data:
        print("No data to display.")
        return

    print("\n🏆 CTF Scoreboard 🏆\n")
    print(f"{'Position':<8} {'Team':<30} {'Score':<6}")
    print("-" * 50)

    for team in data.get('standings', []):
        pos = team.get('pos', '')
        team_name = team.get('team', '')
        score = team.get('score', 0)
        print(f"{pos:<8} {team_name:<30} {score:<6}")

        task_stats = team.get('taskStats', {})
        if task_stats:
            print(f"\n{'Task':<40} {'Points':<6} {'Completion Time':<20}")
            print("-" * 70)
            for task_name, stats in task_stats.items():
                points = stats.get('points', 0)
                time = format_time(stats.get('time', 0))
                print(f"{task_name:<40} {points:<6} {time:<20}")
            print("\n" + "-" * 70 + "\n")

def main():
    api_url = 'https://apoorvctf.iiitkottayam.ac.in/api/v1/ctftime'
    ctf_data = fetch_ctf_data(api_url)
    display_scoreboard(ctf_data)
    validate_flag(api_key)

if __name__ == "__main__":
    main()
