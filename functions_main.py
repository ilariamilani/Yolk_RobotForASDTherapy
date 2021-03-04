import serial
from subprocess import run
from audioplayer import PlayAudio

previous_action = "none"
next_action = "none"
state_user = ""
current_action = "none"


def human_verification(angle_mean, user, count): #return if the object detected by sonar is a human
    #print("angle: " + str(angle_mean)+", User:" + user)
    if (( user== "front") and ((angle_mean >= 155 ) and (angle_mean <= 205)) and (count >= 2)): # 180+-45
        print("Human front")
        tracking_a_user = True
    elif (( user== "right") and (angle_mean <= 205) and (angle_mean >= 315)  and (count >= 2)): # 90+-45
        print("human right")
        tracking_a_user = True
    elif ((user == "left") and (angle_mean >= 45) and (angle_mean <= 155) and (count >= 2)): # 270+-45
        print("Human left")
        tracking_a_user = True
    else:
        tracking_a_user = False
        print("Arduino: object, not human")
    return tracking_a_user

def send_action_arduino(actual_action, reply, ser, tracking_a_user):
    if((actual_action != reply) and (tracking_a_user == True)):
        actual_action = reply
        # then that a new action want to be applied.
        # If there is a user being tracked, send the message tu the arduino to perform the correspondent action
        ser.write(bytes((actual_action+'\n'), encoding='utf-8'))
        line = ser.readline().decode('utf-8').rstrip()
        #reproduce_action_sound(actual_action)
        #print(line)
    elif(tracking_a_user == True):
        # it means that it is the same message as before, then, no new action will be sent
        actual_action = reply
    else:
        actual_action = " "
          
    return actual_action

def send_uno_lights(ser1,action):
        # actions sent to the Arduino for the initial interaction
        ser1.write(bytes((action+'\n'), encoding='utf-8'))
        # The system will not continue until the movement has been performed
        #reproduce_action_sound(action)
        line1 = ser1.readline().decode('utf-8').rstrip()
        
def send_initial_action_arduino(action, ser, sound):
        # actions sent to the Arduino for the initial interaction
        ser.write(bytes((action+'\n'), encoding='utf-8'))
        reproduce_action_sound(sound)

def reproduce_action_sound(action):
    if(action!="none" and action!="move_find"):
        if(action == "excited"):
            PlayAudio().play("sounds/Giochiamo.wav")
            PlayAudio().play("sounds/Excited_R2D2.wav")
        elif(action == "sad"):
            PlayAudio().play("sounds/Sad_R2D2.wav")
        elif(action == "out"):
            PlayAudio().play("sounds/Playful_R2D2.wav")
        elif(action == "found"):
            PlayAudio().play("sounds/founding.wav")
        elif(action == "move"):
            PlayAudio().play("sounds/fordward.wav")
        elif(action == "excited_attract"): #robot identifies the user in front of it, ready to interact
            PlayAudio().play("sounds/Excited_R2D2.wav")
        elif(action == "interested_excited"):
            PlayAudio().play("sounds/Giochiamo.wav")
        elif(action == "happy"): #after receiving a hug
            PlayAudio().play("sounds/wow.wav")
            PlayAudio().play("sounds/cheBello.wav")
        elif(action == "very_scared"):
            PlayAudio().play("sounds/AhiaBasta.wav")
            #also the scream??
        elif(action == "scared"):
            PlayAudio().play("sounds/ahiaCheMale.wav")
        elif(action == "angry"):
            PlayAudio().play("sounds/No.wav")
            PlayAudio().play("sounds/Snappy_R2D2.wav")
            
def decide_action(action):
    global previous_action
    global current_action
    global state_user
    state = state_user
    obtain_user_state(action)
    if(((state =="interested_scared" )and(previous_action == "interested_excited")) or ((state =="interested_scared" )and(previous_action == "happy")) or ((state =="interested_scared" )and(previous_action == "scared")) or ((state =="interested_scared" )and(previous_action == "very_scared")) or ((state =="interested_scared" )and(previous_action == "sad")) or ((state =="scared" )and(previous_action == "interested_excited")) or ((state =="scared" )and(previous_action == "happy")) or ((state =="scared" )and(previous_action == "angry")) or ((state =="scared" )and(previous_action == "sad")) or ((state =="scared" )and(previous_action == "none"))):
        current_action = "excited_attract"
    elif(((state =="interested_scared" )and(previous_action == "excited_attract")) or ((state =="interested_scared" )and(previous_action == "angry")) or ((state =="interested_scared" )and(previous_action == "none")) or ((state =="scared" )and(previous_action == "excited_attract")) or ((state =="scared" )and(previous_action == "scared")) or ((state =="scared" )and(previous_action == "very_scared"))):
        current_action = "interested_excited"
    elif(state == "interested_interacting"):
        current_action = "happy"
    elif(((state =="scared_aggressive" )and(previous_action == "interested_excited")) or ((state =="scared_aggressive" )and(previous_action == "excited_attract")) or ((state =="scared_aggressive" )and(previous_action == "happy")) or ((state =="scared_aggressive" )and(previous_action == "none")) or ((state =="gaming_aggressive" )and(previous_action == "interested_excited")) or ((state =="gaming_aggressive" )and(previous_action == "excited_attract")) or ((state =="gaming_aggressive" )and(previous_action == "happy")) or ((state =="gaming_aggressive" )and(previous_action == "none"))):
        current_action = "scared"
    elif(((state =="scared_aggressive" )and(previous_action == "scared")) or ((state =="gaming_aggressive" )and(previous_action == "scared")) or ((state =="gaming_aggressive" )and(previous_action == "very_scared")) or ((state =="gaming_aggressive" )and(previous_action == "angry"))):
        current_action = "very_scared"
    elif(((state =="scared_aggressive" )and(previous_action == "angry")) or ((state =="scared_aggressive" )and(previous_action == "sad")) or ((state =="gaming_aggressive" )and(previous_action == "sad"))):
        current_action = "sad"
    elif(((state =="scared_aggressive" )and(previous_action == "very_scared"))):
        current_action = "angry"    
    previous_action = current_action
    
