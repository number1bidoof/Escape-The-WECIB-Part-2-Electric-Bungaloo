## NYC School Day Simulator — 3 Day Arc
## Bronx Science High School

init:
    # ---------- BACKGROUNDS ----------
    image bg room           = Image("images/backgrounds/single bedroom.jpg")
    image bg bathroom       = Image("images/backgrounds/bathroom.jpg")
    image bg subwayMorning1 = Image("images/backgrounds/c3_light.jpg")
    image bg subwayMorning2 = Image("images/backgrounds/c5_light.jpg")
    image bg subwayMorning3 = Image("images/backgrounds/window_light.jpg")
    image bg subwayNight1   = Image("images/backgrounds/c3.jpg")
    image bg subwayNight2   = Image("images/backgrounds/c5.jpg")
    image bg subwayNight3   = Image("images/backgrounds/window.jpg")
    image bg kitchen        = Image("images/backgrounds/kitchen.jpg")
    image bg diningRoom     = Image("images/backgrounds/dining_kitchen.jpg")
    image bg entrance1       = Image("images/backgrounds/entrance1.jpg")
    image bg entrance2       = Image("images/backgrounds/entrance2.jpeg")
    image bg schoolCafeteria = Image("images/backgrounds/Cafeteria_Day.png")
    image bg schoolClassroom = Image("images/backgrounds/Classroom_Day.png")
    image bg lounge         = Image("images/backgrounds/lounge.jpg")
    image bg lab            = Image("images/backgrounds/chem_lab.jpg")
    image bg downtownFront  = Image("images/backgrounds/front.jpg")
    image bg downtownAlleyWay = Image("images/backgrounds/alley.jpg")
    image bg downtownPark   = Image("images/backgrounds/park.jpg")
    image bg subwayStation  = Image("images/backgrounds/subwayStation.jpg")
    image bg bodega         = Image("images/backgrounds/bodega.jpg")
    image bg smallPark      = Image("images/backgrounds/smallpark.jpg")
    image bg downtownStreet = Image("images/backgrounds/street.jpg")

    # ---------- CHARACTER SPRITES ----------
    # One sprite per character. Place PNGs in images/characters/.
    # Naming convention: charactername.png

    image mom         = Image("images/characters/mom.jpg")
    image ock         = Image("images/characters/ock.jpeg")
    image guard       = Image("images/characters/guard.png")
    image grace       = Image("images/characters/grace.jpeg")
    image jose        = Image("images/characters/jose.png")
    image leah        = Image("images/characters/leah.jpg")
    image jacky       = Image("images/characters/jacky.png")
    image xavier      = Image("images/characters/xavier.jpeg")
    image micheal     = Image("images/characters/micheal.jpeg")
    image sham        = Image("images/characters/sham.JPG")
    image whittington = Image("images/characters/whittington.JPG")
    image li          = Image("images/characters/li.png")
    image mcCuen      = Image("images/characters/mccuen.png")
    image reyes       = Image("images/characters/reyes.JPG")
    image davis       = Image("images/characters/davis.png")

    # ---------- CHARACTER DEFINITIONS ----------
    define mc          = Character("[player_name]")
    define mom         = Character("Mom")
    define whittington = Character("Ms. Whittington")   # Chemistry
    define li          = Character("Ms. Li")            # Calculus
    define mcCuen      = Character("Mr. McCuen")        # Computer Science
    define reyes       = Character("Ms. Reyes")         # English
    define davis       = Character("Mr. Davis")         # Physics
    define ock         = Character("The Ock")
    define MTAPolice   = Character("MTA Officer")
    define grace       = Character("Grace")
    define jacky       = Character("Jacky")
    define leah        = Character("Leah")
    define jose        = Character("Jose")
    define micheal     = Character("Michael")
    define xavier      = Character("Xavier")
    define sham        = Character("Sham")
    define olivia      = Character("Olivia")
    define karim       = Character("Karim")
    define nayan       = Character("Nayan")
    define metroCard   = Character("MetroCard Machine")
    define narator     = Character("narrator")


## ============================================================
##  START — CHARACTER CREATION
## ============================================================

label start:

    $ player_name = renpy.input("What is your name?", "", allow=None)
    $ player_name = player_name.strip()
    $ player_major  = "placeholder"
    $ knows_train   = False
    $ met_grace     = False
    $ met_jose      = False
    $ homework_done = False

    menu:
        "What is your program area? (This will matter later)"
        "Computer Programming":
            $ player_major = "Computer Programming"
        "Cyber Security":
            $ player_major = "Cyber Security"
        "Biotechnology":
            $ player_major = "Biotechnology"

    scene bg room with fade

    "Waking up from sleeping the night earlier, you begin reflecting on the current state of your life as a senior, almost done with your second semester."
    "As a second semester senior, the senioritis is seriously kicking in."
    "For some it's been kicking in since September."
    "Everyone and their mom seems to be extremely tired and sick of school, including yourself. Struggling to stay awake during lectures, assignments and exams."
    "Some may think it's the best time of their lives, free from academic stress, taking extra time to hang out with friends and using all of the senior privileges."
    "Others are just waiting until May 21st, at around 4:30 PM, being handed their diploma saying 'I have successfully completed 4 whole years of high school.'"
    "But for most seniors, it's a mixture of both — waiting around, but also trying to make the most out of the time left."
    "You were one of those people. Past tense."

    "Because this morning, something is different."
    "You sit up in bed. The light coming through the window is wrong — too bright, too grey, too loud."

    "You pull back the curtain."
    "Instead of the lush treeline of the Piedmont, you see a six-story apartment building, a corner store with a hand-painted sign, and a guy selling something out of a shopping cart."
    "You are not home."

    show mom at right with dissolve
    mom "Wake up [player_name], you're going to be late for school!"
    "[player_name]: ...where am I?"
    mom "The Bronx, baby. Bronx Science. Go wash your face, I made eggs."
    hide mom with dissolve

    "You stare at the ceiling for a moment. Bronx Science. That's a magnet school. That's one of the best high schools in New York City."
    "You don't remember applying."

    jump nycday1


## ============================================================
##  DAY 1
## ============================================================

