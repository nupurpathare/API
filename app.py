from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow Cross-Origin Requests

# Mood-to-Track Mapping
mood_to_track = {
    "Calm": "Settle comfortably. Close your eyes gently. Take a deep breath in, and slowly exhale, letting go. Notice your body relaxing, bit by bit. Feel a wave of calm washing over you. Rest in this stillness for a moment. Gently bring your awareness back when you're ready.",
    "Relax": "Find a comfortable spot. Close your eyes or soften your gaze. Imagine a peaceful natural scene. Hear the gentle sounds around you. Feel the ease and tranquility. Simply be present with these soothing sounds for a few moments. Return to the present when you're ready.",
    "Focus": "With headphones on, sit still. Close your eyes. Focus on your breath, the inhale and exhale. Notice any thoughts, and gently guide your attention back to your breath. Allow the binaural beats to support your focus for a short time. Return to full awareness when you choose.",
    "Anxious": "Sit or lie down comfortably. Take a deep breath in, hold, and release slowly. Notice any tension in your body. Breathe into that tension, and as you exhale, let it go. Imagine a sense of calm surrounding you. Rest here briefly. Gently open your eyes when you feel ready."
}

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    mood = data.get("mood")
    
    track = mood_to_track.get(mood, "Default Meditation Track")
    
    return jsonify({"track": track})

if __name__ == '__main__':
    app.run(debug=True)
