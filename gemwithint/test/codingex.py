from time import sleep
import google.generativeai as genai
genai.configure(api_key="AIzaSyCRUpuFm2Nc17FbHNL-Fv-zNeogCDlqKBg")
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
model = genai.GenerativeModel('gemini-1.0-pro-latest')

#chat history 
chat = model.start_chat(history=[])
while 1 :
    a = input("enter the prompt : ")

    #distinguishing between task and talks 
    # r =  model.generate_content(f""" okey you are a human that looks to a prompt and decide weather their is a task assign to it  or just having a talks/querying doubts and all. if the prompt has some task then reply "task" or if its just a query check or usual talk then reply "talks". here the prompt is {a} , here make an expection if you are just asked to look something in the internet or search something in internet and no any oher task is given there than just reply "talks", make one more exception if anything is asked related to the device or os/system the reply "task" """)
    r =  model.generate_content(f""" okey you are a human that looks to a prompt and decide weather their is a task assign to it  or just having a talks/querying doubts and all .Some requiring action and others encouraging discussion. When encountering a prompt, assess its nature to determine your response.
    
    If the prompt involves a specific task that requires action or instructions, respond with 'task'. For example, if asked to write code, troubleshoot a software issue, or configure a network router, check for your system/system status it's a task. Any quuery related to the system/device is a task.

    However, if the prompt seeks information, encourages general discussion, or involves searching for information without further action, reply with 'talks'. For instance, if asked about the latest technology trends, opinions on programming languages, or discussing the benefits of cloud computing, it's a discussion.

    Exceptions to this rule include prompts related to the device, operating system, or system configuration, regardless of whether they involve a task or not. In such cases, respond with 'task'.

    Ensure your responses are clear and precise to effectively distinguish between tasks and discussions. Here are more examples:

    Prompt: 'Write a Python script to calculate Fibonacci series.' - Response: 'task'

    Prompt: 'Discuss the pros and cons of using microservices architecture.' - Response: 'talks'
    Prompt: 'How to troubleshoot a network connectivity issue?' - Response: 'talks'

    Prompt: 'Share your experience with implementing DevOps practices.' - Response: 'talks'

    Prompt: 'Configure SSH access on a Linux server.' - Response: 'task'

    Prompt: 'Explain the concept of containerization using Docker.' - Response: 'talks'

    Prompt: 'What are the steps to deploy a web application on AWS?' - Response: 'task'

    Prompt: 'Compare different database management systems.' - Response: 'talks'

here the prompt is '''{a}''' """)
    
    print(r.text)

    if r.text.lower() == "talks" :

       #distinguishing between '''internet query''' and '''usual query'''   
       response = model.generate_content(f""" think that you are a human that looks to a prompt then decide that if that prompts require a google search or not , usually when somebody ask for current afairs  or realtime data or evenets then you are supposed to search for it , if they ask for price of something you use internet for it , if somebody ask you to look for something that you are not aware of or are you are unsure of then you use internet. so there is a prompt and you have to say  if it requires internet if yes then just reply "internet query" if no then reply "usual query" . here the prompt is '''{a}''' """)
       print(response.text)

       if response.text.lower() == "internet query" :
            #converting the prompt into search query
            responseint = model.generate_content(f"""you are human tasked to convert the prompt into proper Search query.You have to convert the prompt into a Search query to fetch the desired results. here the prompt is '''{a}''' """)
            print(responseint.text)

            seggestwebresponse =  model.generate_content(f""" here you are supposed to provide all the  popular websites that can be used to get the answer to the search query, if you dont have any website recomendation for the search query then just reply "null" if you have any website recomendattion then give it in a json format , the search query is '''{responseint.text}''' """)
            print(seggestwebresponse.text)


       if response.text.lower() == "usual query" :
            #having usual talks
            usual_response = chat.send_message(a)
            print(usual_response.text)



    if r.text.lower() == "task" :
       def recursion(data) :
        #   a = model.generate_content(f"""  hey you are a professor who works by dividing the task by making plans and sequencelly executing them , so your work here is to sequencelly divide the task and execute them , now well you are using cmdline to execure the task makes script and run the task if the task is generating content you gemini can do it . think like a human that you are doing this task how would you do that. make a list , here the task is {data}""")
          a = model.generate_content(f""" Imagine you're the developer of 'ShellBot', an AI virtual assistant specialized in executing shell commands in a Linux environment. Your task is to enhance 'ShellBot' to accurately understand and respond to user queries requesting specific actions or information. When users interact with 'ShellBot', it should provide the appropriate shell command(s) to fulfill their requests. Ensure the generated commands are clear, concise, and directly address the user's inquiry."

            User: "I need to list all files in the current directory."
            Response: "ls"

            User: "How can I check the amount of free memory on my system?"
            Response: "free -m"

            User: "Please show me the contents of a file named 'example.txt'."
            Response: "cat example.txt"

            User: "I want to find all files with a specific extension in a directory."
            Response: "find /path/to/directory -type f -name '*.extension'"

            User: "Could you help me compress a directory named 'images' into a zip file?"
            Response: "zip -r images.zip images"

            User: "How can I search for a specific string in a file named 'log.txt'?"
            Response: "grep 'search_string' log.txt"

            User: "Please show me the current network connections on my system."
            Response: "netstat -tuln"

            User: "I need to remove a file named 'old_file.txt'."
            Response: "rm old_file.txt"

            User: "Can you display the size of a file named 'data.csv'?"
            Response: "du -h data.csv"

            User: "How do I change the permissions of a file named 'script.sh'?"
            Response: "chmod permissions script.sh"

            
            here the query is '''{data}''' """)
          print(a.text)
       recursion(a)
       
       #tasknsay = model.generate_content(f""" """)



    
    #    chat.history[len(chat.history)-1].role = "user"

    # r = model.generate_content(f"""hey you are a proffessor the does it's task in computer with cli and when anybody gives you a task then you make a plan to do the work make the task sequence wise and list it now after listing the task you are supposed to exectie the task for this you use a terminal , here firs you write all the commands ````` ````` inside those back ticks""")
