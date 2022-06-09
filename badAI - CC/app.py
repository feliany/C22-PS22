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
    "Categorical_Adam_fix.h5", custom_objects={'KerasLayer': hub.KerasLayer})


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
        imagefile = request.files['photo']
        test_image = prepare_image(imagefile)

        result = model.predict(test_image)
        label1 = return_label(result[0])
        prediction = ''
        description = ''
        solution = ''

        if result[0][label1] < 0.5:
            prediction += 'your pic not scalp'
            description += 'wrong input image'
            solution += 'please input scalp image'
        elif label1 == 0:
            prediction += 'Alopecia Areata'
            description += 'Right, it is hair loss and sadly it reaches alopecia areata symptoms. It is an autoimmune disorder that causes your hair to come out. The amount of hair loss is different for everyone. Some people lose it only in a few spots and others sadly lose a lot. Sometimes, hair grows back but falls out again later. In others, hair grows back for good.'
            solution += 'Find haircare products that focus on hair loss and don\'t forget to see your dermatologist.'
        elif label1 == 1:
            prediction += 'Dandruff'
            description += 'Those dry, white flakes of skin you brush off your collar or shoulders are called DANDRUFF. It is harmless, but you know it can be embarrassing and itchy. Dandruff isn\'t about your hair, or how often you wash it. Instead, it\'s about the skin on your scalp.'
            solution += 'Find haircare products that focus on hair loss and don\'t forget to see your dermatologist if you think you need it.'
        elif label1 == 2:
            prediction += 'Folliculitis'
            description += 'You got bacteria or a blockage in a tiny pocket in your skin called a hair follicle. Yes, it is folliculitis. Just to add to your knowledge, you have hair follicles just about everywhere you have hair and on the soles of your feet. Folliculitis can make these hair follicles red and swollen.'
            solution += 'You need to see your dermatologist as soon as possible.'
        elif label1 == 3:
            prediction += 'Healthy Scalp'
            description += 'Your hair shines brighter than the sun. Congratulations or should I say \'Good Job\' instead?. Keep maintaining your hair using the products that you think that work for your hair.'
            solution += 'Good Job'
        elif label1 == 4:
            prediction += 'Psoriasis'
            description += 'Your skin cells multiply up to 10 times faster than normal and these symptoms are called psoriasis. This makes the skin build up into bumpy red patches covered with white scales. They can grow anywhere, but most appear on the scalp, elbows, knees, and lower back. Psoriasis can\'t be passed from person to person. It does sometimes happen in members of the same family.'
            solution += 'Moisture your skin and see your dermatologist for better treatment and most importantly to avoid contagion.'
        elif label1 == 5:
            prediction += 'Seborrheic dermatitis'
            description += 'You got Seborrheic dermatitis! A common skin condition that mainly affects your scalp. It causes scaly patches, red skin, and stubborn dandruff. If you are born with a naturally oily scalp, you are more likely to get this. It might look similar to psoriasis, eczema, or an allergic reaction. It usually happens on your scalp, but you can get it anywhere on your body.'
            solution += 'You can try looking for over-the-counter dandruff shampoos that contain selenium, zinc pyrithione or coal tar, and shampoo with it twice a week or as directed on the label of the product. If it doesn\'t help, you can go see a dermatologist.'
        elif label1 == 6:
            prediction += 'Tinea Capitis'
            description += 'You got Tinea Capitis, which can also be called Ringworm! It is a rash caused by a fungal infection. It usually causes itchy, scaly, bald patches on the head. Ringworm gets its name because of its circular appearance. Don\'t worry, no worm is involved. But, be careful! It is a contagious infection.'
            solution += 'Go see a dermatologist as soon as possible for better treatment and most importantly to avoid contagion.'

        os.remove("images/{}".format(imagefile.filename))
    else:
        prediction = ''
        description = ''
        solution = ''
    return jsonify(prediction=prediction, description=description, solution=solution)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
