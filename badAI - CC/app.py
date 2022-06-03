from flask import Flask, request, render_template, jsonify
from keras.applications.inception_v3 import preprocess_input
from keras_preprocessing.image import img_to_array
from keras_preprocessing.image import load_img
import shutil
import keras as keras
import numpy as np
import tensorflow_hub as hub
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "images"

model = keras.models.load_model(
    "Categorical_Adam.h5", custom_objects={'KerasLayer': hub.KerasLayer})


def return_label(array):
    largest = 0
    for x in range(0, len(array)):
        if(array[x] > largest):
            largest = array[x]
            y = x
    return y


def prepare_image(file):
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(image_path)
    fname = "images/{}".format(os.listdir('images/')[0])
    img = load_img(fname, target_size=(150, 150))
    img_array = img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array_expanded_dims)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        shutil.rmtree('images')
        os.makedirs('images')
        imagefile = request.files['imagefile']
        test_image = prepare_image(imagefile)

        result = model.predict(test_image)
        label1 = return_label(result[0])
        prediction = ''
        if label1 == 0:
            prediction += 'alopecia_areata'
        elif label1 == 1:
            prediction += 'dandruff'
        elif label1 == 2:
            prediction += 'folliculitis'
        elif label1 == 3:
            prediction += 'Healthy_scalp'
        elif label1 == 4:
            prediction += 'psoriasis'
        elif label1 == 5:
            prediction += 'seborrheic_dermatitis'
        elif label1 == 6:
            prediction += 'tinea_capitis'

        os.remove("images/{}".format(imagefile.filename))
    else:
        prediction = ''
    return jsonify(prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