label nycday1:

    scene bg kitchen with fade

    "The kitchen smells like eggs and sofrito. A MetroCard sits on the counter next to a folded sticky note."
    "The note reads: 'B/D from 205th. Get off at Fordham Rd. Walk 3 blocks east. Good luck. — Mom'"
    "Under it, in different handwriting: 'Don't take the 4 by mistake. — Love, a stranger'"
    "You eat fast. The eggs are good. The city outside the window is already in full motion."

    scene bg entrance1 with dissolve

    "You step outside. The air hits you — exhaust, a pretzel cart, someone's music from an open window three floors up."
    "This is real. You're doing this."

    jump day1_bodega

## ---- DAY 1: BODEGA ----

label day1_bodega:

    scene bg bodega with dissolve

    "On the corner there's a bodega. The light inside is warm and yellow against the grey morning."
    "A hand-painted sign: EGG & CHEESE $3.50 — COFFEE $1.75 — ARIZONA $1.00"
    "You already ate but you could use something for the walk."

    menu:
        "Do you stop?"
        "Go in.":
            jump bodega_day1_inside
        "Keep walking. You're already cutting it close.":
            "You walk past. The smell of bacon follows you half a block."
            jump day1_subway

label bodega_day1_inside:

    show ock at right with dissolve
    "The bell above the door rings. A man behind the counter — older, Yankees cap, reading glasses — glances up."
    ock "Whassup."
    "He goes back to whatever's on his phone. A cat on a stack of paper towels watches you from across the store."

    menu:
        "What do you get?"

        "Arizona iced tea. $1.00.":
            "[player_name]: One Arizona please."
            ock "They in the back."
            hide ock with dissolve
            "You grab a green tea from the cooler. Cold. Perfect."
            jump day1_subway

        "Ask what's good.":
            "[player_name]: Uh — what do you recommend?"
            ock "The sandwich."
            "[player_name]: I'll take the sandwich."
            ock "Salt pepper ketchup?"
            menu:
                "Salt pepper ketchup.":
                    "He nods. You made the right call."
                    hide ock with dissolve
                    "He wraps it and slides it across without looking up again."
                    jump day1_subway
                "Just ketchup.":
                    ock "Aight."
                    hide ock with dissolve
                    jump day1_subway

        "Try to pet the cat.":
            "You reach toward the cat. It stares at your hand. It does not move. It does not blink."
            "You stop. You take your hand back."
            ock "She don't like that."
            "[player_name]: Yeah I got that."
            ock "Name's Duchess."
            hide ock with dissolve
            "He goes back to his phone. You buy an Arizona and leave."
            jump day1_subway

        "Just leave.":
            hide ock with dissolve
            "You look around for thirty seconds and walk back out."
            jump day1_subway

## ---- DAY 1: SUBWAY ----

label day1_subway:

    scene bg subwayStation with dissolve

    "205th Street station. You head downstairs."
    "The platform is already packed. Everyone is locked into their phones or staring at the tracks."
    "The sign above reads: B · D"
    "The note said B or D. That's easy. Except a 4 train is also pulling in on the express track and it looks faster."

    menu:
        "Which train do you take?"

        "The B train.":
            $ knows_train = True
            "You let the 4 pass. The B rolls in two minutes later."
            "You squeeze into a car that smells like coffee and someone's breakfast sandwich."
            "Fordham Road. You follow the crowd up the stairs."
            jump day1_arrive_school

        "The D train.":
            $ knows_train = True
            "The D goes express. Fordham Road in twelve minutes. That works."
            jump day1_arrive_school

        "The 4 train — it looks faster.":
            $ knows_train = False
            "You swipe through and board the 4. It does not go to Fordham Road."
            "You end up at 161st Street — Yankee Stadium."
            "The stadium is enormous and completely silent in the morning grey."
            narator "You are at Yankee Stadium. School started seven minutes ago."
            "You backtrack on the D. By the time you reach Fordham Road you're twenty-two minutes late."
            jump day1_arrive_late

        "Ask someone on the platform.":
            $ knows_train = True
            $ met_grace = True
            show grace at left with dissolve
            "You tap a woman on the shoulder. She pulls one earbud out."
            grace "B or D. Don't take the 4."
            "[player_name]: Thank you."
            hide grace with dissolve
            "She puts the earbud back. You take the D. It's right."
            "Her name is Grace. You don't know that yet."
            jump day1_arrive_school

## ---- DAY 1: ARRIVAL ----

label day1_arrive_late:

    scene bg entrance2 with dissolve

    show guard at right with dissolve
    "Bronx Science. Security waves you through the metal detector."
    "Guard: 'ID.'"
    "You don't have one yet. You explain you're new."
    "He calls someone from the main office. You wait four minutes in the lobby."
    hide guard with dissolve
    "Someone walks you to homeroom. Every head turns when you walk in."

    menu:
        "What do you say?"
        "'Sorry. I'm new — I took the wrong train.'":
            "A few kids nod. One mouths 'same.'"
            jump day1_homeroom
        "Nothing. Just find a seat.":
            "The teacher looks at you. You sit. She marks the book."
            jump day1_homeroom
        "'The MTA is an absolute disaster —'":
            "The teacher raises one hand. You stop. You sit. Three kids laugh."
            jump day1_homeroom

label day1_arrive_school:

    scene bg entrance2 with dissolve

    "Bronx Science. You make it through security with two minutes to spare."
    "You find your homeroom and slide into a seat near the middle."

    show jose at right with dissolve
    jose "You new?"
    "[player_name]: Yeah."
    jose "Cool. I'm Jose."
    $ met_jose = True
    "[player_name]: [player_name]."
    "He nods and goes back to his notebook."
    hide jose with dissolve

    jump day1_homeroom

label day1_homeroom:

    scene bg schoolClassroom with dissolve

    "Homeroom. Announcements over the intercom — most of which you don't understand yet."
    "Someone mentions a chemistry quiz. Someone else mentions the CS final project deadline."
    "You write nothing down because you have no notebook yet."
    "The bell rings."
    jump day1_chemistry

