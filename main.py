from pytube import YouTube


link = "https://www.youtube.com/watch?v=m1sOENnFd_k"
yt = YouTube(link)


print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
print("Rating of video: ", yt.rating)
ys = yt.streams.get_highest_resolution()

# Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
