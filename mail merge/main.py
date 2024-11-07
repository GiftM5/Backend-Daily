#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


   

def opening_names():
    real_names = []
    with open("./Input/Names/inivited_names.txt","r") as file:
        names = file.readlines()
        for line in names:
            name = line.strip()
            real_names.append(name)
        
        return real_names
   

def opening_letter():
    with open("./Input/letters/starting_letter.docx","r")as f:
        letter = f.readlines()
        
        return letter
    

def sending_letter():
    names = opening_names()
    letter = opening_letter()
    constructed_letter = "".join(letter)
    
    for name in names:
        email = constructed_letter.replace("[name]",name)
        print("="*30)
        print(email)
    print("="*30)
sending_letter()  
 
