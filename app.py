from flask import Flask,url_for,request,render_template
import sqlite3

import joblib
model = joblib.load('randomforest.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route("/prediction",methods=['GET','POST'])
def prediction():
    if  request.method == "POST":
        name = request.form['name']
        age = int(request.form["age"])
        bmi = int(request.form["bmi"])
        children = int(request.form["children"])
        gender = int(request.form["gender"])
        smoker = int(request.form["smoker"])
        region = request.form["region"]
        northwest = 0
        southeast = 0
        northeast = 0
        if region == 'northwest':
            northwest = 1
        elif region == 'southeast':
            southeast = 1
        elif region == 'northeast':
            northeast = 1

        conn = sqlite3.connect("userdata.db")
        conn.execute("""
                    insert into userrecord(
                        name, age, bmi, gender, children, smoker, region, northwest, southeast, northeast)
                        values(?,?,?,?,?,?,?,?,?,?) """,
                        (name, age, bmi, gender, children, smoker, region, northwest, southeast, northeast))
        conn.commit()
        conn.close()

        UNSEEN_DATA = [[age, bmi, children, gender, smoker, northwest, southeast, northeast]]
        
        prediction = model.predict(UNSEEN_DATA)
        output = round(prediction[0],2)

        # return label[str(prediction)]
        return render_template('result.html',
                               output=output,
                               name=name,
                               age=age,
                               bmi=bmi,
                               children=children,
                               gender='Male' if gender == 1 else 'Female',
                               smoker='Yes' if smoker == 1 else 'No',
                               region=region.capitalize()
                            )

if __name__ == "__main__":
    app.run(debug=True)