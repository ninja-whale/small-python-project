from pytube import YouTube

def on_complete(streams, filepath):
    print('download complete')
    print('filepath')

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100), 2)}%'
    print(progress_string)


link = input("Youtube link: ")

video_object = YouTube(link, on_complete_callback= on_complete, on_progress_callback= on_progress)

print(f'title : {video_object.title}')
print(f'length : {round(video_object.length / 60, 2)} minutes')
print(f'views : {video_object.views/1000000} million')
print(f'author : {video_object.author}')

#download
print('download: (b)est | (w)orst | (a)udio | (e)xit')
download_choice = input('choice: ')

match download_choice:
    case 'b':
        video_object.streams.filter(res="720p").first().download(r'C:\Users\payal\Downloads')
    case 'w':
        video_object.streams.get_lowest_resolution().download(r'C:\Users\payal\Downloads')
    case 'a':
        video_object.streams.get_audio_only().download(r'C:\Users\payal\Downloads')


