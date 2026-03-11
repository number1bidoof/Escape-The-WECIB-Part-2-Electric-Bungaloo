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

    define e = Character("Example")

label start: # starting sequence, or day 0 starting at WECIB

    scene bg subwayMorning1 with fade

    show eileen happy

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"


    return
