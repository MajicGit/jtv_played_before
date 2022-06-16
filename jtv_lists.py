import requests
import json
videos = set()
for year in ["2021","2022"]:
    for week in range(0,52):
        try:
            r = requests.get(f"https://jungletv.live/raffles/weekly/{year}/{week}/tickets#",timeout=2)
        except:
            print("Encountered an error")
            print(f"Couldn't retrieve Data for week {week} and year {year}")
        body = r.text
        lines = body.rsplit("\n")

        for line in lines: 
            split = line.rsplit(",")
            if len(split) == 3 and split[0].isdigit():
                videos.add(split[1])

with open("Output.txt","w") as f:
    f.write(json.dumps(list(videos)))

while True:
    video = input("Video Id")
    if video in videos:
        print("Video has been played")
    else:
        print("Video might not have been played")