## ---- DAY 1: CHEMISTRY — MS. WHITTINGTON ----

label day1_chemistry:

    scene bg lab with dissolve

    show whittington at right with dissolve
    whittington "Settle down. We're continuing Unit 8 — electrochemistry. Can anyone tell me the difference between a galvanic and an electrolytic cell?"
    "The room is quiet."
    whittington "Someone new today. [player_name], is it? Let's hear it."

    menu:
        "Do you answer?"

        "Galvanic produces electricity. Electrolytic uses it.":
            "[player_name]: A galvanic cell generates electrical energy from a spontaneous reaction. An electrolytic cell drives a non-spontaneous reaction using electricity."
            whittington "Correct. Sit down — you're ahead of half this class."
            hide whittington with dissolve
            "A kid at the next bench raises an eyebrow."
            jump day1_chem_lab

        "Say you haven't covered this yet.":
            "[player_name]: We hadn't gotten to electrochemistry yet back home."
            whittington "That's alright. Pay close attention today."
            hide whittington with dissolve
            jump day1_chem_lab

        "Stay quiet.":
            "She waits three seconds. Then picks someone else."
            hide whittington with dissolve
            "You write 'electrochemistry' at the top of a blank page and underline it twice."
            jump day1_chem_lab

label day1_chem_lab:

    scene bg lab with dissolve

    show leah at left with dissolve
    "You get paired with a girl named Leah who moves around the bench like she's done this a hundred times."
    leah "You transferred?"
    "[player_name]: Yeah. First day."
    leah "You know how to use a multimeter?"

    menu:
        "Yes.":
            "[player_name]: Yeah, we did circuit labs last semester."
            leah "Good. You do the readings, I'll set up the cell."
            hide leah with dissolve
            "You work together in a comfortable silence. The cell works on the first try."
            show whittington at right with dissolve
            whittington "Good result, you two."
            hide whittington with dissolve
            jump day1_physics

        "Not really.":
            "[player_name]: Not exactly."
            leah "Okay. Watch first, then I'll show you."
            hide leah with dissolve
            "She's patient about it. You take notes."
            jump day1_physics

        "Ask what a multimeter is.":
            "Leah stares at you for just a moment."
            leah "It measures voltage. Here."
            hide leah with dissolve
            "She hands it to you and shows you where to clip the leads."
            "You don't ask any more questions after that."
            jump day1_physics

## ---- DAY 1: PHYSICS — MR. DAVIS ----

label day1_physics:

    scene bg schoolClassroom with dissolve

    show davis at right with dissolve
    davis "Projectile motion. Classic. Who can give me the horizontal velocity equation?"
    "He scans the room."
    davis "New student. Let's see what you've got."

    menu:
        "Answer?":
            "[player_name]: Horizontal velocity stays constant — v-sub-x equals the initial horizontal velocity. No horizontal force means no change."
            davis "Exactly. No air resistance, no acceleration. Good."
            hide davis with dissolve
            jump day1_physics_problem
        "Give the wrong equation.":
            "[player_name]: v equals v-naught minus g-t?"
            davis "That's the vertical component. Different axis. But you're thinking in the right direction."
            hide davis with dissolve
            jump day1_physics_problem
        "Pass.":
            "[player_name]: I'd rather not."
            davis "Fair enough. Pay attention."
            hide davis with dissolve
            jump day1_physics_problem

label day1_physics_problem:

    show davis at right with dissolve
    davis "Problem on the board. A ball is launched horizontally from a 45-meter cliff at 12 m/s. How long until it hits the ground, and where does it land?"
    hide davis with dissolve

    "You work it. d = ½gt². t = √(2×45/9.8). About 3.03 seconds. x = 12 × 3.03 ≈ 36.3 meters."

    menu:
        "Do you share your work?"

        "Write it on the board when he asks for volunteers.":
            show davis at right with dissolve
            "You go up. Your work is right."
            davis "Clean. Sit down."
            hide davis with dissolve
            "A few people copy your numbers."
            jump day1_lunch

        "Keep it to yourself.":
            "Someone else goes up. Their answer matches yours."
            "You feel quietly good about that."
            jump day1_lunch

        "You didn't finish in time.":
            show davis at right with dissolve
            davis "Always finish the full problem. Time and distance — both."
            hide davis with dissolve
            jump day1_lunch

## ---- DAY 1: LUNCH ----

label day1_lunch:

    scene bg schoolCafeteria with dissolve

    "Lunch. The cafeteria is enormous and already loud when you walk in."
    "Every table is a territory you don't have a map for."

    menu:
        "Where do you sit?"

        "Get food and find an empty table by the window.":
            "You grab a tray — rice, chicken, juice — and find a spot near the glass."
            "Nobody talks to you. You watch the room."
            jump day1_cs

        "Sit near Jose if you met him.":
            if met_jose:
                show jose at left with dissolve
                "You spot Jose near the end of a table."
                jose "Ay, you survived the morning."
                "[player_name]: Barely."
                "He slides over. You sit. His friends glance at you once and go back to their conversation."
                hide jose with dissolve
                "By the end of lunch you've heard names: Xavier, Jacky, Sham."
                jump day1_cs
            else:
                "You look for a familiar face. There isn't one."
                "You find a spot near the window and eat alone. The chicken is actually decent."
                jump day1_cs

        "Eat outside on the front steps.":
            scene bg entrance2 with dissolve
            show grace at left with dissolve
            "Fresh air. A girl sits two steps below you, also alone, earbuds in. She looks up."
            "You nod. She nods back."
            $ met_grace = True
            hide grace with dissolve
            "Her name is Grace. You don't know that yet."
            jump day1_cs

        "Find a quiet stairwell.":
            "Third floor stairwell. You sit on the top step with a granola bar."
            "It's quiet. You need that right now."
            jump day1_cs

## ---- DAY 1: COMPUTER SCIENCE — MR. McCUEN ----

