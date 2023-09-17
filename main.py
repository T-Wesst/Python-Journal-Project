import requests

def appendToFile(fname, contents):
  with open(fname, 'a') as file:
    file.write(f"{contents}\n")

def get(url, resource):
  getByID = input("get by id? y/n ").upper()
  if getByID != "Y":
    res = requests.get(url)
  else:
    id = input("enter an id: ")
    res = requests.get(url+f"/{id}")
  data = res.text
  status = res.status_code
  message = f"HTTP {action} {resource}: {status} | Output: {data}"
  return message
def post(url, newResource):
  res = requests.post(url, data=newResource)
  data = res.text
  status = res.status_code
  message = f"HTTP {action} {resource}: {status} | Output: {data}"
  return message
  
def newUser():
  return {
    "name": input("enter name: "),
    "username": input("enter username: ")
  }
def newComment():
  return {
    "name": input("enter title of comment: "),
    "body": input("enter body of comment: ")
  }
def newPost():
  return {
    "title": input("enter title for post: "),
    "body": input("enter body for post: "),
  }

httpGET = 0
httpPOST = 0
httpFail = 0
logFile = "output.log"
isDone = False
baseURL = "https://jsonplaceholder.typicode.com"

while not isDone:
  action = input("please enter an http method: ").upper()
  if action == "EXIT":
    isDone = True
  else:
    resource = input("Please enter an resource type: ").lower()
    url = f"{baseURL}/{resource}"
    match action:
        case "GET":
          httpGET += 1
          output = get(url, resource)
          appendToFile(logFile, output)
        case "POST":
          httpPOST += 1
          match resource:
            case "users":
              output = post(url, newUser())
              appendToFile(logFile, output)
            case "comments":
              output = post(url, newComment())
              appendToFile(logFile, output)
            case "posts":
              output = post(url, newPost())
              appendToFile(logFile, output)
            case _:
              httpPOST-=1
              httpFail+=1                
        case _:
            httpFail+=1
            print("Please enter an http method: GET | POST | Patch | PUT | DELETE")
appendToFile(logFile, f"Requests: GET {httpGET} | POST {httpPOST} | FAILED {httpFail}")