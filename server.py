import os
import summary 
from flask import Flask, flash, request, redirect, url_for
from flask import send_from_directory, jsonify
from werkzeug.utils import secure_filename
from json import dumps
import upload_object 
import speech_api

from flask_cors import CORS, cross_origin

UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = set(['mp3','flac'])

app = Flask(__name__)
app.secret_key = 'super secret key'
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            upload_object.upload_blob("fruitvodka123",'./files/'+filename, filename)
            res=speech_api.transcribe()
#             res=['''
#             The Earth intercepts a lot of solar power a hundred and seventy-three thousand terawatts that's ten thousand times more power than the planet's population uses. So is it possible that one day the world could be completely reliant on solar energy to answer that question. We first need to examine house solar panels convert solar energy to electrical energy solar panels are made up of smaller units called solar cells. The most common solar cells are made from Silicon a semiconductor. That is the second most abundant element on Earth in a solar cell. Crystalline silicon is sandwiched between conductive layers. Each silicon atom is connected to its neighbors by four strong bonds, which keep the electrons in place. So no current can flow. Here's the key a silicon solar cell uses two different layers of silicon and n-type silicon has extra electrons and Pete.
# Silicon has extra space has four electrons cold holes where the two types of silicon meet electrons can wander across the PN Junction leaving a positive charge on one side and creating negative charge on the other you can think of light as the flow of tiny particles called photons shooting out from the sun. When one of these photons strikes the silicone cell with enough energy. It can knock an electron from its Bond leaving a whole the negatively charged electron and location of the positively charged hole are now free to move around but because of the electric field at the PN Junction, they'll only go one way the electron is drawn to the ends side while the whole is drawn to the peace sign the mobile electrons are collected by Thin metal fingers at the top of the cell from there. They flow through an external circuit doing electrical work like powering a light bulb before.
# Turning through the conductive aluminum sheet on the back each silicone cell only puts out half of Vault, but you can string them together in modules to get more power 12 photovoltaic cells are enough to charge a cell phone while it takes many modules to power an entire house electrons are the only moving Parts in a solar cell and they all go back where they came from. There's nothing to get worn out or used up. So solar cells can last for decades. So what's stopping us from being completely reliant on solar power?
# There are political factors that play not to mention businesses that Lobby to maintain the status quo, but for now, let's focus on the physical and logistical challenges and the most obvious of those is that solar energy is unevenly distributed across the planet some areas are sunnier than others. It's also inconsistent less solar energy is available on cloudy days or at night. So a total Reliance would require efficient ways to get electricity from Sunny spots to cloudy once and effective storage of energy. The efficiency of the cell itself is a challenge to if sunlight is reflected instead of absorbed or if dislodged electrons fall back into a hole before going through the circuit that photons energy is lost the most efficient solar cell yet still only converts 46% of the available sunlight to electricity and most commercial systems are currently 15 to 20%
# Efficient in spite of these limitations it actually would be possible to power the entire world with today's solar technology. We need the funding to build the infrastructure and a good deal with space estimates range from tens to hundreds of thousands of square miles, which seems like a lot but the Sahara Desert alone is over 3 million square miles in area. Meanwhile solar cells are getting better cheaper and are competing with electricity from the grid and Innovations, like floating solar Farms may change the landscape in Tire late thought experiments and there's the fact that over a billion people don't have access to a reliable electric grid, especially in developing countries many of which are sunny.
# So in places like that solar energy is already much cheaper and safer and available Alternatives like kerosene for Save finlander Seattle though effective solar energy may still be a little way off.
# ''']
            #global a
            a=summary.generate(res)
            print("sum")
            #return redirect(url_for('uploaded_file',filename=filename))
            return jsonify(a)
    return 


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

# @app.route('/summary', methods=['GET', 'POST'])
# def gen_summary():
#     print("hello")
    
#     #return a[0]

if __name__ == '__main__':
    app.debug = True
    app.run()
