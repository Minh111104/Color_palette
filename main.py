from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
from werkzeug.utils import secure_filename
import os
from PIL import Image
import numpy as np
from collections import Counter

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['UPLOAD_FOLDER'] = 'static/uploads'


class UploadPictureForm(FlaskForm):
    picture = FileField(
        'Upload Picture',
        validators=[
            FileRequired(),
            FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')
        ]
    )
    submit = SubmitField('Upload')


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


# This function extracts the top N colors from an image
def get_top_colors(image_path, top_n=100):
    img = Image.open(image_path).convert('RGB')
    img_array = np.array(img)
    pixels = img_array.reshape(-1, 3)
    color_counts = Counter(tuple(color) for color in pixels)
    most_common_colors = color_counts.most_common(top_n)

    return [(color, rgb_to_hex(color), count) for color, count in most_common_colors]


@app.route('/', methods=['GET', 'POST'])


# This route handles the file upload and color extraction
def upload():
    form = UploadPictureForm()
    if form.validate_on_submit():
        picture_file = form.picture.data
        filename = secure_filename(picture_file.filename)
        picture_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Picture uploaded successfully!', 'success')
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        top_colors = get_top_colors(file_path)
        return render_template('results.html', image_path=file_path, colors=top_colors)
    return render_template('upload.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

