from items import *

dialogue_start = {
    "name": "Bedroom",
    "description":
    """You wake up and a long night of heavy drinking is catching up on you. Have you just dreamt about Kirill? Confused, you look for something to hold on to. Your stomach is rambling, and a massive headache has made its appearance. Wait, are you even alive? More confused, you look through the window and you are kind of proud that you woke up early for once. It must be Kirill. 
""",
    "numbers": {"1": dialogue_kitchen, "2": dialogue_phone, "3": dialogue_bathroom}
}

dialogue_kitchen = {
    "name": "Kitchen",
    "description":"You Go to the kitchen,  you need something to wake you up .  You bump into your housemate.  You have quick chat about what happened last night.  He tells you that you were studying at Jason’s flat and Denise called round in the morning to say she’s studying at the library.",
    "numbers": {"1": dialogue_breakfast, "2": dialogue_coffee}
}

dialogue_bathroom = {
    "name": "Bathrom",
    "description":"You smell and you definitely need a shower"
    "numbers": {"1": dialogue_shower, "2": dialogue_no_shower}
}

dialogue_shower = {
    "name": "Bathrom",
    "description":"You smell and you definitely need a shower"
    "numbers": {"1": dialogue_shower, "2": dialogue_no_shower}
}

dialogue_phone = {
    "name": "Reach for Phone",
    "description":"Reach your phone and start scrolling and You discover photos from the other night. Are those your study notes on the table at pre drinks?,Call Jason to find out what happened He tells you that you left your notes at pre drinks and they are still at his flat in Taly South. You feel exhausted but you need to get up.",
    "numbers": {"1": dialogue_kitchen, "2": dialogue_bathroom, "3":dialogue_jason_flat_through}
}

dialogue_jason_flat_through = {
    "name": "Bump Housemate",
    "description":"Throw on your clothes and leave to Jason’s flat. On your way out you bump into your housemate.You find out denise is at the library studying."
    "numbers": {"1": dailogue_jason, "2": dialogue_library}
}

dialogue_coffee = {
    "name": "Make Coffee",
    "description":"This wiil boost your energy",
    "numbers": {"1": dialogue_bathroom, "2": dialogue_jason, "3": dialogue_library}
}

dialogue_breakfast = {
    "name": "Make Breakfast",
    "description":"You find a Python book in the cereal box. What a coincidence.",
    "numbers": {"1": dialogue_take_book, "2": dialogue_leave_book}
}

dialogue_leave_book = {
    "name": "leave book",
    "description":"",
    "numbers": {"1": dialogue_bathroom, "2": dialogue_jason, "3": dialogue_library}
}

dialogue_leave_book = {
    "name": "leave book",
    "description":"",
    "numbers": {"1": dialogue_bathroom, "2": dialogue_jason, "3": dialogue_library}
}

dialogue = {
    "1": dialogue_start,
    #"2": dialogue_stretch,
    #"3": room_tutor,
    #"4": room_parking,
    #"5": room_office
}
