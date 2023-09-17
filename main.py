import requests

def appendToFile(fname, contents):
  with open(fname, 'a') as file:
    file.write(f"{contents}\n")

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
            getByID = input("Get resource by id? y/n ").upper()
            httpGET += 1
            if getByID != 'Y':
              response = requests.get(url)
            else:
              id = input("Please enter a id: ")
              response = requests.get(url+f"/{id}")
            data = response.text
            status = response.status_code
            output = f"HTTP {action} {resource}: {status} | Output: {data}"
            appendToFile(logFile, output)
        case "POST":
            httpPOST += 1
            match resource:
              case "users":
                newUser = {
                  "name": input("enter name: "),
                  "username": input("enter username: ")
                }
                response = requests.post(url, data=newUser)
                data = response.text
                status = response.status_code
                output = f"HTTP {action} {resource}: {status} | Output: {data}"
                appendToFile(logFile, output)
              case "comments":
                newComment = {
                  "name": input("enter title of comment: "),
                  "body": input("enter body of comment: ")
                }
                response = requests.post(url, data=newComment)
                data = response.text
                status = response.status_code
                output = f"HTTP {action} {resource}: {status} | Output: {data}"
                appendToFile(logFile, output)
              case "posts":
                newPost = {
                  "title": input("enter title for post: "),
                  "body": input("enter body for post: "),
                }
                response = requests.post(url, data=newPost)
                data = response.text
                status = response.status_code
                output = f"HTTP {action} {resource}: {status} | Output: {data}"
                appendToFile(logFile, output)
              case _:
                httpPOST-=1
                httpFail+=1                
        case _:
            httpFail+=1
            print("Please enter an http method: GET | POST | Patch | PUT | DELETE")
appendToFile(logFile, f"Requests: GET {httpGET} | POST {httpPOST} | FAILED {httpFail}")