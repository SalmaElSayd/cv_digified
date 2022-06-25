import random
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import video_predictor
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ENV'] = 'development'

app.config['CONFIG'] = True

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/predict_video', methods=['POST'])
def predict_video():  # put application's code here
    f = request.files['video']
    # creating a random number as a prefic for the video name
    rand = random.randint(100,1000000);
    file_path = 'uploads/vid{}{}'.format(rand,secure_filename(f.filename))
    f.save(file_path)  # saving video to uploads folder
    result= video_predictor.__main__(file_path)  # getting predictions
    os.remove(file_path)  # deleting video after prediction is done for data privacy
    return render_template('result.html', res=result)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port,debug=False, use_reloader=False)
