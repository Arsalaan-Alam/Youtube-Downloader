# Importing Dependency
from pytube import YouTube

# Add your link here
link = input("Enter the link of YouTube video which has to be downloaded:  ")
yt = YouTube(link)

# Video Info
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
print("Rating of video: ", yt.rating)
ys = yt.streams.get_highest_resolution()

# Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
