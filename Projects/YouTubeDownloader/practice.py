# # pip install pytube --> run in your terminal

# from pytube import YouTube
# link = "https://www.youtube.com/watch?v=-yuY4oxyUPQ&list=RD-yuY4oxyUPQ&start_radio=1"
# youtube_1 = YouTube(link)
# # print(youtube_1.title)
# # print(youtube_1.thumbnail_url)
# videos = youtube_1.streams.all()
# vid = list(enumerate(videos))#--> enumerate give us the index number
# for i in vid:
#     print(i)
# print()
# strm = int(input("Enter: "))
# videos[strm].download()
# print("Successfully Downloaded")

#-------------------------------------------< code From ChatGPT >-------------------------------------------------
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

try:
    link = "https://www.youtube.com/shorts/F3LJou_5zTI"
    youtube_1 = YouTube(link)
except RegexMatchError:
    print("Error: Invalid YouTube URL")
    exit(1)
except VideoUnavailable:
    print("Error: Video is unavailable")
    exit(1)
except Exception as e:
    print(f"Error fetching YouTube link: {e}")
    exit(1)

try:
    videos = youtube_1.streams.all()
    if not videos:
        print("Error: No streams available")
        exit(1)
    vid = list(enumerate(videos))  # enumerate gives us the index number
    for i in vid:
        print(i)
    print()
except Exception as e:
    print(f"Error fetching video streams: {e}")
    exit(1)

try:
    strm = int(input("Enter the index number of the desired stream: "))
    if strm < 0 or strm >= len(videos):
        raise ValueError("Invalid index number")
except ValueError as ve:
    print(f"Error: {ve}")
    exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    exit(1)

try:
    videos[strm].download()
    print("Successfully Downloaded")
except Exception as e:
    print(f"Error during download: {e}")

