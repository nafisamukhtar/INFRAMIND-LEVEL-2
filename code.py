from tkinter import *
import os
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()

#shopping list 
import tkinter
from tkinter import *
from tkinter import messagebox 
l=[] 
c=1
def entryError() : 
   
  if insertField.get() == "" : 
    
    
    messagebox.showerror("Error in input. Please input again") 
    
    return 0
  
  return 1
def insertTask(): 
  global c 
  
  value = entryError() 
  if (value == 0): 
    return
  var=insertField.get()+"\n"
  l.append(var) 
  TextArea.insert('end -1 chars', str(c) + " :" + var) 
  c=c+1
  del_tf()
  file = open(var, "w")
  file.write(var + "\n")
  file.close()
def del_nf() : 
  
  nf.delete(0.0, END) 
def del_tf() : 
  insertField.delete(0, END) 
  
def delete() : 
  
  global c 
  
  if (len(l)==0): 
    messagebox.showerror("There are no items") 
    return
  number = nf.get(1.0, END) 
  if (number=="\n"): 
    messagebox.showerror("input error") 
    return
  else : 
    task_no = int(number) 
  del_nf() 
  
  l.pop(task_no - 1) 
  c=c-1
  
  TextArea.delete(1.0, END) 
  for i in range(len(l)): 
    TextArea.insert('end -1 chars',str(i + 1) + ":" + l[i]) 
  
if (__name__ == "__main__"): 
  window = Tk() 
  window.configure(background = "grey") 
  window.title("Shopping List") 
  window.geometry("450x300") 
  enterTask = Label(window, text = "Please enter your item", bg = "lightblue")
  insertField = Entry(window)
  
  Submit = Button(window, text = "Submit", fg = "Black", bg = "lightblue", command = insertTask) 
  TextArea = Text(window, height = 4, width = 35, font = "arial 13")
  
  taskNumber = Label(window, text = "Specify the item number that you want to remove, below", bg = "lightblue")
            
  nf = Text(window, height = 1, width = 2, font = "arial 13")
  
  delete = Button(window, text = "Delete", fg = "Black", bg = "lightblue", command = delete) 
  
  Exit = Button(window, text = "Do you want to close?", fg = "Black", bg = "lightblue", command = exit) 
  enterTask.grid(row = 0, column = 2) 
  insertField.grid(row = 1, column = 2, ipadx = 50) 
  Submit.grid(row = 2, column = 2) 
  TextArea.grid(row = 3, column = 2, padx = 10, sticky = W) 
  taskNumber.grid(row = 4, column = 2, pady = 5) 
  nf.grid(row = 5, column = 2) 
  delete.grid(row = 6, column = 2, pady = 5) 
  Exit.grid(row = 7, column = 2) 
  
  window.mainloop() 

#query handler
import tkinter
from tkinter import *
from tkinter import messagebox 
l=[] 
c=1
def entryError() : 
   
  if insertField.get() == "" : 
    
    
    messagebox.showerror("Error in input. Please input again") 
    
    return 0
  
  return 1
def insertTask(): 
  global c 
  
  value = entryError() 
  if (value == 0): 
    return
  var=insertField.get()+"\n"
  l.append(var) 
  TextArea.insert('end -1 chars', str(c) + "---> " + var) 
  c=c+1
  del_tf()
  file = open(var, "w")
  file.write(var + "\n")
  file.close()
def del_nf() : 
  
  nf.delete(0.0, END) 
def del_tf() : 
  insertField.delete(0, END) 
  
def delete() : 
  
  global c 
  
  if (len(l)==0): 
    messagebox.showerror("There are no queries") 
    return
  number = nf.get(1.0, END) 
  if (number=="\n"): 
    messagebox.showerror("input error") 
    return
  else : 
    task_no = int(number) 
  del_nf() 
  
  l.pop(task_no - 1) 
  c=c-1
  
  TextArea.delete(1.0, END) 
  for i in range(len(l)): 
    TextArea.insert('end -1 chars',str(i + 1) + "---> " + l[i]) 
  
if (__name__ == "__main__"): 
  window = Tk() 
  window.configure(background = "light green") 
  window.title("WE ARE HEAR TO ANSWER") 
  window.geometry("500x300") 
  enterTask = Label(window, text = "Please enter your query in the format (query-username)", bg = "grey")
  insertField = Entry(window)
  
  Submit = Button(window, text = "Submit", fg = "Black", bg = "grey", command = insertTask) 
  TextArea = Text(window, height = 4, width =40, font = "arial 13")
  Exit = Button(window, text = "Click here to close", fg = "Black", bg = "grey", command = exit) 
  enterTask.grid(row = 0, column = 2) 
  insertField.grid(row = 1, column = 2, ipadx = 50) 
  Submit.grid(row = 2, column = 2) 
  TextArea.grid(row = 3, column = 2, padx = 10, sticky = W) 
  Exit.grid(row = 7, column = 2) 
  
  window.mainloop() 

