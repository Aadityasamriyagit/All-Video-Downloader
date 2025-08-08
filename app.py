from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import yt_dlp
import re

app = Flask(__name__)
CORS(app)

def sanitize_filename(filename):
    """Removes special characters to make a safe filename."""
    return re.sub(r'[\\/*?:"<>|]', "", filename)

# This is the main page of your website
@app.route('/')
def home():
    """Serves the index.html file to the user."""
    return render_template('index.html')

# This is the backend brain that gets the video info
@app.route('/get_video_info', methods=['GET'])
def get_video_info():
    """Takes a video link and returns a list of formats."""
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "URL parameter is missing"}), 400

    ydl_opts = {'noplaylist': True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            
            formats_list = []
            for f in info.get('formats', []):
                filesize = f.get('filesize') or f.get('filesize_approx')
                # We only add formats that have a direct download URL
                if filesize and f.get('url'):
                    formats_list.append({
                        "format_id": f.get('format_id'),
                        "ext": f.get('ext'),
                        "resolution": f.get('resolution', 'Audio'),
                        "filesize_bytes": filesize,
                        "download_url": f.get('url') # This is the direct link to the video file
                    })
            
            # Put the best quality formats at the top
            formats_list.sort(key=lambda x: x['filesize_bytes'], reverse=True)
            
            return jsonify({
                "title": sanitize_filename(info.get('title', 'Untitled')),
                "formats": formats_list
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500