label day1_cs:

    scene bg schoolClassroom with dissolve

    show mcCuen at right with dissolve
    mcCuen "We're in the middle of our final projects. Groups of two. [player_name] — you're new, so I'll slot you into an existing group."

    if player_major == "Computer Programming":
        mcCuen "What's your background?"
        "[player_name]: CS program back home. Python mostly, some Java."
        mcCuen "Good. You're with Xavier and Jacky. They could use the help."
    elif player_major == "Cyber Security":
        mcCuen "Cyber background? We've got a security-adjacent project running. You're with Xavier and Jacky."
    else:
        mcCuen "Biotech? Interesting lens. Xavier and Jacky — you've got a third."

    hide mcCuen with dissolve

    show xavier at left with dissolve
    show jacky at right with dissolve
    "Xavier slides his laptop over."
    xavier "We're doing a top-down game prototype in Python. Movement works. Collision is broken."
    "[player_name]: What library?"
    xavier "Pygame."
    hide xavier with dissolve
    hide jacky with dissolve

    menu:
        "How do you contribute?"

        "Dig in — you know Pygame.":
            show xavier at left with dissolve
            show jacky at right with dissolve
            "[player_name]: Let me look at the collision logic."
            "You find the bug in about four minutes. A rectangle comparison on the wrong axis."
            jacky "...Okay. That was fast."
            hide xavier with dissolve
            hide jacky with dissolve
            jump day1_calculus

        "Offer to handle UI and scoring instead.":
            show xavier at left with dissolve
            "[player_name]: I can build the UI and scoring system while you two fix collision."
            xavier "Yeah, that works."
            hide xavier with dissolve
            "You spend the period building a score display. Clean and simple."
            jump day1_calculus

        "Watch and ask questions to get caught up.":
            show xavier at left with dissolve
            show jacky at right with dissolve
            "You watch Xavier walk through the codebase and ask questions."
            "By the end you understand the structure."
            jacky "You can handle the menu screen?"
            "[player_name]: Yeah."
            hide xavier with dissolve
            hide jacky with dissolve
            jump day1_calculus

## ---- DAY 1: CALCULUS — MS. LI ----

label day1_calculus:

    scene bg schoolClassroom with dissolve

    show li at right with dissolve
    "Ms. Li writes before the bell finishes ringing. The board already has three integrals on it."
    li "Integration by parts. Last week you should have practiced problems 12 through 20. Today we go over 17 and 19."
    "She turns. She sees you."
    li "[player_name]. Transfer student. What have you covered in calc?"
    "[player_name]: We just finished derivatives. We hadn't started integration yet."
    li "Then today you observe. Tomorrow you participate."
    hide li with dissolve

    show micheal at left with dissolve
    "The kid next to you leans over."
    micheal "Lucky. Integration by parts is the worst."
    "[player_name]: Is it hard?"
    micheal "You'll find out tomorrow."
    hide micheal with dissolve
    "His name is Michael."

    "You watch. Ms. Li is fast and expects the class to keep up."
    "The formula is: ∫u dv = uv − ∫v du"
    "It starts making sense around the third example."

    menu:
        "What do you do with the notes?"

        "Copy everything down carefully.":
            "You fill four pages. Your hand hurts. But you have it all."
            $ homework_done = True
            jump day1_english

        "Take selective notes on the key steps.":
            "Two pages. The parts where everyone else seemed lost."
            jump day1_english

        "Just watch and try to absorb it.":
            "You write almost nothing. You trust it'll click later."
            jump day1_english

## ---- DAY 1: ENGLISH — MS. REYES ----

label day1_english:

    scene bg schoolClassroom with dissolve

    show reyes at right with dissolve
    reyes "Last period. We're going over 'The Ones Who Walk Away from Omelas' by Ursula K. Le Guin."
    reyes "The city of Omelas is perfect — joyful, abundant — built on the suffering of one child kept in a basement. Everyone knows. Most stay. Some walk away."
    reyes "Is walking away enough? Is it moral to simply remove yourself from a system you benefit from?"
    "The room is quiet."
    reyes "We have someone new. [player_name] — you can answer or pass. First day, your call."

    menu:
        "What do you do?"

        "Answer seriously.":
            "[player_name]: Walking away feels like it lets you off the hook without actually changing anything. You're not complicit, but you're not helping either."
            reyes "So what's the moral option?"
            "[player_name]: Stay and try to change it. Even if that makes you complicit in the short term."
            reyes "That's the argument Le Guin doesn't make — she just presents the choice. Interesting that you went there."
            hide reyes with dissolve
            jump day1_after_school

        "Give a shorter take.":
            "[player_name]: Walking away is still choosing to do nothing."
            reyes "Is doing nothing the same as doing harm?"
            "[player_name]: Sometimes."
            hide reyes with dissolve
            jump day1_after_school

        "Pass.":
            "[player_name]: I'll pass. First day."
            reyes "Fair. You'll have plenty of time to get into it."
            hide reyes with dissolve
            jump day1_after_school

## ---- DAY 1: AFTER SCHOOL ----

label day1_after_school:

    scene bg entrance1 with dissolve

    "3:15. The building empties fast."
    "Fordham Road is loud and alive in the afternoon."

    menu:
        "What do you do after school?"

        "Head straight to the subway.":
            jump day1_subway_home

        "Walk around the neighborhood.":
            scene bg downtownStreet with dissolve
            "You walk east on Fordham. A dollar van honks at no one. A woman sells flowers from a bucket."
            "You pass a West African restaurant, a nail salon, a cell phone repair place that's also a barber somehow."
            jump day1_subway_home

        "Stop at the bodega again.":
            scene bg bodega with dissolve
            show ock at right with dissolve
            ock "You're back."
            "[player_name]: Long day."
            ock "Arizona?"
            "[player_name]: Yeah."
            hide ock with dissolve
            "He grabs one from the cooler and slides it across."
            jump day1_subway_home

label day1_subway_home:

    scene bg subwayStation with dissolve

    if knows_train:
        "You know which train. B or D north. The D comes first. You get on."
    else:
        "You check your phone map this time. D train north."

    scene bg subwayNight1 with dissolve

    "The car is less crowded heading home. You get a seat."

    scene bg room with dissolve

    "The apartment is quiet. There's food in the fridge with a note: 'Heat for 2 min. — Mom'"
    "You sit on the couch and stare at the ceiling. One day down."

    if homework_done:
        "You pull out your calculus notes and read through them once more before sleeping."
        "The integration by parts formula is already starting to stick."
    else:
        "You think about those calc problems. You should look them up tonight."
        "You do not look them up tonight."

    jump nycday2


