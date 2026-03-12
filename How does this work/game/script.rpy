'''
Name: A (number1bidoof on github & itch.io)
Description:
As a second semester senior, you already know the routine: go to class, try to stay awake in calc & making games in programming classes.
However, one day you look around outside, and instead of seeing the lush forest of piedmont, you see the busy streets of NYC.
You try to survive 7 days in a completely new environment of Bronx Sci, totally NOT WECIB, navigating surviving a completely new life in a new city on your own.
Notice: No generative AI was used in the process of making this game, all images are either made by me, or backgrounds provided by Noraneko Games & Spiral Atlas on itch.io.
Bronx Sci is a real high school in NYC, but no one character is a real life person expect for people I got explict permission to use as a character in the WECIB portion.
'''
init:
    # backgrounds
    image bg room = Image("images/backgrounds/single bedroom.jpg")
    image bg bathroom = Image("images/backgrounds/bathroom.jpg")
    image bg subwayMorning1 = Image("images/backgrounds/c3_light.jpg")
    image bg subwayMorning2 = Image("images/backgrounds/c5_light.jpg")
    image bg subwayMorning3 = Image("images/backgrounds/window_light.jpg")
    image bg subwayNight1 = Image("images/backgrounds/c3.jpg")
    image bg subwayNight2 = Image("images/backgrounds/c5.jpg")
    image bg subwayNight3 = Image("images/backgrounds/window.jpg")
    image bg kitchen = Image("images/backgrounds/kitchen.jpg")
    image bg diningRoom = Image("images/backgrounds/dining_kitchen.jpg")
    image bg entrance = Image("images/backgrounds/entrance.jpg")
    image bg schoolCafeteria = Image("images/backgrounds/Cafeteria_Day.png")
    image bg schoolClassroom = Image("images/backgrounds/Classroom_Day.png")
    image bg lounge = Image("images/backgrounds/lounge.jpg")
    image bg lab = Image("images/backgrounds/chem_lab.jpeg")
    image bg downtownFront = Image("images/backgrounds/front.jpg")
    image bg downtownAlleyWay = Image("images/backgrounds/alley.jpg")
    image bg downtownPark = Image("images/backgrounds/park.jpg")
    image bg subwayStation = Image("images/background/subwayStation.jpg")
    image bg bodega = Image("images/backgrounds/bodega.jpg")
    image bg smallPark = Image("images/backgrounds/smallpark.jpg")
    image bg downtownStreet = Image("images/background/street.jpg")

    # characters TBD
    define e = Character("Example")
    define mc = Character("[player_name]", color = "#3BB3EF")
    define mrMcCuen = Character("Mr.McCuen")
    define mom = Character("Mom", "#")

label start: # character creation sequence
    $ player_name = renpy.input("What is your name?","", allow = None)
    $ player_name = player_name.strip()
    $ player_major = "placeholder"

    menu:
        "What is your program area (This will matter later)"
        "Computer Programming":
            $ player_major = "Computer Programming"
        "Cyber Security":
            $ player_major = "Cyber"
        "Biotechnology":
            $ player_major = "Biotech"

    scene bg room with pixellate
    "You start out any regular day at high school, waking up, brushing your teeth, backing your backpack & driving to school."
    "As a second semester senior, the senioritis is seriously kicking in."
    "For some its been kicking in since September."
    "Everyone and their mom seems to be extremely tired and sick of school, including yourself. Struggling to stay awake during lectures, assignments and exams"
    "Some may think its the best time of their lives, free from academic stress & taking extra time to hang out with friends & using all of the senior privileges"
    "Others are just waiting until the May 21st, at around ~4:30 PM, being handed their diploma saying \"I have successfully completed 4 whole years of high school\""
    "But for most seniors, it\'s a mixture of both, waiting around, but also trying to make the most out of the time we have left"



    return
label wclass_chem:
    scene bg lab


label wclass_programming:
label wclass_calc:

