# importing the requests library
import requests
# defining the api-endpoint
API_ENDPOINT = "http://16c7-115-119-250-30.ngrok.io/train"
# data to be sent to api
data = {
	"url": "https://github.com/MJ410/mlops-classify_test",
	"branch_name": "main",
	"algo_type": "Regression"
}
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)
# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)