from items import *

dialogue_start = {
    "name": "Bedroom",
    "description":
    """Opening your eyes, you feel dizzy. What happened last night? Wait a moment, it's Thursday already- you have your final exam today! You're going to be late if you don't hurry, but are you ready for the exam? First things first, you need to sort out this headache! """,
    "numbers":{"1": "dialogue_bedroom"},
    "time" : 0,
    "items": []
}

dialogue_bedroom = {
    "name":"to look round your bedroom",
    "description":"""
                 _____________    _____________
                |             |__|             |
                |   Bedroom    __   Bathroom   |
                |      X      |  |             |
                |_____   _____|  |_____________|
                      | |
                  ____| |____    ______________
 _____________   |           |  |              |
|             |  |           |  |              |
|   Jason's   |__|           |__|              |
|    Room      __   Hallway   __    Kitchen    |
|_____________|  |           |  |              |
                 |           |  |              |
                 |____   ____|  |______________|
                      | |


    You stand up and spot your phone on the table nearby.""",
    "numbers":{"1": "dialogue_hallway", "2": "dialogue_phone", "3": "dialogue_bathroom"},
    "items": [],
    "time":0

}

dialogue_hallway = {
    "name":"to go into your flats hallway",
    "description":"""
                 _____________    _____________
                |             |__|             |
                |   Bedroom    __   Bathroom   |
                |             |  |             |
                |_____   _____|  |_____________|
                      | |
                  ____| |____    ______________
 _____________   |           |  |              |
|             |  |           |  |              |
|   Jason's   |__|           |__|              |
|    Room      __   Hallway   __    Kitchen    |
|_____________|  |     X     |  |              |
                 |           |  |              |
                 |____   ____|  |______________|
                      | |
You step into the narrow hallway connecting you and your faltmates rooms. You really need to clean this place.""",
    "numbers":{"1": "dialogue_kitchen", "2": "dialogue_bedroom", "3": "dialogue_jason", "4": "dialogue_outside"},
    "items": [],
    "time":0

}

dialogue_kitchen = {
    "name": "to go the kitchen",
    "description":"""
                 _____________    _____________
                |             |__|             |
                |   Bedroom    __   Bathroom   |
                |             |  |             |
                |_____   _____|  |_____________|
                      | |
                  ____| |____    ______________
 _____________   |           |  |              |
|             |  |           |  |              |
|   Jason's   |__|           |__|              |
|    Room      __   Hallway   __    Kitchen    |
|_____________|  |           |  |      X       |
                 |           |  |              |
                 |____   ____|  |______________|
                      | |
You go to the kitchen, some food should wake you up. A post-it left on your chair tells you that your friend Denise called round in the morning to say she’s studying at the library.""",
    "time":5,
    "numbers": {"1": "dialogue_breakfast", "2": "dialogue_coffee"},
    "items": []
}

dialogue_bathroom = {
    "name": "to go to the bathroom",
    "description":"""
                 _____________    _____________
                |             |__|             |
                |   Bedroom    __   Bathroom   |
                |             |  |      X      |
                |_____   _____|  |_____________|
                      | |
                  ____| |____    ______________
 _____________   |           |  |              |
|             |  |           |  |              |
|   Jason's   |__|           |__|              |
|    Room      __   Hallway   __    Kitchen    |
|_____________|  |           |  |              |
                 |           |  |              |
                 |____   ____|  |______________|
                      | |
You take a quick look at yourself in the mirror, and come to the conclusion that you should really have a shower...""",
    "numbers": {"1":"dialogue_shower", "2":"dialogue_brush_teeth", "3":"dialogue_bedroom"},
    "items": [item_paracetemol],
    "time":0
}

dialogue_shower = {
    "name":"to take a shower",
    "description" : "You shower quickly and half-dry your hair with a towel.",
    "numbers": {"1":"dialogue_brush_teeth", "2":"dialogue_bedroom"},
    "items": [item_paracetemol]
}

dialogue_brush_teeth = {
    "name":"to brush teeth",
    "description" : "You go to brush your teeth but find you've run out of toothpaste. Water will have to do for today.",
    "numbers": {"1":"dialogue_shower", "2":"dialogue_paracetamol", "3":"dialogue_bedroom"},
    "items": [],
    "time":0
}

