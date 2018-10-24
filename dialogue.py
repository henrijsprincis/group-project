from items import *

dialogue_start = {
    "name": "Bedroom",
    "description":
    """Opening your eyes, you feel dizzy. What happened last night? First things first, you need to sort out this headache! """,
    "numbers":{"1": "dialogue_bedroom"},
    "time" : 0,
    "items": []
}

dialogue_bedroom = {
    "name":"to look round your bedroom",
    "description":"You step into the office and are relieved to find it unoccupied. You sit at the computer, but something pops up on the screen. It seems to be a puzzle. Will you attempt it?",
    "numbers":{"1": "dialogue_kitchen", "2": "dialogue_phone", "3": "dialogue_bathroom"},
    "items": [],
    "time":0

}

dialogue_kitchen = {
    "name": "to go the kitchen",
    "description":"You go to the kitchen, you need something to wake you up.  You bump into your housemate.  You have quick chat about what happened last night.  He tells you that you were studying at Jason’s flat and Denise called round in the morning to say she’s studying at the library.",
    "time":5,
    "numbers": {"1": "dialogue_breakfast", "2": "dialogue_coffee"},
    "items": []
}

dialogue_bathroom = {
    "name": "to go to the bathroom",
    "description":"You smell and you definitely need a shower",
    "numbers": {"1":"dialogue_shower", "2":"take paracetamol"},
    "items": [item_paracetemol],
    "time":0
}

dialogue_shower = {
    "name":"to take a shower",
    "description" : "You've taken a shower and change your clothes, do you want to bru sh your teeth",
    "numbers": {"1":"dialogue_brush_teeth", "2":"dialogue_pracetemol"},
    "items": []
}

dialogue_brush_teeth = {
    "name":"to brush teeth",
    "description" : "You've Brushed your teeth and you take paracetemol to help with headache",
    "numbers": {"1":"dialogue_kitchen", "2":"dialogue_jason", "3":"dialogue_library"},
    "items": [],
    "time":0
}

dialogue_phone = {
    "name": "to reach for phone",
    "description":"Reach your phone and start scrolling and You discover photos from the other night. Are those your study notes on the table at pre drinks?,Call Jason to find out what happened He tells you that you left your notes at pre drinks and they are still at his flat in Taly South. You feel exhausted but you need to get up.",
    "time": 10,
    "numbers": {"1": "dialogue_kitchen", "2": "dialogue_bathroom", "3":"dialogue_jason_flat_through"},
    "items": []
    
}

dialogue_jason_flat_through = {
    "name": "to bump housemate",
    "description":"Throw on your clothes and leave to Jason’s flat. On your way out you bump into your housemate.You find out denise is at the library studying.",
    "time": 5,
    "numbers": {"1": "dailogue_jason", "2": "dialogue_library"},
    "items": []
}

dialogue_coffee = {
    "name": "to make coffee",
    "description":"This wiil boost your energy",
    "time": 5,
    "numbers": {"1": "dialogue_bathroom", "2": "dialogue_jason", "3": "dialogue_library"},
    "items":[item_coffee]
}

dialogue_breakfast = {
    "name": "to make breakfast",
    "description":"You find a Python book in the cereal box. What a coincidence.",
    "numbers": {"1": "take textbook", "2":"dialogue_bathroom","3":"dialogue_jason","4":"dialogue_library"},
    "time": 15,
    "items":[item_textbook]
}

dialogue_jason = {
    "name": "to go to Jason's Flat",
    "description" : "You go to Jsons flat and find there is no answr when you knock on the door",
    "numbers":{"1":"dialogue_wait", "2":"dialogue_outside"},
    "time":20,
    "items": []
}

dialogue_wait = {
    "name": "to wait",
    "description" : "You wait and knock again after 5 minutes and the door is answered, you enter the house and see your notes",
    "numbers":{"1":"take notes", "2":"dialogue_stay", "3":"dialogue_library"},
    "time":5,
    "items": [item_notes]
}

dialogue_stay = {
    "name": "to stay",
    "description" : "This is taking for too long. You really don't have time.",
    "numbers":{"1":"dialogue_outside"},
    "time":60,
    "items": []
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
    "description":"You meet Denise in the library and study for half an hour soon your stomach is rumbling and energy is low. Do you have the time to grab something to eat?",
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
    "description":"You step into the office and are relieved to find it unoccupied. You sit at the computer, but something pops up on the screen. It seems to be a puzzle. Will you attempt it?",
    "numbers":{"yes":"dialogue_puzzle", "leave":"dialogue_stairwell"},
    "items": [],
    "time":0
}

dialogue_stairwell = {
    "name":"to go to the stairwell",
    "description":"The computerscience building is covered in posters, and smells strongly of coffee.",
    "numbers":{"1":"dialogue_library", "2":"dialogue_reception", "3":"dialogue_examhall"},
    "items": [],
    "time":0

}
dialogue_examhall = {
    "name":"to enter the exam hall",
    "description":"Are you sure you are ready to do the exam?",
    "numbers":{"yes":"EXAMSTART", "no":"dialogue_stairwell"},
    "items": [],
    "time":0

}

dialogue_reception = {
    "name":"to go into reception",
    "description":"The receptionist glances at you. Damn, it's always so cold in this building.",
    "numbers":{"1":"dialogue_stairwell"},
    "items": [],
    "time":0

}

dialogue = {
    "dialogue_start": dialogue_start,
    "dialogue_bedroom":dislogue_bedroom,
    "dialogue_kitchen": dialogue_kitchen,
    "dialogue_bathroom": dialogue_bathroom,
    "dialogue_shower": dialogue_shower,
    "dialogue_phone":dialogue_phone,
    "dialogue_jason_flat_through": dialogue_jason_flat_through,
    "dialogue_coffee": dialogue_coffee,
    "dialogue_breakfast": dialogue_breakfast,
    "dialogue_library": dialogue_library,
    "dialogue_wait": dialogue_wait,
    "dialogue_stay": dialogue_stay,
    "dialogue_jason": dialogue_jason,
    "dialogue_food": dialogue_food,
    "dialogue_brush_teeth":dialogue_brush_teeth,
    "dialogue_shower":dialogue_shower,
    "dialogue_investigate":dialogue_investigate,
    "dialogue_stairwell":dialogue_stairwell,
    "dialogue_examhall":dialogue_examhall,
    "dialogue_reception":dialogue_reception,
    "dialogue_outside":dialogue_outside,
    "dialogue_continue":dialogue_continue
}
