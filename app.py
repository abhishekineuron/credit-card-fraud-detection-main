from flask import Flask, render_template, request, send_file, jsonify
from src.exception import CustomException
from src.pipeline.train_pipeline import TrainingPipeline
from src.pipeline.predict_pipeline import PredictionPipeline
import os
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify("home")

@app.route("/train")
def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return "Training Completed."
    except CustomException as e:
        return str(e)

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    try:
        if request.method == 'POST':
            prediction_pipeline = PredictionPipeline(request)
            prediction_file_detail = prediction_pipeline.run_pipeline()
            return send_file(
                prediction_file_detail.prediction_file_path,
                download_name=prediction_file_detail.prediction_file_name,
                as_attachment=True
            )
        else:
            return render_template('upload_file.html')
    except CustomException as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
