import requests
import json
videos = {}
print("Querying for videos, this may take a while")
for year in ["2021","2022"]:
    for week in range(1,53):
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
                video_id = split[1]
                if video_id in videos:
                    videos[video_id] = videos[video_id] + 1
                else:
                    videos[video_id] = 1 
print("Got all the videos, saving to file")
with open("Output.txt","w") as file:
    file.write("Video ID, Number of times played \n")
    for video_id,num_plays in sorted(videos.items(),key= lambda x:x[1],reverse=True): #Sort videos by number of plays
        file.write(f"{video_id}, {num_plays} \n")

print("Infinite querying of specific Video IDs:")
while True:
    video = input("Video Id: ")
    if video in videos:
        print("Video has been played")
    else:
        print("Video might not have been played")