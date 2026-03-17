from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()

def getVideoTranscript(video_link = "https://www.youtube.com/watch?v=dFHEgsJTmDI"):
    video_id = video_link.split("v=")[-1].split('&')[0]
    try:
        transcript = ytt_api.fetch(video_id)
        return (transcript, video_id)
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None
    
# the following code only runs if this script is executed directly, and not imported as a module
if __name__ == "__main__":
    transcript = getVideoTranscript("https://www.youtube.com/watch?v=dFHEgsJTmDI")
    print(
    transcript 
    )   