dialogue_phone = {
    "name": "to reach for phone",
    "description":"You reach for your phone, and notice that there is a photo of you making paper airplanes with your notes next door. Maybe your notes would help with the exam?",
    "time": 10,
    "numbers": {"1": "dialogue_hallway", "2": "dialogue_bathroom"},
    "items": []
    
}

dialogue_jason = {
    "name": "to knock on Jason's door.",
    "description":"You knock and find no answer. Damnit Jason, wake up!",
    "time": 5,
    "numbers": {"1": "dailogue_wait", "2": "dialogue_hallway"},
    "items": []
}

dialogue_coffee = {
    "name": "to make coffee",
    "description":"This will boost your energy",
    "time": 5,
    "numbers": {"1": "dialogue_hallway", "2": "dialogue_breakfast"},
    "items":[item_coffee]
}

dialogue_breakfast = {
    "name": "to make breakfast",
    "description":"You find a Python book in the cereal box. What a coincidence.",
    "numbers": {"1": "dialogue_coffee", "2":"dialogue_hallway"},
    "time": 15,
    "items":[item_textbook]

}

dialogue_wait = {
    "name": "to wait",
    "description" : """
                 _____________    _____________
                |             |__|             |
                |   Bedroom    __   Bathroom   |
                |             |  |             |
                |_____   _____|  |_____________|
                      | |
                  ____| |____    ______________
 _____________   |           |  |              |
|             |  |           |  |              |
|   Jason's   |__|           |__|              |
|    Room X    __   Hallway   __    Kitchen    |
|_____________|  |           |  |              |
                 |           |  |              |
                 |____   ____|  |______________|
                      | |
You wait and knock again after 5 minutes and the door is answered, a grumpy Jason answers the door, and falls back into bed. You notice your notes on the floor.""",
    "numbers":{"1":"dialogue_hallway"},
    "time":5,
    "items": [item_notes]

}

dialogue_outside = {
    "name": "to leave the flat",
    "description" : "You stumble towards the computer science building, head pounding all the way. You don't feel like doing this walk again for a while.",
    "numbers":{"1":"dialogue_reception"},
    "time":60,
    "items": []
}

dialogue_library = {
    "name":"to go to the library",
    "description":"""
            | |
 ___________| |______
|                    |
|     Reception      |
|                    |       _______________
|_____   ____________|      |               |
      | |                   |Kirill's Office|
   ___| |___                |               |
  |         |               |______   ______|
  |         |                      | |      _________________
  |         |______________________| |__   |                 |
  |                                     |  |                 |
  |             Stairwell               |__|                 |
  |                                      __      Library     |
  |____________________   ______________|  |        X        |
                       | |                 |                 |
              _________| |_________        |_________________|
             |                     |
             |      Exam Hall      |
             |                     |
             |_____________________|
You meet Denise in the library and study for half an hour soon your stomach is rumbling and energy is low. Do you have the time to grab something to eat?""",
    "numbers":{"1":"dialogue_food", "2":"dialogue_continue"},
    "items": [],
    "time":0
}

dialogue_food = {
    "name":"to go to the hallway and grab some food",
    "description":"As you step back into the hallway, you notice Kirill's offfice door has been left ajar.",
    "numbers":{"1":"dialogue_investigate", "2":"dialogue_stairwell"},
    "items": [],
    "time":0
}

dialogue_continue = {
    "name": "to continue studying",
    "description" : "You push yourself and continue studying for a little longer.",
    "numbers":{"1":"dialogue_stairwell"},
    "time":60,
    "items": []
}

