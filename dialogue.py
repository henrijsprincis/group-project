from items import *

dialogue_start = {
    "name": "Bedroom",
    "description":
    """You wake up and a long night of heavy drinking is catching up on you. Have you just dreamt about Kirill? Confused, you look for something to hold on to. Your stomach is rambling, and a massive headache has made its appearance. Wait, are you even alive? More confused, you look through the window and you are kind of proud that you woke up early for once. It must be Kirill. """,
    "numbers":{"1": "dialogue_kitchen", "2": "dialogue_phone", "3": "dialogue_bathroom"},
    "time" : 0,
    "items": []
}

dialogue_kitchen = {
    "name": "Kitchen",
    "description":"You Go to the kitchen,  you need something to wake you up .  You bump into your housemate.  You have quick chat about what happened last night.  He tells you that you were studying at Jason’s flat and Denise called round in the morning to say she’s studying at the library.",
    "time":5,
    "numbers": {"1": "dialogue_breakfast", "2": "dialogue_coffee"},
    "items": []
}

dialogue_bathroom = {
    "name": "Bathrom",
    "description":"ERROR DIALOGUE_SHOWER IS MISSING! You smell and you definitely need a shower",
    "numbers": []#{"1":"dialogue_shower", "2":"dialogue_no_shower"},
    "items": []
}

dialogue_phone = {
    "name": "Reach for Phone",
    "description":"Reach your phone and start scrolling and You discover photos from the other night. Are those your study notes on the table at pre drinks?,Call Jason to find out what happened He tells you that you left your notes at pre drinks and they are still at his flat in Taly South. You feel exhausted but you need to get up.",
    "time": 10,
    "numbers": {"1": "dialogue_kitchen", "2": "dialogue_bathroom", "3":"dialogue_jason_flat_through"},
    "items": []
    
}

dialogue_jason_flat_through = {
    "name": "Bump Housemate",
    "description":"Throw on your clothes and leave to Jason’s flat. On your way out you bump into your housemate.You find out denise is at the library studying.",
    "time": 5,
    "numbers": {"1": "dailogue_jason", "2": "dialogue_library"},
    "items": []
}

dialogue_coffee = {
    "name": "Make Coffee",
    "description":"This wiil boost your energy",
    "time": 5,
    "numbers": {"1": "dialogue_bathroom", "2": "dialogue_jason", "3": "dialogue_library"},
    "items":[item_coffee]
}

dialogue_breakfast = {
    "name": "Make Breakfast",
    "description":"You find a Python book in the cereal box. What a coincidence.",
    "numbers": {"1": "take_book", "2": "leave_book"},
    "time": 15,
    "items":[item_textbook]
}

dialogue_jason = {
    "name": "Jason's Flat",
    "description" : "You go to Jsons flat and find there is no answr when you knock on the door",
    "numbers":{"1":"dialogue_wait", "2":"dialogue_library"},
    "time":20,
    "items": []
}

dialogue_wait = {
    "name": "Wait",
    "description" : "You wait and knock again after 5 minutes and the door is answered, you enter the house and see your notes",
    "numbers":{"1":"take_notes", "2":"dialogue_stay", "3":"dialogue_library"},
    "time":5,
    "items": [item_notes]
}

dialogue_stay = {
    "name": "Stay",
    "description" : "You wait and knock again after 5 minutes and the door is answered, you enter the house and see your notes",
    "numbers":{"1":"dialogue_exam"},
    "time":60,
    "items": []
}

dialogue_library = {
    "name":"Library",
    "description":"You meet Denise in the library and study for half an hour soon your stomach is rumbling and energy is low",
    "numbers":{"1":"dialogue_food", "2":"dialogue_no_food"},
    "items": []
}

dialogue_food = {
    "name":"Hallway",
    "description":"On your way from getting food yu notice a key on the floor",
    "numbers":{"1":"dialogue_investigate", "2":"dialogue_library"},
    "items": []
}


dialogue = {
    "dialogue_start": dialogue_start,
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
    "dialogue_food": dialogue_food
}