#sentiment analyser
  
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tkinter import *
 
# Function for clearing the   
# contents of all entry boxes
# And text area.
def clearAll() : 
   
    # deleting the content from the entry box 
    negativeField.delete(0, END) 
    neutralField.delete(0, END) 
    positiveField.delete(0, END) 
    overallField.delete(0, END) 
 
    # whole content of text area  is deleted 
    textArea.delete(1.0, END)
     
# function to print sentiments 
# of the sentence. 
def detect_sentiment():
 
    # get a whole input content from text box
    sentence = textArea.get("0.5", "end")
 
    # Create a SentimentIntensityAnalyzer object. 
    sid_obj = SentimentIntensityAnalyzer() 
 
    # polarity_scores method of SentimentIntensityAnalyzer 
    # oject gives a sentiment dictionary. 
    # which contains pos, neg, neu, and compound scores. 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
 
    string = str(sentiment_dict['neg']*100) + "% Negative"
    negativeField.insert(10, string)
     
 
    string = str(sentiment_dict['neu']*100) + "% Neutral"
    neutralField.insert(10, string)
 
    string = str(sentiment_dict['pos']*100) +"% Positive"
    positiveField.insert(10, string)

    
     
    # decide sentiment as positive, negative and neutral 
    if sentiment_dict['compound'] >= 0.05 :
        string = "Positive"
 
    elif sentiment_dict['compound'] <= - 0.05 :
        string = "Negative"
      
 
    else :
        string = "Neutral"
 
    overallField.insert(10, string)

    file = open(string, "w")
    file.write(string + "\n")
    file.close()
         
 
 
# Driver Code 
if __name__ == "__main__" :
     
 
    # Create a GUI window 
    gui = Tk() 
     
    # Set the background colour of GUI window 
    gui.config(background =  "light green") 
 
    # set the name of tkinter GUI window 
    gui.title("Sentiment Detector") 
 
    # Set the configuration of GUI window 
    gui.geometry("200x400") 
 
    # create a label : Enter Your Task 
    enterText = Label(gui, text = "Enter Your Review",
                                     bg = "light green")
 
    # create a text area for the root 
    # with lunida 13 font 
    # text area is for writing the content 
    textArea = Text(gui, height =5, width =15, font = "lucida 13")
   
 
    # create a Submit Button and place into the root window 
    # when user press the button, the command or  
    # function affiliated to that button is executed  
    check = Button(gui, text = "Check Review", fg = "Black", 
                         bg = "blue", command = detect_sentiment)
 
    # Create a negative : label 
    negative = Label(gui, text = "Review Rated As: ",
                                        bg = "light green") 
   
    # Create a neutral : label 
    neutral = Label(gui, text = "Review Rated As: ", 
                                       bg = "light green") 
   
    # Create a positive : label 
    positive = Label(gui, text = "Review Rated as: ",
                                        bg = "light green")
 
    # Create a overall : label 
    overall = Label(gui, text = "Review Overall Rated As: ",
                                           bg = "light green")
    
 
    # create a text entry box  
    negativeField = Entry(gui)
 
    # create a text entry box  
    neutralField = Entry(gui)
 
    # create a text entry box  
    positiveField = Entry(gui)
 
    # create a text entry box  
    overallField = Entry(gui) 
 
    # create a Clear Button and place into the root window 
    # when user press the button, the command or  
    # function affiliated to that button is executed . 
    clear = Button(gui, text = "Clear", fg = "Black", 
                      bg = "blue", command = clearAll)
     
    # create a Exit Button and place into the root window 
    # when user press the button, the command or  
    # function affiliated to that button is executed . 
    Exit = Button(gui, text = "Exit", fg = "Black", 
                        bg = "blue", command = exit)
 
    # grid method is used for placing  
    # the widgets at respective positions  
    # in table like structure. 
    enterText.grid(row = 0, column = 2)
     
    textArea.grid(row = 1, column = 2, padx = 10, sticky = W)
     
    check.grid(row = 2, column = 2)
     
    negative.grid(row = 3, column = 2)
     
    neutral.grid(row = 5, column = 2)
     
    positive.grid(row = 7, column = 2)
     
    overall.grid(row = 9, column = 2)
     
    negativeField.grid(row = 4, column = 2)
 
    neutralField.grid(row = 6, column = 2)
                       
    positiveField.grid(row = 8, column = 2)
     
    overallField.grid(row = 10, column = 2)
     
    clear.grid(row = 11, column = 2)
     
    Exit.grid(row = 12, column = 2)
 
    # start the GUI 
    gui.mainloop() 
    