import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json

import sys


#data =  {
#
#        "Inputs": {
#
#                "input1":
#                {
#                    "ColumnNames": ["symbol", "date_ex", "open_p", "high_p", "low_p", "close_p", "volume", "adj_close_p", "future_price"],
#                    "Values": [ [ "GOOG", "","536.35","537.20","532.52","533.33","1390000", "0", "0" ] ]
#                },        },
#            "GlobalParameters": {
#}
#    }
data =  {
    
    "Inputs": {
        
        "input1":
            {
                "ColumnNames": ["symbol", "date_ex", "open_p", "high_p", "low_p", "close_p", "volume", "adj_close_p", "future_price"],
                    "Values": [ [ "FB", "","81.87","82.46","81.51","82.14","16140000", "0", "0" ], [ "value", "", "0", "0", "0", "0", "0", "0", "0" ], ]
                },        },
            "GlobalParameters": {
}
}

#print 'Argument List:', str(sys.argv[5])



body = str.encode(json.dumps(data))

resDic = json.loads(body)
resDic["Inputs"]["input1"]["Values"][0][0] =sys.argv[1]
resDic["Inputs"]["input1"]["Values"][0][2] =sys.argv[2]
resDic["Inputs"]["input1"]["Values"][0][3] =sys.argv[3]
resDic["Inputs"]["input1"]["Values"][0][4] =sys.argv[4]
resDic["Inputs"]["input1"]["Values"][0][5] =sys.argv[5]
resDic["Inputs"]["input1"]["Values"][0][6] =sys.argv[6]


body = str.encode(json.dumps(resDic))

#print'Body:', body


url = 'https://ussouthcentral.services.azureml.net/workspaces/0329a393be4c47328a97aa0dd0429581/services/a276ea8e1dab4304a1f75508811e2b85/execute?api-version=2.0&details=true'
api_key = 'DsZj/Vq6FbRPdhw6+J/94o2CVfBbdkv5W8UHrHRFM5OwFfMgurzkPXVccZSxKyRHujnCIK0Peda7YUiwGnad2w==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers) 

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    #print(result)
    resDic = json.loads(result)
    high_p = resDic["Results"]["output1"]["value"]["Values"][0][7]
    print("Expected High Value in 3 Months : " + high_p)
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))
