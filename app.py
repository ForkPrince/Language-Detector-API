from flask import Flask, request, jsonify
import ShortLanguageDetection

app = Flask(__name__)

detection = ShortLanguageDetection.Detector(reliable_min=0.5)

@app.route('/', methods=['GET', 'POST'])
def detect_language():
    if request.method == 'POST':
        try:
            data = request.json

            if "text" not in data:
                return jsonify(error="Missing 'text' field in request data"), 400

            text = data["text"]
            detected_language, is_reliable = detection.detect(text)

            response_data = {
                "language": detected_language,
                "reliable": is_reliable
            }

            return jsonify(response_data), 200
        except Exception as e:
            return jsonify(error=str(e)), 500

    elif request.method == 'GET':
        return "This endpoint supports POST requests for language detection. Use POST to detect language."

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
