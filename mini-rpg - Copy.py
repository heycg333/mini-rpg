
import random
import sys
import time
import streamlit as st
import pandas as pd
import numpy as np


quests = {
    "The Hill Dwarves": "dwarves_intro",
    "Tomb of the Dragon Slayer": "slayer_intro",
    "Forest Rangers": "rangers_intro"
}


for key in ["q1", "q2", "quest"]:
    if key not in st.session_state:
        st.session_state[key] = ""


class Hero: #hero stats and combat methods
    def __init__(self, name, maxhp, hp, atk, atkmin, atkmax, defense, block, potion, sword, shield, armor, fireshield, slayersword, rangervolley, venom):
        self.name = name
        self.max_hp = maxhp
        self.hp = hp
        self.atk = atk
        self.atk_min = atkmin
        self.atk_max = atkmax
        self.defense = defense
        self.block = block
        self.potion = potion
        self.sword = sword
        self.shield = shield
        self.armor = armor
        self.fire_shield = fireshield
        self.slayer_sword = slayersword
        self.ranger_volley = rangervolley
        self.venom = venom
    
    def equipment_check(self):
        st.write(f"Inventory - {hero.sword}, {hero.shield}, {hero.armor}, {hero.potion} potion")      
     

class Monsters: #enemy stats and combat actions
    def __init__(self, hero, name, hp, atk, atkmin, atkmax, defense, poisoned, special, specdmg, specprep, specdesc):
        self.hero = hero
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atk_min_base = atkmin
        self.atk_max_base = atkmax
        self.defense = defense
        self.poisoned = poisoned
        self.special = special
        self.spec_dmg = specdmg
        self.spec_prep = specprep
        self.spec_desc = specdesc


        
if "hero" not in st.session_state:
    st.session_state.hero = Hero("", 20, 20, 1, 1, 3, 1, False, 3, "Shortsword", "Wood Shield", "No Armor", False, False, False, False)
hero = st.session_state.hero

if "wolf" not in st.session_state:
    st.session_state.wolf = Monsters(hero, "Wolf", 12, 2, 2, 4, 0, False, "none", 0, "", "")
wolf = st.session_state.wolf
if "roadbandit" not in st.session_state:
    st.session_state.roadbandit = Monsters(hero, "Bandit", 14, 3, 1, 3, 0, False, "none", 0, "", "")
roadbandit = st.session_state.roadbandit
if "durgrin" not in st.session_state:
    st.session_state.durgrin = Monsters(hero, "Durgrin", 14, 2, 2, 4, 0, False, "none", 0, "", "")
durgrin = st.session_state.durgrin
if "troll" not in st.session_state:
    st.session_state.troll = Monsters(hero, "Troll", 30, 2, 2, 5, 0, False, "RAMPAGE", 5, "is winding up for a devastating strike!", "roars and thrashes around wildly with his giant club")
troll = st.session_state.troll
if "goblin" not in st.session_state:
    st.session_state.goblin = Monsters(hero, "Goblin", 12, 3, 1, 4, 0, False, "none", 0, "", "")
goblin = st.session_state.goblin
if "orc" not in st.session_state:
    st.session_state.orc = Monsters(hero, "Orc", 13, 2, 2, 5, 0, False, "none", 0, "", "")
orc = st.session_state.orc
if "spider" not in st.session_state:
    st.session_state.spider = Monsters(hero, "Spider", 12, 3, 1, 3, 0, False, "none", 0, "", "")
spider = st.session_state.spider
if "forestbandit" not in st.session_state:
    st.session_state.forestbandit = Monsters(hero, "Forest Bandit", 12, 3, 2, 3, 0, False, "none", 0, "", "")
forestbandit = st.session_state.forestbandit
if "giantspider" not in st.session_state:
    st.session_state.giantspider = Monsters(hero, "Giant Spider", 30, 4, 2, 6, 0, False, "Fang Leap", 5, "rears back hissing, ready to pounce!", "launches itself at you, fangs glinting, legs outstretched")
giantspider = st.session_state.giantspider
if "dragon" not in st.session_state:
    st.session_state.dragon = Monsters(hero, "Dragon", 75, 4, 3, 6, 1, False, "Fire Breath", 12, "stands and its throat begins to glow orange!", "spews flames that engulf you")
dragon = st.session_state.dragon

def color_text(text, color_code): 
    return f"\033[{color_code}m{text}\033[0m"

def pause(text = "Continue"):
    st.button(text)

def gameover(hero):
    st.write(f"\nIt looks like {hero.name} won't be saving the village")
    st.write("GAME OVER")
    sys.exit()
    
def click_button():
    st.session_state.clicked = True

