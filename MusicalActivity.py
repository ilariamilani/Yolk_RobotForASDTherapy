from AudioActivity import AudioActivity
import time
import os
import random
from subprocess import run
from audioplayer import PlayAudio


#print(os.path.abspath(__file__))
#print(os.path.dirname(os.path.abspath(__file__)))
#os.chdir(os.path.dirname(os.path.abspath(__file__)))  # change working directory

audio_list = ["sounds/Evviva.wav", "sounds/wow.wav", "sounds/SuonaConMe.wav", "sounds/CheBravo.wav"]

#da mettere in funtions_main
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
        elif (Nsong == 7):
            PlayAudio().play("sounds/Sad_R2D2.wav")
        elif (Nsong == 8):
            # pick a random choice from a list of strings.
            audio = random.choice(audio_list)
            PlayAudio().play(audio)
    if (level == 1):
        if (Nsong == 0):
            PlayAudio().play("sounds/AttentiallaMusica1.wav")
        elif (Nsong == 1):
            PlayAudio().play("sounds/dindondan.wav")
        elif (Nsong == 2):
            PlayAudio().play("sounds/dindondan.wav")
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
            PlayAudio().play("sounds/TwinkleTwinkleLittleStar.wav")
        elif (Nsong == 2):
            PlayAudio().play("sounds/TwinkleTwinkleLittleStar.wav")
        elif (Nsong == 3):
            PlayAudio().play("sounds/queen.wav")
        elif (Nsong == 4):
            PlayAudio().play("sounds/queen.wav")
        elif (Nsong == 5):
            PlayAudio().play("sounds/BrillaBrillaStellina.wav")
        elif (Nsong == 6):
            PlayAudio().play("sounds/BrillaBrillaStellina.wav")
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
            PlayAudio().play("sounds/fraMartino.wav")
        elif (Nsong == 4):
            PlayAudio().play("sounds/SuonaLeCampane.wav")
        elif (Nsong == 5):
            PlayAudio().play("sounds/vecchiaFattoria1.wav")
        elif (Nsong == 6):
            PlayAudio().play("sounds/vecchiaFattoria2.wav")
        elif (Nsong == 7):
            PlayAudio().play("sounds/founding.wav")
            #PlayAudio().play("sounds/TartarugaSprint.waw")
    #elif (level == 4):




#da mettere in main program:

#defines
NSongsinLevel = 7 # number of songs in a level
MA_interactionLevel = 0 #contains the audios for interaction in MA

if __name__ == '__main__':

    reproduce_song(MA_interactionLevel, 8) # random!
    Nid = 0
    answerTime = 8.0
    TIME_OUT_song = 12.0  # maximum time given to reproduce a song
    ActivityLevel = 1
    identification_time = 0
    while ActivityLevel < 4:
        song = 0
        reproduce_song(ActivityLevel, song) #Attenti alla musica!
        NSongIdentified = 0
        if ActivityLevel == 1:
            answerTime -= 3.0
            TIME_OUT_song -= 3.0
        else:
            answerTime = 9.0
            TIME_OUT_song = 12.0
        while song < NSongsinLevel:
            song += 1
            if song == NSongsinLevel:
                print("end of level")
                break
            if (((song % 2) != 0) and (song != NSongsinLevel)): #every time a new song is played (odd number)(every song is reproduced twice)
                reproduce_song(MA_interactionLevel, 0) #suona con me!
            #if song == 2:
            reproduce_song(MA_interactionLevel, 5)  # ora tocca a me!
            reproduce_song(ActivityLevel, song)
            #if song == 1:
            reproduce_song(MA_interactionLevel, 4) #tocca a te!

            # BEAT RECOGNITION
            activity = AudioActivity()
            activity.start(id=Nid)
            print("id=")
            print(Nid)
            if (song % 2) != 0:  # every time a new song is played (odd number)(every song is reproduced twice)
                Nid += 1
            while ((activity.elapsed_time < answerTime or activity.silence < 15) and activity.elapsed_time < TIME_OUT_song): #wait in case the child is still playing (making noises)
                time.sleep(1.0)
                if activity.sequence_identified > 0:
                    print("Bravoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
                    NSongIdentified += 1
                    time.sleep(1.5)
                    identification_time = time.perf_counter()
                    break
            if activity.sequence_identified > 0:
                while activity.silence < 15 and (identification_time + 1.5 > activity.elapsed_time):  #wait in case the child is still playing
                    continue
            activity.stop()
            if ( ((song % 2) == 0) and (NSongIdentified > 0)): #at least 1 song over 2 has been correctly reproduced
                reproduce_song(MA_interactionLevel, 2) #wow evviva!
            if (activity.sequence_identified == 0) and (activity.other_activity > 20 or activity.Nbeat < 3):
                print("the child is not performing the activity")
                reproduce_song(MA_interactionLevel, 7)  # sad :(
            print(".")
            print("next song in the same level")
            print(".")
            activity.sequence_identified = 0
        # LEVEL CONCLUDED: checking for results. if 50% of the activity is correct: next level. else: repeat the level
        if (song == NSongsinLevel): #end of the level
            if NSongIdentified >= ((NSongsinLevel - 1) // 2): #50% correct
                print(".")
                print("yeeeeeeeeeeeeeyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy ready fot the next level")
                print(".")
                reproduce_song(MA_interactionLevel, 1)  # wow, bravo! reproduced when the level has been passed
                reproduce_song(MA_interactionLevel, 6)  # canta con me!
                reproduce_song(ActivityLevel, song) # long song
                ActivityLevel += 1
            else:
                print(".")
                print("well well riproviamooo")
                print(".")
                reproduce_song(MA_interactionLevel, 3)  # riproviamo
                # if the child was not able to pass to the next level, the same will be reproposed
                Nid -= ((NSongsinLevel - 1) // 2)


##aggiungi anche luci e movimenti alle espressioni
