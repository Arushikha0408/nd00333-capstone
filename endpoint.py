import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://ee83b334-0b8c-458e-b3fe-a9ba02913292.southcentralus.azurecontainer.io/score'

# Two sets of data to score, so we get two results back

data = {"data":
        [
          {
            "age": 62,
            "anaemia": 0,
            "creatinine_phosphokinase": 231,
            "diabetes": 0,
            "ejection_fraction": 25,
            "high_blood_pressure": 1,
            "platelets": 253000,
            "serum_creatinine": 0.9,
            "serum_sodium": 140,
            "sex": 1,
            "smoking": 1,
            "time": "10"
          },
          {
            "age": 45,
            "anaemia": 1,
            "creatinine_phosphokinase": 981,
            "diabetes": 0,
            "ejection_fraction": 30,
            "high_blood_pressure": 0,
            "platelets":  136000,
            "serum_creatinine": 1.1,
            "serum_sodium": 137,
            "sex": 1,
            "smoking": 0,
            "time": "11"
          },
      ]
    }
 
 
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