def radio_form(label, options, key, mapping=None):
    with st.form(f"{key}_form"):
        choice = st.radio(label, options)
        submit = st.form_submit_button("Confirm")
    if submit and choice:
        st.session_state[key] = mapping[choice] if mapping else choice
        return True
    return False



if "step" not in st.session_state:
    st.session_state.step = "intro"
step = st.session_state.step

if "clicked" not in st.session_state:
    st.session_state.clicked = False
    
clicked = st.session_state.clicked

# === GAME INTRODUCTION ===
if step == "intro":
    st.markdown("""
    <div style='text-align: center; padding: 1rem; background-color: #f5fff5; border: 10px solid green; border-radius: 20px;'>
        <h1 style='color: green; font-weight: bold;'>⚔️ Codédex Quest ⚔️</h1>
    </div>
    """, unsafe_allow_html=True)

    with st.form("name form"):
        name = st.text_input("What is your name?")
        submit = st.form_submit_button("Confirm")

    if submit and name:
        hero.name = name
        st.session_state.step = "story_begins"

elif step == "story_begins":
    st.write("## The Story Begins......")
    st.write("---")
    st.write(f"{hero.name} is from a small village nestled in the shadow of the snowy peaks of a looming mountain range")
    st.write("Recently a dragon has moved into the mountains and the village is in danger")
    st.write(f"{hero.name}'s father, the village guardian, has fallen in battle and the people need a new champion...")
    st.write("---")
    st.button("Continue", on_click=click_button)
    
    if st.session_state.clicked:
            st.session_state.step = "elder_knocks"

elif step == "elder_knocks":
    st.write("One morning you hear the Village Elder knocking on your door and calling your name")
    with st.form("q1_form"):
        st.radio("Do you answer the door?", ["Yes", "No"], key = "q1")
        submit = st.form_submit_button("Confirm")
    if submit:
        st.session_state.step = "elder_enters"

elif step == "elder_enters":
    if "q1" in st.session_state and st.session_state.q1 == "No":
        st.write(f"'{hero.name}, this is too important - I hope you're dressed, I'm coming in'")
        st.write("---")
    st.write("Village Elder enters and asks for your help. He describes several options to help protect the village from the dragon")
    st.write("---")
    st.write("  1- The dwarves in the nearby Copper Hills may be convinced to help defend us")
    st.write("---")
    st.write("  2- A legendary dragon slayer's tomb lies on the coast and contains his magic sword")
    st.write("---")
    st.write("  3- The rangers in the forest are masterful archers and could take down a dragon")
    st.write("---")
    st.write(f"'What say you, young {hero.name}, do you feel up to the task?'")
    with st.form("q2_form"):
        st.radio("Answer - ", ["Yes", "No"], key = "q2")
        submit = st.form_submit_button("Confirm")
    if submit:
        st.session_state.step = "elder_sendoff"

elif step == "elder_sendoff":
    if "q2" in st.session_state and st.session_state.q2 == "No":
        st.write(f"'Oh {hero.name}, and that's precisely why you are the right person'")
    st.write("---")

    with st.form("quest_form"):
        selected_quest = st.radio("Where will you go for aid?", list(quests.keys()))
        submit = st.form_submit_button("Confirm")
    if submit:
        if selected_quest:
            st.session_state.quest = selected_quest
            st.write(st.session_state.quest)
            st.session_state.step = "intro_rewards"
        else:
            st.warning("Please choose a quest before continuing")

elif step == "intro_rewards":
    st.write(st.session_state.quest)

    st.write("'A splendid choice, let's prepare you for your journey with some equipment'")
    st.write("(GAIN SHORTSWORD)")
    st.write("(GAIN SHIELD)")
    st.write("(GAIN 3 10hp HEAL POTIONS)")
    st.write("---")
    hero.equipment_check()
    

    if st.button("Begin Quest"):
        raw_quest = st.session_state.quest
        st.write("RAW quest value:", repr(raw_quest))

        quest_key = raw_quest.strip()
        next_step = quests.get(quest_key)

        if next_step:
            st.session_state.step = next_step
        else:
            st.write("Available quest keys:", list(quests.keys()))
            st.write("quest not found")


# === DWARVES QUEST ===
elif step == "dwarves_intro":
    st.write("The Dwarves live in the Copper Hills to the south.")
    dwarf_road = st.radio("You can either - ", [
        "Take the well-traveled mining trail road, following it south then cut east to the Copper Hills",
        "Take a riskier, more direct route and head southeast across the plains"
        ], key= "dwarf_road")
    if st.button("Confirm"):
        if "riskier" in dwarf_road:
            st.session_state.step = "combat"
        else:
            st.session_state.step = "combat"



    





