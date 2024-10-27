from time import sleep
import google.generativeai as genai
genai.configure(api_key="AIzaSyCRUpuFm2Nc17FbHNL-Fv-zNeogCDlqKBg")
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
model = genai.GenerativeModel('gemini-pro')

#chat history 
chat = model.start_chat(history=[])
while 1 :
    a = input("enter the prompt : ")

    #distinguishing between task and talks 
    r =  model.generate_content(f""" okey you are a human that looks to a prompt and decide weather their is a task assign to it  or just having a talks/querying doubts and all. if the prompt has some task then reply "task" or if its just a query check or usual talk then reply "talks". here the prompt is {a} , here make an expection if you are just asked to look something in the internet or search something in internet and no any oher task is given there than just reply "talks" """)
    
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
       
       #tasknsay = model.generate_content(f""" """)
       
       pass




    
    #    chat.history[len(chat.history)-1].role = "user"

    # r = model.generate_content(f"""hey you are a proffessor the does it's task in computer with cli and when anybody gives you a task then you make a plan to do the work make the task sequence wise and list it now after listing the task you are supposed to exectie the task for this you use a terminal , here firs you write all the commands ````` ````` inside those back ticks""")
