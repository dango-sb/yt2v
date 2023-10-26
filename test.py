from pytube import Playlist, YouTube
import os

# Input the YouTube playlist URL
playlist_url = input("Enter the YouTube playlist URL: ")

try:
    # Create a Playlist object
    playlist = Playlist(playlist_url)

    # Extract all the video URLs from the playlist
    video_urls = playlist.video_urls

    # Provide the path where you want to save the audio files
    save_path = input("D:\Music\Between Here And Now")

    for url in video_urls:
        try:
            # Create a YouTube object for the video
            yt = YouTube(url)

            # Get the stream with the audio only (in the highest quality available)
            audio_stream = yt.streams.filter(only_audio=True).first()

            # Download the audio
            audio_stream.download(output_path=save_path)

            # Rename the downloaded file to have a .mp3 extension
            original_filename = audio_stream.default_filename
            new_filename = original_filename.replace(".mp4", ".mp3")
            os.rename(os.path.join(save_path, original_filename), os.path.join(save_path, new_filename))

            print(f"Audio downloaded: {new_filename}")

        except Exception as e:
            print(f"An error occurred for video at {url}: {str(e)}")

    print("All audio files downloaded successfully!")

except Exception as e:
    print("An error occurred:", str(e))

