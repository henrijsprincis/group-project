from items import *

dialogue_start = {
    "name": "Bedroom",
    "description":
    """You wake up and a long night of heavy drinking is catching up on you. Have you just dreamt about Kirill? Confused, you look for something to hold on to. Your stomach is rambling, and a massive headache has made its appearance. Wait, are you even alive? More confused, you look through the window and you are kind of proud that you woke up early for once. It must be Kirill. """,
    "numbers":{"1": "dialogue_kitchen", "2": "dialogue_phone", "3": "dialogue_bathroom"},
    "items": []
}

dialogue_kitchen = {
    "name": "Kitchen",
    "description":"You Go to the kitchen,  you need something to wake you up .  You bump into your housemate.  You have quick chat about what happened last night.  He tells you that you were studying at Jason’s flat and Denise called round in the morning to say she’s studying at the library.",
    "numbers": {"1": "dialogue_breakfast", "2": "dialogue_coffee"}
}

dialogue_bathroom = {
    "name": "Bathrom",
    "description":"You smell and you definitely need a shower",
    "numbers": {"1":"dialogue_shower", "2":"dialogue_no_shower"}
}

dialogue_shower = {
    "name": "Bathrom",
    "description":"You smell and you definitely need a shower",
    "numbers": {"1": "dialogue_shower", "2": "dialogue_no_shower"}
}


dialogue = {
    "dialogue_start": dialogue_start,
    "dialogue_kitchen": dialogue_kitchen,
    "dialogue_bathroom": dialogue_bathroom,
    "dialogue_shower": dialogue_shower,
}
