from flask import Flask , render_template , request,flash,url_for
import random,string
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
app = Flask(__name__)

import pickle

# open a file, where you stored the pickled data
file = open('covid_predicting_model.pkl', 'rb')
classification_model = pickle.load(file)
file.close()

@app.route("/", methods=["GET","POST"])
def index():
   if request.method == "POST":
      all_data = request.form
      #print(all_data)
      runnyNose = int(all_data['runnyNose'])
      fever = int(all_data['fever'])
      sorethroat = int(all_data['sorethroat'])
      diffBreath = int(all_data['diffBreath'])
      headache = int(all_data['headache'])
      # Code for inference
      inputFeatures = [runnyNose, fever, sorethroat, diffBreath, headache]
      infection_probability =classification_model.predict_proba([inputFeatures])[0][1]
      #print(infection_probability)

      if(infection_probability>=0.5):
         return render_template('danger.html',infection_probability = round(infection_probability*100))
      else:
         return render_template('show.html', infection_probability = round(infection_probability*100))
   return render_template('index.html')
   # return "<p>Hello, World!</p>" + str(infection_probability)


@app.route('/show')
def show():
   return render_template('schedule_test.html')

@app.route('/danger')
def danger():
    return render_template('schedule_test.html')

@app.route('/about')
def about():
    return render_template('about.html')




#here is the code that works well with the flask flashing message flash is shown properly

@app.route('/schedule',methods=['POST'])
def schedule():

   if request.method=="POST":
      booked_data = request.form
      text_msg=''
      btn=''

 
      btn='Done'
      text_msg = 'ThankYou, Booked Date: '+booked_data['date']+'. You will be notified over email shortly!!'
      msg = 'Hi, '+ booked_data['fname']
      request_data = {
                  'text_msg':text_msg,
                  'btn':btn
             }
      flash(msg,'success')
      #or
      #return redirect(url_for('schedule_test',**request_data))
      return render_template('schedule_test.html',**request_data)
   return render_template('schedule_test.html')




if __name__ == "__main__":
   result = ''.join((random.choice(string.ascii_lowercase) for x in range(20))) # run loop 
   app.secret_key = result
   app.run(debug=True)









   '''
booked_data = request.form
      text_msg=''
      btn=''

 
      btn='Done'
      text_msg = 'ThankYou, Booked Date: '+booked_data['date']+'. You will be notified over email shortly!!'
      msg = 'Hi, '+ booked_data['fname']
      request_data = {
                  'text_msg':text_msg,
                  'btn':btn
             }
      flash(msg,'success')
   '''