## ============================================================
##  DAY 2
## ============================================================

label nycday2:

    scene bg room with dissolve

    "The alarm goes off at 6:45. This time you know where you are."
    "That's already better than yesterday."

    menu:
        "How do you start Day 2?"
        "Up immediately.":
            "You're moving before the second alarm."
            jump day2_bodega
        "Snooze once.":
            "7:15. Still manageable."
            jump day2_bodega
        "Snooze twice. Yesterday was a lot.":
            "It was. Now it's 7:35. You move fast."
            jump day2_subway

## ---- DAY 2: BODEGA ----

label day2_bodega:

    scene bg bodega with dissolve

    show ock at right with dissolve
    ock "You again."
    "[player_name]: Every day apparently."
    ock "Arizona?"
    "[player_name]: And the sandwich."
    ock "Salt pepper ketchup."
    "[player_name]: Yeah."
    hide ock with dissolve
    "Duchess doesn't acknowledge you. Progress."
    jump day2_subway

## ---- DAY 2: SUBWAY ----

label day2_subway:

    scene bg subwayStation with dissolve

    "205th Street. You find the B/D without hesitating."

    if met_grace:
        show grace at left with dissolve
        "Grace is on the platform again. She's reading a book."
        grace "You made it yesterday."
        "[player_name]: Eventually."
        grace "The 4 goes to the stadium."
        "[player_name]: I know that now."
        hide grace with dissolve
        "The D pulls in. You ride in the same car but don't speak again."
    else:
        "D train. You've got it."
        "A man across from you plays chess on his phone with the sound on."

    jump day2_arrive

## ---- DAY 2: ARRIVAL ----

label day2_arrive:

    scene bg entrance2 with dissolve

    "You make it to Bronx Science on time. The security guard nods — he recognizes you."

    show jose at left with dissolve
    jose "Yo. You take the D?"
    "[player_name]: Yeah."
    jose "B is slower but less crowded."
    jose "Ms. Li is going to call on you today, by the way. She said 'tomorrow you participate.' She meant it."
    hide jose with dissolve

    jump day2_chemistry

## ---- DAY 2: CHEMISTRY — MS. WHITTINGTON ----

label day2_chemistry:

    scene bg lab with dissolve

    show whittington at right with dissolve
    whittington "Lab reports from yesterday's galvanic cell were due this morning."
    whittington "Some of you handed in something that made me sad."
    whittington "[player_name], you're new so yours isn't due until Friday. But I want you to write the methods section today during lab."
    hide whittington with dissolve

    menu:
        "How do you approach it?"
        "Start it now while the experiment is fresh.":
            show leah at left with dissolve
            leah "That actually looks good."
            "[player_name]: Thanks."
            hide leah with dissolve
            $ homework_done = True
            jump day2_chem_lab
        "Wait and do it at home.":
            "You watch the setup and take mental notes."
            jump day2_chem_lab
        "Ask Leah what format she used.":
            show leah at left with dissolve
            "[player_name]: Can I see your structure?"
            leah "Sure. But write your own — she'll know."
            hide leah with dissolve
            jump day2_chem_lab

label day2_chem_lab:

    show whittington at right with dissolve
    whittington "Today: copper electroplating. You'll deposit copper onto a steel electrode using an electrolytic cell."
    hide whittington with dissolve

    show leah at left with dissolve
    "Leah sets up the power supply. You clip the leads."
    leah "You do know what you're doing."
    "[player_name]: Slowly."
    "The electrode starts turning pink-copper after about two minutes."
    leah "That's electroplating."
    "[player_name]: That's actually kind of beautiful."
    "She shrugs like she stopped finding it beautiful three lab reports ago. But she's smiling a little."
    hide leah with dissolve

    jump day2_physics

## ---- DAY 2: PHYSICS — MR. DAVIS ----

label day2_physics:

    scene bg schoolClassroom with dissolve

    show davis at right with dissolve
    davis "Momentum. Conservation of momentum. Classic collision problems."
    "He writes two scenarios — elastic and inelastic."
    davis "What's the difference between an elastic and inelastic collision? [player_name]."

    menu:
        "Answer?":
            "[player_name]: Elastic conserves both momentum and kinetic energy. Inelastic only conserves momentum — kinetic energy is lost to heat or deformation."
            davis "Perfect. Someone did some reading."
            hide davis with dissolve
            jump day2_physics_problem
        "Take a guess.":
            "[player_name]: Elastic means they bounce off. Inelastic means they stick?"
            davis "Mostly right. The formal distinction is kinetic energy. But you're thinking correctly."
            hide davis with dissolve
            jump day2_physics_problem
        "Say you're not sure.":
            "[player_name]: I haven't covered this yet."
            davis "Pay attention. You will."
            hide davis with dissolve
            jump day2_physics_problem

label day2_physics_problem:

    show davis at right with dissolve
    davis "Problem: a 2 kg cart at 4 m/s hits a stationary 3 kg cart. They stick together. Final velocity?"
    hide davis with dissolve

    "You work it. p = mv. 2×4 = 8 kg⋅m/s. Final mass = 5 kg. v = 8/5 = 1.6 m/s."

    menu:
        "Share your answer?":
            show davis at right with dissolve
            davis "Correct. Inelastic. Momentum holds, kinetic energy doesn't. Good."
            hide davis with dissolve
            jump day2_lunch
        "Check against whoever goes up.":
            show micheal at left with dissolve
            "Michael goes up. His answer matches yours."
            hide micheal with dissolve
            jump day2_lunch
        "You got a different answer.":
            show davis at right with dissolve
            davis "Remember: the mass after collision is the combined mass. Common mistake."
            hide davis with dissolve
            jump day2_lunch

## ---- DAY 2: LUNCH ----

