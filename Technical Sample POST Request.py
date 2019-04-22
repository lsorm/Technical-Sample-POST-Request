import requests
import json

test_url = "https://lyft-interview-test.herokuapp.com/test"

string_to_cut = "iamyourlyftdriver"

result = ""

for i in range(2, len(string_to_cut), 3) :
    result += string_to_cut[i];

datas = {"string_to_cut": string_to_cut, "return_string": result}

r = requests.post(test_url, json = datas)
