from flask import Flask , render_template , request,flash,url_for
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
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

@app.route('/schedule_test',methods=['GET','POST'])
def schedule_test():

   if request.method=="POST":
      booked_data = request.form
      text_msg=''
      btn=''

      #print(booked_data)
      if(booked_data['fname']=='' or booked_data['lname']=='' or booked_data['email']=='' or booked_data['phonenumber']=='' or (booked_data['address1']=='' and booked_data['address2']=='') or booked_data['city']=='') or booked_data['state']=='' or booked_data['pin']=='' or booked_data['date']=='': 
         btn = 'Proceed'
         text_msg = 'Fill All The Fields To Book Your Slot.'

         request_data = {
                 'fname': booked_data['fname'],
                 'lname': booked_data['lname'],
                 'email': booked_data['email'],
                 'phonenumber': booked_data['phonenumber'],
                 'address1': booked_data['address1'],
                 'address2': booked_data['address2'],
                 'state': booked_data['state'],
                 'pin': booked_data['pin'],
                 'date': booked_data['date'],
                 'text_msg':text_msg,
                 'btn':btn
             }
         flash('Fields Empty!!','error') #message and followed by category is apssed in the flash message
         
      else:
         btn='Done'
         text_msg = 'ThankYou, Booked Date: '+booked_data['date']+'. You will be notified over email shortly!!'
         msg = 'Hi, '+ booked_data['fname']
         request_data = {
                 'fname': booked_data['fname'],
                 'lname': booked_data['lname'],
                 'email': booked_data['email'],
                 'phonenumber': booked_data['phonenumber'],
                 'address1': booked_data['address1'],
                 'address2': booked_data['address2'],
                 'state': booked_data['state'],
                 'pin': booked_data['pin'],
                 'date': booked_data['date'],
                  'text_msg':text_msg,
                  'btn':btn
             }
         flash(msg,'success')
      #or
      #return redirect(url_for('schedule_test',**request_data))
      return render_template('schedule_test.html',**request_data)
   return render_template('schedule_test.html')




if __name__ == "__main__":
   app.secret_key = '12345jojsrojoh9211'
   app.run(debug=True)