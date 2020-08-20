from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

engine=pp.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot=ChatBot("MyBot")

convo=[
    'Hi',
    'Hi',
    'Hello',
    'hi there',
    'What is your name',
    'my name is Mr Bot, I am created by Varun',
    'I am doing great these days',
    'thankyou',
    'In which city do you live',
    'I live in Mangalore',
    'In which language do you speak ?',
    'I speak in tulu',
    'Bye',
    'Bye Bye'

]

trainer=ListTrainer(bot)
trainer.train(convo)
#answer=bot.get_response("what is your name")
#print(answer)
"""print("Talk to Bot:")
while True:
    query=input()
    if query=='exit':
        break
    answer=bot.get_response(query)
    print("Bot:",answer)"""
main =Tk()
main.geometry("500x650")
main.title("My chat bot")

img=PhotoImage(file="bot.png")
photoL=Label(main,image=img)
photoL.pack(pady=5)

def takeQuerry():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("Your bot is listening try to speak: ")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print("Not Recognized")





def ask_from_bot():
    query=textF.get()
    ans_from_bot=bot.get_response(query)
    msgs.insert(END,"you:"+query)
    msgs.insert(END,"Bot:"+str(ans_from_bot))
    speak(ans_from_bot)
    textF.delete(0,END)
    msgs.yview(END)
frame=Frame(main)
scroll=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20,yscrollcommand=scroll.set)
scroll.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
msgs.pack(side=RIGHT,)
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(main,text="Ask from Bot",font=("Verdana",20),command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>',enter_function)
if __name__ == '__main__':
    def repeatL():
        while True:
            takeQuerry()


    t=threading.Thread(target=repeatL)
    t.start()
    main.mainloop()