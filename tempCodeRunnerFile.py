from youtube_transcript_api import YouTubeTranscriptApi

def getVideoTranscript(video_link):
    video_id = video_link.split("v=")[-1].split('&')[0]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None
    
transcript = getVideoTranscript("https://www.youtube.com/watch?v=T-D1OfcDW1M&t=18s")
print(
   transcript 
) 