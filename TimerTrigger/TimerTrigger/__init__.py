import datetime
import logging
import json
import azure.functions as func
from azure.cosmosdb.table.tableservice import TableService
import requests

def main(mytimer: func.TimerRequest, sendGridMessage: func.Out[str]) -> None:
    

     #if mytimer.past_due:
        logging.info('The timer is past due!')
        
        table_service = TableService(account_name='put table name', account_key='put storage account key')

        rows = table_service.query_entities("mailinglist","PartitionKey eq '1'")
        maillist = []

        

        x = requests.get('https://api.covid19india.org/data.json')
        x = x.json()
        recent = x["cases_time_series"][-1]
        recentdate = recent["date"]
        dailyconfirmed = recent["dailyconfirmed"]
        dailydeceased = recent["dailydeceased"]
        dailyrecovered = recent["dailyrecovered"]
        totalconfirmed = recent["totalconfirmed"]
        totaldeceased = recent["totaldeceased"]
        totalrecovered = recent["totalrecovered"]
        subjectline = "COVID19 cases update - "+recentdate
        emailcontent = "Today's ("+recentdate+") COVID-19 cases in India\n\n Confirmed : " + dailyconfirmed + "\n Recovered: "+dailyrecovered+"\n Deaths: "+dailydeceased+"\n\n Overall Cases in India\n\n Total Confirmed : " + totalconfirmed + "\n Total Recovered: "+totalrecovered+"\n Total Deaths: "+totaldeceased+"\n\n\n Stay Safe. Maintain Social Distancing. Follow Healthcare guidelines. Wear mask. Sanitize your hands regularly\n\n"

        for row in rows:
            temp = {}
            temp["email"] = row['email']
            maillist.append(temp)
           
        message = {
                 "personalizations": [
    {
      "to": [
        {
          "email": "abhirupbhattacharya8@gmail.com"
        }
      ],
      
      "bcc": maillist
    }
  ],
                "subject": subjectline,
                "content": [{
                    "type": "text/plain",
                    "value": emailcontent }]
        }
                
        sendGridMessage.set(json.dumps(message))
