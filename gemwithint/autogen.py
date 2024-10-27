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
    #response = model.generate_content(f""" okey you are an ai assistant that helps me to automate my system i.e. linux here  , what are the steps that should be taken to complete the task that is asked in the prompt , where the pronpt is ''' {a}''' """)
    # response = model.generate_content(f"""okey you are an ai assistant that helps me to automate my system i.e. linux . 
    #                                 here you need to tell me how many task are there and what are the task that are asked in the prompt ,
    #                                 all the task should go sequence by sequence and you have to specify the actual given task in 1 line for each task. 
    #                                 also take in consideration that if their is any conjuction for ex 'and' their is possibility of having more than one task .
    #                                 where the prompt is '''{a}''' ,

    #                                     the example for your response is like this :
    #                                     human : can you write an essay on mohamad ali and save it to the file
    #                                     ai : tasks
    #                                     1 : write or get an essay on mohamad ali  
    #                                     2 : save the essay to a file

    #                                     example 2
    #                                     human : can you write a basic python program in vscode
    #                                     ai : tasks
    #                                     1 : open vs code
    #                                     2 : writing a basic python program in vscode

    #                                 """)
    response = model.generate_content(f"what are the things that are asked in the prompt list all the task in sequence but specify the actual detail given in the task not an example , here the prompt is {a} ")

    print(response.text)
    k =  input(" should this append it ?")
    if k == 'y' :
         with open('data.txt' ,'a') as f :
                  f.write(f"{a} \n")
                  f.write(f"{response.text}\n")
                  f.write("\n-------------------------")