def obtain_user_state(action):
    global state_user
    if action == "touch": state_user = "interested_scared"
    elif action == "push": state_user = "scared"
    elif action == "hit": state_user = "scared_aggressive"
    elif action == "hug": state_user = "interested_interacting"
    elif action == "strongHug": state_user = "gaming_aggressive"
    else: state_user = state_user        
        
def reproduce_song(level, Nsong):
    if (level == 0): #interaction with the user
        if (Nsong == 0):
            PlayAudio().play("sounds/SuonaConMe.wav")
        elif (Nsong == 1):
            PlayAudio().play("sounds/wow.wav")
            PlayAudio().play("sounds/CheBravo.wav")
        elif (Nsong == 2):
            PlayAudio().play("sounds/wow.wav")
            PlayAudio().play("sounds/Evviva.wav")
        elif (Nsong == 3):
            PlayAudio().play("sounds/Riproviamo.wav")
        elif (Nsong == 4):
            PlayAudio().play("sounds/ToccaATe.wav")
        elif (Nsong == 5):
            PlayAudio().play("sounds/OraToccaAMe.wav")
        elif (Nsong == 6):
            PlayAudio().play("sounds/CantaConMe.wav")
    if (level == 1):
        if (Nsong == 0):
            PlayAudio().play("sounds/AttentiallaMusica1.wav")
        elif (Nsong == 1):
            PlayAudio().play("sounds/tatittitata.wav")
        elif (Nsong == 2):
            PlayAudio().play("sounds/tatittitata.wav")
        elif (Nsong == 3):
            PlayAudio().play("sounds/tichetà.wav")
        elif (Nsong == 4):
            PlayAudio().play("sounds/tichetà.wav")
        elif (Nsong == 5):
            PlayAudio().play("sounds/opopop.wav")
        elif (Nsong == 6):
            PlayAudio().play("sounds/opopop.wav")
        elif (Nsong == 7):
            PlayAudio().play("sounds/founding.wav")
            #PlayAudio().play("sounds/44Gatti.wav.waw")
    elif (level == 2):
        if (Nsong == 0):
            PlayAudio().play("sounds/AttentiallaMusica2.wav")
        elif (Nsong == 1):
            PlayAudio().play("sounds/Snappy_R2D2.wav")
        elif (Nsong == 2):
            PlayAudio().play("sounds/Snappy_R2D2.wav")
        elif (Nsong == 3):
            PlayAudio().play("sounds/queen.wav")
        elif (Nsong == 4):
            PlayAudio().play("sounds/queen.wav")
        elif (Nsong == 5):
            PlayAudio().play("sounds/queen.wav")
        elif (Nsong == 6):
            PlayAudio().play("sounds/queen.wav")
        elif(Nsong == 7):
            PlayAudio().play("sounds/founding.wav")
            #PlayAudio().play("sounds/PulcinoBallerino.waw")
    elif (level == 3):
        if (Nsong == 0):
            PlayAudio().play("sounds/AttentiallaMusica3.wav")
        elif (Nsong == 1):
            PlayAudio().play("sounds/GiroGiroTondo1.wav")
        elif (Nsong == 2):
            PlayAudio().play("sounds/GiroGiroTondo2.wav")
        elif (Nsong == 3):
            PlayAudio().play("sounds/Snappy_R2D2.wav")
        elif (Nsong == 4):
            PlayAudio().play("sounds/Snappy_R2D2.wav")
        elif (Nsong == 5):
            PlayAudio().play("sounds/Snappy_R2D2.wav")
        elif (Nsong == 6):
            PlayAudio().play("sounds/Snappy_R2D2.wav")
        elif (Nsong == 7):
            PlayAudio().play("sounds/founding.wav")
            #PlayAudio().play("sounds/TartarugaSprint.waw")
    
        
    
    