dialogue_investigate = {
    "name":"to investigate the office",
    "description":"""
            | |
 ___________| |______
|                    |
|     Reception      |
|                    |       _______________
|_____   ____________|      |               |
      | |                   |Kirill's Office|
   ___| |___                |       X       |
  |         |               |______   ______|
  |         |                      | |      _________________
  |         |______________________| |__   |                 |
  |                                     |  |                 |
  |             Stairwell               |__|                 |
  |                                      __      Library     |
  |____________________   ______________|  |                 |
                       | |                 |                 |
              _________| |_________        |_________________|
             |                     |
             |      Exam Hall      |
             |                     |
             |_____________________|
You step into the office and are relieved to find it unoccupied. You sit at the computer, but something pops up on the screen. It seems to be a puzzle. Will you attempt it?""",
    "numbers":{"yes":"dialogue_puzzle", "leave":"dialogue_stairwell"},
    "items": [],
    "time":0
}

dialogue_stairwell = {
    "name":"to go to the stairwell",
    "description":"""
            | |
 ___________| |______
|                    |
|     Reception      |
|                    |       _______________
|_____   ____________|      |               |
      | |                   |Kirill's Office|
   ___| |___                |               |
  |         |               |______   ______|
  |         |                      | |      _________________
  |         |______________________| |__   |                 |
  |                                     |  |                 |
  |             Stairwell   X           |__|                 |
  |                                      __      Library     |
  |____________________   ______________|  |                 |
                       | |                 |                 |
              _________| |_________        |_________________|
             |                     |
             |      Exam Hall      |
             |                     |
             |_____________________|
The computerscience building is covered in posters, and smells strongly of coffee.""",
    "numbers":{"1":"dialogue_library", "2":"dialogue_reception", "3":"dialogue_examhall"},
    "items": [],
    "time":0

}
dialogue_examhall = {
    "name":"to enter the exam hall",
    "description":"""
            | |
 ___________| |______
|                    |
|     Reception      |
|                    |       _______________
|_____   ____________|      |               |
      | |                   |Kirill's Office|
   ___| |___                |               |
  |         |               |______   ______|
  |         |                      | |      _________________
  |         |______________________| |__   |                 |
  |                                     |  |                 |
  |             Stairwell               |__|                 |
  |                                      __      Library     |
  |____________________   ______________|  |                 |
                       | |                 |                 |
              _________| |_________        |_________________|
             |                     |
             |      Exam Hall      |
             |          X          |
             |_____________________|
Are you sure you are ready to do the exam?""",
    "numbers":{"yes":"EXAMSTART", "no":"dialogue_stairwell"},
    "items": [],
    "time":0

}

dialogue_reception = {
    "name":"to go into reception",
    "description":"""
            | |
 ___________| |______
|                    |
|     Reception      |
|         X          |       _______________
|_____   ____________|      |               |
      | |                   |Kirill's Office|
   ___| |___                |               |
  |         |               |______   ______|
  |         |                      | |      _________________
  |         |______________________| |__   |                 |
  |                                     |  |                 |
  |             Stairwell               |__|                 |
  |                                      __      Library     |
  |____________________   ______________|  |                 |
                       | |                 |                 |
              _________| |_________        |_________________|
             |                     |
             |      Exam Hall      |
             |                     |
             |_____________________|
The receptionist glances at you. Damn, it's always so cold in this building.""",
    "numbers":{"1":"dialogue_stairwell"},
    "items": [],
    "time":0

}

dialogue = {
    "dialogue_start": dialogue_start,
    "dialogue_bedroom":dialogue_bedroom,
    "dialogue_kitchen": dialogue_kitchen,
    "dialogue_bathroom": dialogue_bathroom,
    "dialogue_shower": dialogue_shower,
    "dialogue_phone":dialogue_phone,
    "dialogue_coffee": dialogue_coffee,
    "dialogue_breakfast": dialogue_breakfast,
    "dialogue_library": dialogue_library,
    "dialogue_wait": dialogue_wait,
    "dialogue_jason": dialogue_jason,
    "dialogue_food": dialogue_food,
    "dialogue_brush_teeth":dialogue_brush_teeth,
    "dialogue_shower":dialogue_shower,
    "dialogue_investigate":dialogue_investigate,
    "dialogue_stairwell":dialogue_stairwell,
    "dialogue_examhall":dialogue_examhall,
    "dialogue_reception":dialogue_reception,
    "dialogue_outside":dialogue_outside,
    "dialogue_continue":dialogue_continue,
    "dialogue_hallway":dialogue_hallway
}