label day2_lunch:

    scene bg schoolCafeteria with dissolve

    "Lunch again. You know where the line is. You know the good side of the cafeteria."

    if met_jose:
        show jose at left with dissolve
        show xavier at right with dissolve
        jose "Sit with us."
        xavier "The collision code is fine now."
        show jacky at right with dissolve
        jacky "The hitbox is still wrong."
        xavier "The hitbox is a square."
        jacky "It's the wrong size square."
        jose "They've been like this since homeroom."
        hide jose with dissolve
        hide xavier with dissolve
        hide jacky with dissolve
        "You eat and listen. It's comfortable. That's a good sign."
    else:
        "You find a window seat. The cafeteria makes more sense today."

    jump day2_cs

## ---- DAY 2: COMPUTER SCIENCE — MR. McCUEN ----

label day2_cs:

    scene bg schoolClassroom with dissolve

    show mcCuen at right with dissolve
    mcCuen "Project check-in. Groups — where are you?"
    show xavier at left with dissolve
    xavier "Movement and collision are fixed. Working on enemy AI now."
    mcCuen "What kind of AI?"
    xavier "Basic pathfinding. Maybe A*."
    hide xavier with dissolve

    menu:
        "How do you contribute?"

        "Suggest a state machine instead of A*.":
            "[player_name]: A* might be heavy for the scope. State machine could work — patrol, chase, attack."
            mcCuen "Reasonable tradeoff. Xavier?"
            show xavier at left with dissolve
            show jacky at right with dissolve
            xavier "Yeah, actually. Faster to build."
            jacky "...Fine."
            hide mcCuen with dissolve
            hide xavier with dissolve
            hide jacky with dissolve
            jump day2_cs_work

        "Help implement A* using a grid map.":
            show xavier at left with dissolve
            "[player_name]: I can help with A* if we use a grid-based layout."
            xavier "That's the plan."
            hide mcCuen with dissolve
            hide xavier with dissolve
            jump day2_cs_work

        "Stay quiet and let them decide.":
            hide mcCuen with dissolve
            "They land on a simplified pathfinding approach."
            "You take notes and wait to be assigned something."
            jump day2_cs_work

label day2_cs_work:

    scene bg schoolClassroom with dissolve

    show jacky at right with dissolve
    "You work for the rest of the period."
    "Jacky leans over to look at your code."
    jacky "Why'd you structure it like that?"
    "[player_name]: So the states are easy to add later."
    jacky "Okay. Yeah."
    hide jacky with dissolve
    "High praise."

    jump day2_calculus

## ---- DAY 2: CALCULUS — MS. LI ----

label day2_calculus:

    scene bg schoolClassroom with dissolve

    show li at right with dissolve
    li "Yesterday you observed. Today you participate."
    "She writes on the board: ∫ x·eˣ dx"
    li "[player_name]. Walk me through it."
    "The class goes quiet."
    hide li with dissolve

    if homework_done:
        "You reviewed the notes last night. You know the formula."

        menu:
            "Work through it?"

            "Yes — u = x, dv = eˣ dx.":
                "[player_name]: Let u equal x, so du equals dx. Let dv equal e-to-the-x dx, so v equals e-to-the-x."
                show li at right with dissolve
                li "Continue."
                "[player_name]: The integral becomes x times e-to-the-x, minus the integral of e-to-the-x — which gives x-e-to-the-x minus e-to-the-x, plus C."
                li "Correct. Exactly right."
                hide li with dissolve
                show micheal at left with dissolve
                micheal "I said it was the worst."
                "[player_name]: It's not that bad."
                micheal "Give it a week."
                hide micheal with dissolve
                jump day2_english

            "Get the setup right but lose the final step.":
                "[player_name]: u equals x, dv equals e-to-the-x... so the integral becomes x-e-to-the-x minus the integral of e-to-the-x..."
                "You pause."
                show li at right with dissolve
                li "And?"
                "[player_name]: Minus e-to-the-x plus C."
                li "Correct. Don't pause like that on an exam."
                hide li with dissolve
                jump day2_english
    else:
        "[player_name]: u equals x, dv equals e-to-the-x."
        show li at right with dissolve
        li "And?"
        "[player_name]: I lose it after the setup."
        li "The integral of v du. That's where you stopped. Write that tonight."
        hide li with dissolve
        jump day2_english

## ---- DAY 2: ENGLISH — MS. REYES ----

label day2_english:

    scene bg schoolClassroom with dissolve

    show reyes at right with dissolve
    reyes "Le Guin. We're still in Omelas, but today I want to talk about the child."
    "She reads a passage aloud — the description of the basement. The room is unusually quiet."
    reyes "Le Guin is specific: the citizens must understand. They can't pretend. They have to know. Why does that matter?"

    menu:
        "What do you say?"

        "Because ignorance is the easiest excuse.":
            "[player_name]: If you're allowed to not know, everyone just chooses not to know. The knowledge is what makes the moral weight real."
            reyes "So guilt requires awareness."
            "[player_name]: Or at least the refusal to look away."
            hide reyes with dissolve
            jump day2_after_school

        "Because it makes staying a choice, not a default.":
            "[player_name]: If you know and stay anyway, that's a decision. You own it."
            reyes "And is owning it enough?"
            "[player_name]: Probably not."
            hide reyes with dissolve
            jump day2_after_school

        "Stay quiet.":
            "You listen. Two kids in the back genuinely disagree."
            "Ms. Reyes catches your eye at one point. You shrug. She almost smiles."
            hide reyes with dissolve
            jump day2_after_school

## ---- DAY 2: AFTER SCHOOL ----

label day2_after_school:

    scene bg entrance2 with dissolve

    show jose at left with dissolve
    jose "Yo — we're going to the park near the stadium. You coming?"

    menu:
        "Do you go?"

        "Yeah. Let's go.":
            hide jose with dissolve
            scene bg downtownPark with dissolve
            show leah at right with dissolve
            leah "You're adjusting fast."
            "[player_name]: I don't feel like it."
            leah "Day one you looked like you were doing math in your head the whole time."
            "[player_name]: I probably was."
            hide leah with dissolve
            "You stay until the light goes orange."
            jump day2_home

        "Nah. I've got homework.":
            "[player_name]: Maybe tomorrow. I've got the calc stuff to catch up on."
            show jose at left
            jose "Ms. Li got to you."
            hide jose with dissolve
            jump day2_home

        "Walk home the long way.":
            hide jose with dissolve
            scene bg downtownStreet with dissolve
            "You walk south on Jerome Avenue, past the elevated tracks."
            "The 4 runs overhead. You watch it go. You know which train that is now."
            jump day2_home

