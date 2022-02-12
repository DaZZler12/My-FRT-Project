<div id="top"></div>



<!-- PROJECT SHIELDS -->
<!-- [![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url] -->
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- Requirements for FRT submission -->
<h1>
 Some Important Links:-
 <ol>
 <li><a href="https://mycovid19selfchecker.azurewebsites.net/" target="_blank">My Project URL</a></li>
  <li>Project Demo Videos :- i. <a href="https://drive.google.com/file/d/1dtUsfguaD5Z9dQg9tVTxr6f8vV_RmEbY/view?usp=sharing" target="_blank">Video-1 </a> ii. <a href="https://drive.google.com/file/d/1L5qkumMOv6EIQjezlBc8CwaDMthQtM8T/view?usp=sharing" target="_blank">Video-2 </a></li>
  <li>Azure Services Used:-
   <ul><li><a href="https://github.com/DaZZler12/My-FRT-Project/tree/master" target="_blank">Azure App Services Coding Implementation</a>, <a href="https://github.com/DaZZler12/My-FRT-Project/actions/runs/1817825408">Deployment</a>, <a href="https://mycovid19selfchecker.azurewebsites.net/" target="_blank">Running Website</a><br><br>
   <img src="https://github.com/DaZZler12/My-FRT-Project/blob/main/images/appservice.jpg"></li></ul><br>
    
   <ul><li><a href="https://github.com/DaZZler12/covid19-info-frt/tree/main/Website">Azure Static Web App Coding Implementation</a>, <a href="https://github.com/DaZZler12/covid19-info-frt/runs/5125079443?check_suite_focus=true" target="_blank">Deployment</a>, <a href="https://red-beach-0fec6a200.1.azurestaticapps.net/" target="_blank">Running Website</a><br><br><img src="https://github.com/DaZZler12/My-FRT-Project/blob/main/images/staticwebapp.jpg"></li></ul><br>
   
   <ul><li><a href="https://github.com/DaZZler12/My-FRT-Project/tree/Functions/HttpTrigger%20Function" target="_blank">Azure HttpTrigger Function Coding Implementation</a><br><br><img src="https://github.com/DaZZler12/My-FRT-Project/blob/main/images/httptrigger.jpg"></li></ul><br>
   
   <ul><li><a href="https://github.com/DaZZler12/My-FRT-Project/tree/TimerFunction/TimerTrigger" target="_blank">Azure TimerTrigger Function Coding Implementation</a><br><br><img src="https://github.com/DaZZler12/My-FRT-Project/blob/main/images/timmer.jpg"></li></ul><br>
   
   <ul><li><a>Azure Table Storage</a><br><br><img src="https://github.com/DaZZler12/My-FRT-Project/blob/main/images/table.jpg"></li></ul>
  </li>
  
   <ul><li><a>Azure SaaS Service</a><br><br><img src="https://github.com/DaZZler12/My-FRT-Project/blob/main/images/sendgrid.jpg"></li></ul>
  </li>
 </ol>
<h1>
 <h2>
  Unfortunately, My Azure for students' credit expired, thus the storage account is not accessible as well as the associated HttpTrigger and TimerTrigger Functions are out of service! Sorry for the inconvenience!<br><br>
  
- ![subscription](https://github.com/DaZZler12/My-FRT-Project/blob/main/images/imgend.jpg?raw=true)
 </h2>
 
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://mycovid19selfchecker.azurewebsites.net/" target="_blank">
    <img src="https://github.com/DaZZler12/My-FRT-Project/blob/main/images/icon2.png" alt="Logo" width="100" height="90">
  </a>

<h2 align="center">Covid19 Self-Checker</h2>

  <p align="center">
    <br />
    <a href="https://github.com/DaZZler12/My-FRT-Project/tree/master"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://mycovid19selfchecker.azurewebsites.net">View Demo</a>
    ·
     <a href="https://github.com/DaZZler12/covid19-info-frt">NewsLetter Repo</a>
    .
    <a href="https://github.com/DaZZler12/My-FRT-Project/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#My-WebApp">My-WebApp</a></li>
    <li><a href="#AboutUs">AboutUs</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Covid19 Self-Checker](https://github.com/DaZZler12/My-FRT-Project/blob/main/images/product.jpg)](https://mycovid19selfchecker.azurewebsites.net)

<h3>A Quick Overview-</h3>
<h5><b>In this project, I attempted to build a web application that capable of recognizing whether a person is Covid19 positive or negative to a reasonable degree by taking some basic symptoms as input. I've set the boundary value to 50%, which means that if the predicted probability value is greater than or equal to 0.5, the system will classify that person as Covid19 positive, and the user will be redirected from the home page to the result display page, where he or she will be instructed to book a slot for the Covid19 test (for confirmation) by entering the necessary information.<br /><br />
This system will be able to show its potential in the undermentioned scenario:-
<br /><br />1. When a big number of people seek to schedule a slot for a Covid19 test, this system will do a primary classification to prevent a mass gathering at the Covid19 centers.
<br /><br />2. A user can also subscribe to the newsletter using their email address, and the subscribed user will receive daily Covid19 updates at a specific time.</h5>
  
<h3>How the entire system is working ?</h3>
  <h4>The technology used -</h4>
<h5>1.	For making Prediction, I had created a model using simple Logistic regression, as it’s clear from the data set  (sample2.csv) we have 5 independent variables – [runnyNose, fever, sorethroat, diffBreath, headache], and one dependent variable categorical variable i.e corona_result.  Thus by using those independent variables the best possible and simple way to perform a categorical classification is to perform a Logistic Regression. One can test the result in the web app also.
For input = [1,0,1,1,1] ==> output = 64% and the system will classify the case as covid +ve.
<br /><br />
2.	I created a storage account in the Azure platform to store the subscribed user mail id. When a user clicks the subscribe button, the related HTTP-TRIGGER function will be responsible for pushing the mail id to the table, however when a user clicks the unsubscribe button, then that particular id will simply be popped out. (*)
 <br />
  
  <br />
3.	To send regular mail to all subscribed users, I created a TIMER-TRIGGER function that is linked to the Twilio SendGrid API. To create and access this SendGrid API, one must first create a SaaS subscription through the Azure Portal, from which one will receive a URL to redirect to the SendGrid portal. Now, the Timer Trigger function will take all of the email addresses stored in the table and, using the SendGrid API, send emails to all of the subscribers at a predetermined time. (*)
 <br /><br />
  4.	Lastly, to host the web application, I have used Azure App Service and to host the NewsLetter website I have used the Azure Static web App.<br /><br />
  </h5>
  
# (*)(Unfortunately, My Azure for students' credit expired, thus the storage account is not accessible as well as the associated HttpTrigger and TimerTrigger Functions are out of service! Sorry for the inconvenience!) 

  
- ![subscription](https://github.com/DaZZler12/My-FRT-Project/blob/main/images/imgend.jpg?raw=true)
  
  
  # Flowchart for the prediction system
  
  ![flow1](https://github.com/DaZZler12/My-FRT-Project/blob/main/images/flow1.jpg?raw=true)
  
  # Flowchart of the NewsLetter System
  
  ![flow2](https://github.com/DaZZler12/My-FRT-Project/blob/main/images/flow2.jpg?raw=true)
  
  
  
<p align="right">(<a href="#top">Move Up!</a>)</p>



### Built With

* [Microsoft Azure](https://portal.azure.com/?websitesextension_ext=asd.featurePath%3Danalysis%2FLinuxAppDown#home)
* [React.js](https://reactjs.org/)
* [SendGrid](https://landing.sendinblue.com/en/sendgrid?utm_source=adwords&utm_medium=cpc&utm_content=Competitors&utm_extension=&utm_term=%2Bsendgrid&utm_matchtype=b&utm_campaign=902129196&utm_network=g&km_adid=516527901107&km_adposition=&km_device=c&utm_adgroupid=41695235981&gclid=CjwKCAiA6Y2QBhAtEiwAGHybPbQP2OlrLdbEUlOvwqTBfaK7DL7uO_7FbMqQiW5EQ3WUqjTF2KT5TRoCYTQQAvD_BwE)
* [flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
* [JavaScript](https://www.javascript.com/)
* [SweetAlert](https://sweetalert.js.org/guides/)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [scikit-learn](https://scikit-learn.org/stable/)

<p align="right">(<a href="#top">Move Up!</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Do the following needful in order to setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

1. Install Python and the below mentioned packeges
   ```sh
   flask, sendgrid, scikit-learn, azure.functions, azure.cosmosdb.table.tableservice, json, datetime, logging, requests
   ```

2. Clone the repo
   ```sh
   git clone https://github.com/DaZZler12/My-FRT-Project/tree/master.git
   ```
3. Create a newsletter like website which will be a static website take ref from (https://github.com/DaZZler12/covid19-info-frt)
   ```sh
   https://red-beach-0fec6a200.1.azurestaticapps.net/
   ```
4. Create a flask application take ref from (https://github.com/DaZZler12/My-FRT-Project/tree/master)
   ```sh
   https://mycovid19selfchecker.azurewebsites.net/
   ```
5. Create a stourage account in azure platform with fileds
   ```sh
   emailid | partitionkey = 1
   ```
6. Create a HttpTrigger Function take ref from (https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=csharp)
   ```sh
   https://github.com/DaZZler12/My-FRT-Project/tree/Functions/HttpTrigger%20Function
   ```
7. Create a TimerTrigger Function take ref from (https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?tabs=csharp)
   ```sh
   https://github.com/DaZZler12/My-FRT-Project/tree/TimerFunction/TimerTrigger
   ```
 8. Create a web app and host your flask application, go thorugh the below documation by Microsoft Learning to host your web app
   ```sh
  https://docs.microsoft.com/en-us/learn/modules/host-a-web-app-with-azure-app-service/
   ```
 9. Create a static web app to host your newsletter website
   ```sh
  https://docs.microsoft.com/en-us/learn/paths/azure-static-web-apps/
   ```
  
  
<p align="right">(<a href="#top">Move Up!</a>)</p>



<!-- My-WebApp -->
## My-WebApp
  
  ![subscription](https://github.com/DaZZler12/My-FRT-Project/blob/main/images/show.jpg?raw=true)
  ![subscription](https://github.com/DaZZler12/My-FRT-Project/blob/main/images/pic2.jpg?raw=true)
  ![subscription](https://github.com/DaZZler12/My-FRT-Project/blob/main/images/pic3.jpg?raw=true)
  ![subscription](https://github.com/DaZZler12/My-FRT-Project/blob/main/images/pic4.jpg?raw=true)
  ![subscription](https://github.com/DaZZler12/My-FRT-Project/blob/main/images/pic5.jpg?raw=true)
  ![subscription](https://github.com/DaZZler12/My-FRT-Project/blob/main/images/pic6.jpg?raw=true)


_To know more about Azure, please refer to the [Documentation](https://docs.microsoft.com/en-us/learn/paths/az-900-describe-cloud-concepts/)_

<p align="right">(<a href="#top">Move Up!</a>)</p>



<!-- AboutUs -->
## [AboutUs](https://mycovid19selfchecker.azurewebsites.net/about)

See the [open issues](https://github.com/DaZZler12/My-FRT-Project/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">Move Up!</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star!✨✨ Thanks again! 🙂🙂🙂

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">Move Up!</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See [MIT License](LICENSE) for more information.

<p align="right">(<a href="#top">Move Up!</a>)</p>



<!-- CONTACT -->
## Contact

Abhirup Bhattacharya - [@_A_bhirup](https://twitter.com/_A_bhirup)
  
Important Project Link: 
  1. [Flask Complete Web Application](https://github.com/DaZZler12/My-FRT-Project/tree/master)
  2. [HttpTrigger Function](https://github.com/DaZZler12/My-FRT-Project/tree/Functions/HttpTrigger%20Function)
  3. [TimerTrigger Function](https://github.com/DaZZler12/My-FRT-Project/tree/TimerFunction/TimerTrigger)
  4. [Covid19 NewsLetter Static Website](https://github.com/DaZZler12/covid19-info-frt)

<p align="right">(<a href="#top">Move Up!</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Future Plans](https://mycovid19selfchecker.azurewebsites.net/about#portfolio)
* [About](https://mycovid19selfchecker.azurewebsites.net/about#values)

<p align="right">(<a href="#top">Move Up!</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/DaZZler12/My-FRT-Project/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/DaZZler12/My-FRT-Project/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/DaZZler12/My-FRT-Project/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/DaZZler12/My-FRT-Project/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/abhirup-bhattacharya-72973a199
[product-screenshot]: images/screenshot.png
