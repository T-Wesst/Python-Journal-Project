# import requests module to make http requests to url
import requests
# initialize global variables
httpGET = 0
httpPOST = 0
httpFail = 0
logFile = "output.log"
isDone = False
baseURL = "https://jsonplaceholder.typicode.com"
# function to append data to file
def appendToFile(fname, contents):
  with open(fname, 'a') as file:
    file.write(f"{contents}\n")
# function to GET data from url with resource type
def get(url, resource):
  getByID = input("get by id? y/n ").upper()
  # if user does not want to get a resource by its ID use base url otherwise append id to url
  if getByID != "Y":
    res = requests.get(url)
  else:
    id = input("enter an id: ")
    res = requests.get(url+f"/{id}")
  data = res.text
  status = res.status_code
  # construct and return logged message
  message = f"HTTP {action} {resource}: {status} | Output: {data}"
  return message
# function to POST data to url with resource type
def post(url, newResource):
  # post new resource to url
  res = requests.post(url, data=newResource)
  data = res.text
  status = res.status_code
  # construct and return logged message
  message = f"HTTP {action} {resource}: {status} | Output: {data}"
  return message
# function to create and return new user from users input
def newUser():
  return {
    "name": input("enter name: "),
    "username": input("enter username: ")
  }
# function to create and return new comment from users input
def newComment():
  return {
    "name": input("enter title of comment: "),
    "body": input("enter body of comment: ")
  }
# function to create and return a new post from users input
def newPost():
  return {
    "title": input("enter title for post: "),
    "body": input("enter body for post: "),
  }
# while the user is not done making HTTP requests
while not isDone:
  # ask user what HTTP method to do
  action = input("please enter an http method: ").upper()
  # if user inputs exit terminate the loop and log total requests to file
  if action == "EXIT":
    isDone = True
    appendToFile(logFile, f"Requests: GET {httpGET} | POST {httpPOST} | FAILED {httpFail}")
  else:
    # ask user what type of resource will they GET or POST (users, comments, posts)
    resource = input("Please enter an resource type: ").lower()
    url = f"{baseURL}/{resource}"
    # in the case action matches GET | POST | default (doesn't match a case)
    match action:
        # case user action equals GET
        case "GET":
          # call get function to url with users inputted resource type
          output = get(url, resource)
          # write output from GET request to file
          appendToFile(logFile, output)
          # increment GET request counter by 1
          httpGET += 1
        # case user action equals POST
        case "POST":
          # in the case where resource matches users | comments | posts | default (doesn't match a case)
          match resource:
            case "users":
              # call post function to url and create a user using the newUser function
              output = post(url, newUser())
              # write output from POST request to file
              appendToFile(logFile, output)
              # increment POST request counter by 1
              httpPOST += 1
            case "comments":
              # call post function to url and create a comment using the newComment function
              output = post(url, newComment())
              # write output from POST request to file
              appendToFile(logFile, output)
              # increment POST request counter by 1
              httpPOST += 1
            case "posts":
              # call post function to url and create a post using the newPost function
              output = post(url, newPost())
              # write output from POST request to file
              appendToFile(logFile, output)
              # increment POST request counter by 1
              httpPOST += 1
            case _:
              # when the user inputs an invalid resource type increment failed http requests by 1
              httpFail+=1                
        case _:
          # when user inputs an invalid http method notify user of error and retry
            print("Please enter an http method: GET | POST | Patch | PUT | DELETE")