label day2_home:

    scene bg room with dissolve

    "Home. The fold-out couch feels more familiar tonight."

    menu:
        "What do you actually do?"
        "All of it — full study session.":
            "Two hours. Lab report. Three integration problems. Physics reading."
            $ homework_done = True
            jump nycday3
        "Calc first. That's the one that matters.":
            "You finish the integration practice. Lab report tomorrow morning."
            jump nycday3
        "Fall asleep reading.":
            "Xavier sends a meme. Jacky sends a code snippet."
            "You read for twenty minutes and fall asleep with your notes on your chest."
            $ homework_done = False
            jump nycday3


## ============================================================
##  DAY 3
## ============================================================

label nycday3:

    scene bg room with dissolve

    "Day 3."
    "The alarm goes off. You're already mostly awake."
    "Something about this city — it never fully goes quiet, so you never fully go under."
    "You've started to not mind it."

    scene bg kitchen with dissolve
    show mom at right with dissolve
    "There's a note on the counter."
    "'Calculus quiz today? I don't know. Good luck either way. — Mom'"
    hide mom with dissolve
    "There's no quiz today. But the thought is nice."

    jump day3_bodega

## ---- DAY 3: BODEGA ----

label day3_bodega:

    scene bg bodega with dissolve

    show ock at right with dissolve
    ock "Salt pepper ketchup?"
    "You didn't even order yet."
    "[player_name]: Yeah."
    hide ock with dissolve
    "Duchess is on top of the cooler now. You look at her. She looks at you."
    "You both accept this arrangement."
    jump day3_subway

## ---- DAY 3: SUBWAY ----

label day3_subway:

    scene bg subwayStation with dissolve

    "205th. D train. You don't check the board anymore."

    if met_grace:
        show grace at left with dissolve
        "Grace is there again. On the same page of the same book."
        grace "Slow reader?"
        grace "I read it three times."
        "[player_name]: What is it?"
        "She holds up the cover. 'The Dispossessed.' Ursula K. Le Guin."
        "[player_name]: We're reading Le Guin in English."
        grace "Ms. Reyes?"
        "[player_name]: Yeah."
        grace "She does Omelas every year. It's the one that sticks."
        hide grace with dissolve
    else:
        "A man across the car is eating a full plate of rice and beans at 7:40 AM."
        "This city contains everything."

    jump day3_arrive

## ---- DAY 3: ARRIVAL ----

label day3_arrive:

    scene bg entrance2 with dissolve

    show guard at right with dissolve
    "The security guard who checked your bag on Day 1 recognizes you now."
    "He doesn't wave you to the side."
    hide guard with dissolve
    "Small thing. Feels big."
    jump day3_chemistry

## ---- DAY 3: CHEMISTRY — MS. WHITTINGTON ----

label day3_chemistry:

    scene bg lab with dissolve

    show whittington at right with dissolve
    whittington "Lab reports. I've read them."
    whittington "Some of you are rewriting the results section. You know who you are."
    whittington "[player_name] — your methods section was clean. Results next time."
    "[player_name]: Yes, Ms. Whittington."
    whittington "Today: titration. Sodium hydroxide to find the concentration of an unknown acid."
    hide whittington with dissolve

    show leah at left with dissolve
    leah "You've done titrations before?"
    "[player_name]: Once. Back home."
    leah "Here the unknown is actually unknown. She changes it every semester."
    "[player_name]: So we actually have to do the math."
    leah "We actually have to do the math."
    hide leah with dissolve

    "You work carefully. Three trials. Values within 0.2 mL of each other."

    show whittington at right with dissolve
    whittington "Good consistency, [player_name]. Leah, same to you."
    hide whittington with dissolve

    show leah at left with dissolve
    leah "We make a decent team."
    hide leah with dissolve

    jump day3_physics

## ---- DAY 3: PHYSICS — MR. DAVIS ----

label day3_physics:

    scene bg schoolClassroom with dissolve

    show davis at right with dissolve
    davis "Test Friday. Projectile motion, conservation of momentum, Newton's laws."
    davis "[player_name] — you're excused from Friday since you're still catching up. Attempt the practice exam instead."
    "[player_name]: I'll do the real one."
    davis "...You sure?"
    "[player_name]: Yeah."
    davis "Okay. You're in."
    hide davis with dissolve

    show micheal at left with dissolve
    micheal "Why would you do that."
    "[player_name]: I want to know where I actually am."
    micheal "That's the most transferred-from-another-state thing I've ever heard."
    hide micheal with dissolve

    "Davis runs a full review. You work through every problem alongside the class."
    "The momentum problems you get. Projectile motion — mostly."
    jump day3_lunch

## ---- DAY 3: LUNCH ----

label day3_lunch:

    scene bg schoolCafeteria with dissolve

    "Lunch. You go to Jose's table without being asked. You just sit down."
    "Nobody makes a thing out of it."

    show jose at left with dissolve
    show xavier at right with dissolve
    show jacky at right with dissolve
    jose "Physics test Friday."
    xavier "I know."
    jose "You studying?"
    xavier "I'm always studying."
    jacky "You're never studying."
    xavier "I'm always studying in spirit."
    show leah at left with dissolve
    leah "That's not how tests work."
    hide jose with dissolve
    hide xavier with dissolve
    hide jacky with dissolve
    hide leah with dissolve

    "You eat. The conversation moves. At one point you say something and everyone responds naturally."
    "Like you've been here longer than three days."

    jump day3_cs

## ---- DAY 3: COMPUTER SCIENCE — MR. McCUEN ----

label day3_cs:

    scene bg schoolClassroom with dissolve

    show mcCuen at right with dissolve
    mcCuen "Presentations in two weeks. Playable prototype by next Friday."
    mcCuen "What's the game?"

    show xavier at left with dissolve
    if player_major == "Computer Programming":
        xavier "Top-down survival. Avoid enemies. Score goes up."
        mcCuen "Simple. Achievable. Good."
    elif player_major == "Cyber Security":
        xavier "A hacker avoiding security protocols. Enemies are detection systems."
        mcCuen "I like that. Fits the curriculum."
    else:
        xavier "A cell avoiding pathogens."
        "[player_name]: That was me."
        mcCuen "Interesting application. Make it work."

    hide mcCuen with dissolve
    hide xavier with dissolve

    show jacky at right with dissolve
    "You spend the period getting the prototype presentable."
    "At one point Jacky and you are debugging the same function from opposite ends."
    jacky "I found it."
    "[player_name]: I found it first."
    jacky "Prove it."
    "[player_name]: We found it at the same time."
    jacky "Fine."
    hide jacky with dissolve

    jump day3_calculus

## ---- DAY 3: CALCULUS — MS. LI ----

label day3_calculus:

    scene bg schoolClassroom with dissolve

    show li at right with dissolve
    li "Quiz today. Five problems — integration by parts and u-substitution."
    li "[player_name] — you've had two days. You take it for practice. Ungraded."
    hide li with dissolve

    menu:
        "Do you take it seriously anyway?"

        "Yes — every problem.":
            "You work through all five."
            if homework_done:
                "The u-substitution ones are clean. Integration by parts takes longer but you finish."
                show li at right with dissolve
                li "Not bad for two days."
                hide li with dissolve
            else:
                "You get through three. The last two are messier."
                show li at right with dissolve
                li "Work on your method consistency."
                hide li with dissolve
            jump day3_english

        "Do the ones you know, skip the rest.":
            "You finish three. Set up the other two but don't complete them."
            show li at right with dissolve
            li "The setup is right on both. You stopped too early."
            "[player_name]: I wasn't sure of the next step."
            li "That's what practice is for. Do it tonight."
            hide li with dissolve
            jump day3_english

        "Write your name and observe.":
            "You follow along on scratch paper."
            show li at right with dissolve
            li "You can do more than that."
            "[player_name]: I know."
            li "Then do it."
            hide li with dissolve
            jump day3_english

## ---- DAY 3: ENGLISH — MS. REYES ----

label day3_english:

    scene bg schoolClassroom with dissolve

    show reyes at right with dissolve
    reyes "Last day on Omelas — for now. I want to return to it at the end of the semester."
    reyes "You've been a stranger this week, [player_name]. New city, new school."
    reyes "Is it easier to walk away from a place you've never been — or a place that's become home?"

    menu:
        "What do you say?"

        "Easier to walk away when you don't belong yet.":
            "[player_name]: When you just got somewhere, you haven't invested in it. It's easier to leave what you haven't chosen."
            reyes "And once you've chosen it?"
            "[player_name]: Then leaving means admitting you chose wrong."
            reyes "Le Guin would've liked that answer. It has weight."
            hide reyes with dissolve
            jump day3_after_school

        "Harder to walk away when you're the stranger.":
            "[player_name]: When you're new, leaving feels like failure. You haven't earned the right to have an opinion yet."
            reyes "So belonging is a prerequisite for moral agency?"
            "[player_name]: Maybe for feeling like you're allowed to have one."
            hide reyes with dissolve
            jump day3_after_school

        "I don't know yet. Ask me in a week.":
            "[player_name]: I've been here three days. Ask me when I actually know what I've accepted and what I haven't."
            reyes "I'll hold you to that."
            hide reyes with dissolve
            jump day3_after_school

## ---- DAY 3: AFTER SCHOOL ----

label day3_after_school:

    scene bg entrance2 with dissolve

    show jose at left with dissolve
    show xavier at right with dissolve
    show jacky at right with dissolve
    show leah at left with dissolve
    jose "Park?"
    "Everyone looks at you."
    hide jose with dissolve
    hide xavier with dissolve
    hide jacky with dissolve
    hide leah with dissolve

    menu:
        "What do you say?"

        "Yeah. Let's go.":
            scene bg downtownPark with dissolve
            show jose at left with dissolve
            show xavier at right with dissolve
            "You play two-on-two with Jose and Xavier. You win once. Lose twice."
            hide jose with dissolve
            hide xavier with dissolve
            show jacky at left with dissolve
            jacky "You're staying, right? Not transferring back?"
            "[player_name]: I don't know yet."
            jacky "The game won't run without you at this point."
            "[player_name]: That's a low bar."
            jacky "Take it."
            hide jacky with dissolve
            jump day3_subway_home

        "In a bit. I want to walk first.":
            scene bg downtownStreet with dissolve
            "Fordham Road, Grand Concourse, a park with old men playing dominoes."
            "Pieces of the city are starting to feel like yours."
            jump day3_subway_home

        "I should study for Friday.":
            show jose at left with dissolve
            jose "On a Wednesday?"
            "[player_name]: Physics test."
            jose "You said you were taking it for real."
            "[player_name]: Exactly."
            jose "Tomorrow then."
            hide jose with dissolve
            jump day3_subway_home

label day3_subway_home:

    scene bg subwayStation with dissolve

    "Fordham Road station. D train north. You don't think about which train. You just go."

    scene bg subwayNight1 with dissolve

    "In the car, you open your notebook."
    "Physics formulas. Calc. The structure of a galvanic cell. Le Guin."
    "A kid across the car is doing the same thing — headphones in, notebook out, completely somewhere else."
    "You recognize that look."

    scene bg room with dissolve

    "Home. The fold-out couch."
    "Three days."
    "You know the train. You know the bodega. You know the teachers and which questions they're going to ask."
    "You know Leah is meticulous in the lab. You know Jacky codes from the outside in."
    "You know Michael has already done the calc problems three times."
    "You know Grace reads Le Guin on the D train."

    "You don't know if you're staying."
    "But tonight, for the first time, you're not sure you want to leave."

    menu:
        "Play again from the beginning?":
            jump start
        "Continue from here?":
            "More days coming. Hold tight."
            return
        "That's enough for now.":
            return
