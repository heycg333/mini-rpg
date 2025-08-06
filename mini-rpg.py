import base64
import random
import sys
import time
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np


# with open("battle_music.mp3", "rb") as audio_file:
#     st.audio(audio_file.read(), format="audio/mp3")


# audio_file = open('battle_music.mp3', 'rb')
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format='audio/mp3')

# def play_music(track_path):
#     with open(track_path, "rb") as audio_file:
#         st.audio(audio_file.read(), format="audio/mp3")

# def music_player():
#     step = st.session_state.step
#     soundtrack = {
#         "intro": "village-background.mp3",
#         "combat_hero": "combat_loop.mp3",
#         "combat_monster": "combat_loop.mp3",
#         "combat_victory": "combat_loop.mp3",
#         "final_boss": "final_dragon.mp3",
#         "dwarves_intro": "dwarves_entry.mp3",
#         "dwarves_throne": "dwarves_throne.mp3",
#         "tomb_puzzle": "tomb_puzzle.mp3",
#         "slayer_sword_room": "slayer_sword_room.mp3",
#         "forest_maze": "forest_maze.mp3",
#         "ranger_village": "ranger_village.mp3",
#     }
#     if step in soundtrack:
#         st.audio(f"music/{soundtrack[step]}", loop= True)



# === BUILD IMAGE FUNCTION LIKE THIS vvv TO PULL IMAGE FOR SCENES ===
# === ADD 

def scene_image():
    step = st.session_state.step
    image_list = {
        "intro": "images/title.png",
        "story_begins": "images/village.webp", 
        "dwarves_intro": "images/mountains.webp",
        "elder_enters": "images/elder.webp",
        "combat_victory": "images/victory.png",
        "enter_dwarf_gate": "images/dwarf-city.jpg",
        "to_throneroom": "images/dwarf-city.jpg",
        "dwarf_throneroom": "images/thane.webp",
        "dwarf_rewards2": "images/dwarf-rewards.webp",
        "thane_plead": "images/thane-standing.webp",
        "dwarf_bonus_quest": "images/thane-standing.webp",
        "game_over": "images/game-over.webp", 
        "slayer_intro": "images/road-to-slayer-tomb.webp",
        "tomb_arrival": "images/tomb-entrance.webp",
        "tomb_entrance": "images/tomb-main-chamber-4-shield.webp",
        "tomb_door_intro": "images/tomb-main-chamber-4-shield.webp",
        "tomb_door_open": "images/slayer-burial-chamber.webp",
        "trial_of_names": "images/trial-of-names.webp",
        "w_room_explore": "images/trial-of-names.webp"

    }

    if step in image_list:
        st.image(image_list[step], caption=None, use_container_width=True)


def combat_image():
    monster = st.session_state.monster.name
    image_list = {
        "Wolf": "images/wolf.webp",
        "Road Bandit": "images/road-bandit.webp",
        "Durgrin": "images/durgrin.webp",
        "Troll": "images/troll.webp",
        "Goblin": "images/goblin.webp"
    }

    if monster in image_list:
        st.image(image_list[monster], caption=None, use_container_width=True)
    

def scene_music():
    step = st.session_state.step
    track_map = {
        "intro": "music/village-background.mp3",
        "story_begins": "music/village-background.mp3",
        "elder_knocks": "music/village-background.mp3",
        "elder_enters": "music/village-background.mp3",
        "elder_sendoff": "music/village-background.mp3",    
        "intro_rewards": "music/village-background.mp3",
        "combat_hero": "music/combat.mp3",
        "hero_action": "music/combat.mp3",
        "combat_monster": "music/combat.mp3",
        "combat_victory": "music/victory.mp3",
        "final_boss": "music/final_dragon.mp3",
        "dwarves_intro": "music/dwarven-entrance.mp3",
        "dwarf_road_combat": "music/combat.mp3",
        "dwarf_gate": "music/dwarven-entrance.mp3",
        "dwarf_gate2": "music/dwarven-entrance.mp3",
        "enter_dwarf_gate": "music/dwarven-entrance.mp3",
        "to_throneroom": "music/dwarven-entrance.mp3",
        "throneroom_floor": "music/throneroom.mp3",
        "dwarf_throneroom": "music/throneroom.mp3",
        "dwarf_throneroom2": "music/throneroom.mp3",
        "dwarf_throneroom3": "music/throneroom.mp3",
        "dwarf_throneroom4": "music/throneroom.mp3",
        "convince_thane": "music/throneroom.mp3",
        "thane_decision": "music/throneroom.mp3",
        "thane_plead": "music/throneroom.mp3",
        "thane_plead_result": "music/throneroom.mp3",
        "dwarf_bonus_quest": "music/throneroom.mp3",
        "troll_intro": "music/mines.mp3",
        "dwarf_rewards": "music/throneroom.mp3",
        "sleep": "music/sleeping.mp3",
        "wake_up":"music/sleeping.mp3",
        "dwarf_rewards2": "music/quest-victory.mp3",
        "tomb_puzzle": "music/tomb_puzzle.mp3",
        "slayer_sword_room": "music/slayer_sword_room.mp3",
        "forest_maze": "music/forest_maze.mp3",
        "ranger_village": "music/ranger_village.mp3",
        "final battle prep": "music/final-battle-prep.mp3",
        "game_over": "music/game-over.mp3", 
        "slayer_intro": "music/slayer-tomb-intro.mp3",
        "slayer_road_combat": "music/slayer-tomb-intro.mp3",
        "tomb_arrival": "music/slayer-tomb-intro.mp3",
        "tomb_entrance": "music/slayer-tomb.mp3",
        "tomb_door_intro": "music/slayer-tomb.mp3",
        "tomb_explore": "music/slayer-tomb.mp3",
        "tomb_door": "music/slayer-tomb.mp3",
        "puzzle_trigger": "music/slayer-tomb.mp3",
        "trial_of_names": "music/slayer-tomb.mp3",
        "w_room_explore": "music/slayer-tomb.mp3",
        "w_room_plates": "music/slayer-tomb.mp3",
        "w_room_incorrect_choice": "music/slayer-tomb.mp3",
        "w_room_correct_choice": "music/slayer-tomb.mp3",
        "w_room_statue": "music/slayer-tomb.mp3",
        "w_room_banner": "music/slayer-tomb.mp3",
        "w_room_table": "music/slayer-tomb.mp3",
        "puzzle_trigger": "music/slayer-tomb.mp3",
        "puzzle_trigger": "music/slayer-tomb.mp3",
        "puzzle_trigger": "music/slayer-tomb.mp3",
        "puzzle_trigger": "music/slayer-tomb.mp3",
        "puzzle_trigger": "music/slayer-tomb.mp3",
        "puzzle_trigger": "music/slayer-tomb.mp3",
        "puzzle_trigger": "music/slayer-tomb.mp3",
        "puzzle_trigger": "music/slayer-tomb.mp3",
        "puzzle_trigger": "music/slayer-tomb.mp3",

    }

    audio = AudioManager()

    if step in track_map:
        #custom_music_player(track_map[step])
        col1, col2 = st.columns([5, 1])
        with col2: #moves to right edge
            #custom_music_player(track_map[step])
            audio.play(track_map[step])
    else:
        audio.stop()


#use if you want to control html placement, but still limited in st iframe
def custom_music_player(file_path: str, autoplay=True, loop=True):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()

    auto = "autoplay" if autoplay else ""
    looping = "loop" if loop else ""

    # Inline audio player using markdown
    st.markdown(
        f"""
        <audio controls {auto} {looping} style="
            width: 180px;
            height: 28px;
            margin-top: 0.5rem;
            margin-bottom: 0.5rem;
        ">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )


# def scene_music():
#     step = st.session_state.step
#     soundtrack = {
#         "intro": "village-background.mp3",
#         "story_begins": "village-background.mp3",
#         "elder_knocks": "village-background.mp3",
#         "combat_hero": "combat_loop.mp3",
#         "combat_monster": "combat_loop.mp3",
#         "combat_victory": "combat_loop.mp3",
#         "final_boss": "final_dragon.mp3",
#         "dwarves_intro": "dwarves_entry.mp3",
#         "dwarves_throne": "dwarves_throne.mp3",
#         "tomb_puzzle": "tomb_puzzle.mp3",
#         "slayer_sword_room": "slayer_sword_room.mp3",
#         "forest_maze": "forest_maze.mp3",
#         "ranger_village": "ranger_village.mp3",
#     }

#     if "current_music" not in st.session_state:
#         st.session_state.current_music = ""
        
#     if step in soundtrack:
#         new_track = soundtrack[step]
#         if st.session_state.current_music != new_track:
#             autoplay_music(f"music/{new_track}")
#             st.session_state.current_music = new_track


# def autoplay_music(file_path):
#     with open(file_path, "rb") as f:
#         data = f.read()
#     b64 = base64.b64encode(data).decode()
#     audio_tag = f"""
#         <audio autoplay hidden>
#             <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
#         </audio>
#     """
#     components.html(audio_tag, height=0)


#         ✅ Use st.audio("file.mp3") (i.e. in scene_music()) when:
# Your audio files are in your project folder

# You're referencing tracks by filename

# You want simplicity and automatic browser handling

# ✅ Use play_music(path) only if:
# You need to read the file in binary mode for dynamic control

# You want to serve an audio object rather than a path

# You’re building something like a custom audio manager


# if step == "combat_hero":
#     play_music("music/battle_theme.mp3")
# if step == "silent_cutscene":
#     st.audio("")  # no-op, will remove player if it was part of previous step






quests = {
    "The Hill Dwarves": "dwarves_intro",
    "Tomb of the Dragon Slayer": "slayer_intro",
    "Forest Rangers": "rangers_intro"
}



equipment = {
    "Shortsword": [1, 1, 3],
    "Longsword": [3, 1, 3],

}

battle_options = ["⚔️  Attack", "🛡️  Block", "💗 Heal Potion"]


for key in ["q1", "q2", "quest"]:
    if key not in st.session_state:
        st.session_state[key] = ""

class AudioManager:
    def __init__(self):
        if "current_track" not in st.session_state:
            st.session_state.current_track = None

    def play(self, track_path: str):
        # Only reload if track is different
        if st.session_state.current_track != track_path:
            st.session_state.current_track = track_path
            st.audio(track_path, loop=True, autoplay= True)
        else:
            # Always re-render to keep browser playback going
            st.audio(st.session_state.current_track, loop=True, autoplay=True)

    def stop(self):
        st.session_state.current_track = None


class SoundEffectManager:
    def __init__(self):
        self.sfx_map = {
            "sword": "sfx/sword-slice.mp3",
            "potion": "sfx/potion.mp3",
            "death": "sfx/enemy_death.mp3",
            "block": "sfx/block.mp3",
            "gameover": "sfx/gameover.mp3",
            "knock": "sfx/knocking.mp3", 
            "door": "sfx/open-door.mp3",
            "gate": "sfx/dwarf-gate.mp3",
            "troll": "sfx/troll.mp3",
            "troll_special": "sfx/troll-special.mp3",
            "low_monster_roar": "sfx/low-monster-roar.mp3",
            "monster_attack": "sfx/monster-attack.mp3",
            "monster_roar": "sfx/monster-roar.mp3",
            "you_chose_poorly": "sfx/you-chose-poorly.mp3"

        }

    def play(self, effect_name: str):
        if effect_name not in self.sfx_map:
            st.warning(f"SFX '{effect_name}' not found")
            return

        file_path = self.sfx_map[effect_name]
        with open(file_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        audio_tag = f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        components.html(audio_tag, height=0)

# example in combat logic
# sfx = SoundEffectManager()

# # After player attacks
# hero.std_atk(monster)
# sfx.play("attack")

# # When potion is used
# hero.heal_potion()
# sfx.play("potion")

# # On enemy defeat
# if monster.hp <= 0:
#     sfx.play("death")


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


    def std_atk(self, monster): #standard attack with 1/20 chance for crit/miss
        st.write(f"{self.name} attacks!")
        d20 = random.randint(1,20)
        rng = (random.randint(self.atk_min,self.atk_max))
        dmg = (self.atk + rng)
        if d20 == 20:
            st.write("**********************")
            st.write("⚔️  CRITICAL HIT!  ⚔️")
            st.write("**********************")
            dmg *= 2  
        elif d20 == 1:
            st.write(f"{self.name} Missed!")
            st.session_state.step = "combat_monster"
            return

        if self.block: #blocking adds 2 dmg to next attack
            dmg += 2
            self.block = False
        
        monster.take_dmg(dmg)
        

    def block_atk(self): #sets block attribute to add atk dmg and reduce next incoming dmg
        st.write(f"{self.name} conserves energy, raises shield, and braces for impact")
        self.block = True
    
    def heal_potion(self): #heals 10 up to max hp
        self.hp = min(self.hp + 10, self.max_hp)
        if self.hp == self.max_hp:
            st.write(f"{self.name} is fully healed")
        else:
            st.write(f"{self.name} heals 10 hp")
        st.write(f"{self.name} has {self.hp} hp")
        self.potion -= 1

    def take_dmg(self, dmg): #applies monster attack dmg
        st.write(f"{hero.name} takes {dmg} damage")
        self.hp -= dmg
        if self.hp <= 0:
            st.write("💀💀💀💀💀💀💀💀")
            st.write(f"{self.name} has perished")
            st.write("💀💀💀💀💀💀💀💀")
            gameover(hero)
        else:
            st.write(f"{self.name} has {self.hp} hp left")


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

    @property
    def atk_min(self):
        return max(self.atk_min_base, hero.defense)
        
    @property
    def atk_max(self):
        return max(self.atk_max_base, hero.defense + 2)


    # === COMBAT LOOP - MONSTER ACTION ===
    def m_std_atk(self, hero):  
        st.write(f"{self.name} attacks!")
        d20 = random.randint(1,20)
        rng = (random.randint(self.atk_min, self.atk_max))
        dmg = max(0, self.atk - hero.defense + rng)
        if d20 == 20:
            st.write("**********************")
            st.write("⚔️  CRITICAL HIT!  ⚔️")
            st.write("**********************")
            dmg *= 2 
        elif d20 == 1:
            st.write(f"{self.name} Missed!")
            return
        
        if hero.block: #checks for block, halves dmg (rounded down)
            dmg //= 2
        
        hero.take_dmg(dmg)

    def m_special_prep(self, hero): #every 3rd round skip attack to prep special attack
        sfx = SoundEffectManager()
        st.write("⚠️-------------------------------------------------------------------------⚠️")
        st.write(f"Watch out {hero.name}, the {self.name} {self.spec_prep}")
        st.write("⚠️-------------------------------------------------------------------------⚠️")

    def m_special_atk(self, hero): #special attack every 4th round
        st.markdown("<h2 style='text-align:center;'>💀------------------⚔️</h2>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align:center;'>{self.special}</h1>", unsafe_allow_html=True)
        # st.header(f"        {self.special}        ")

        st.markdown("<h2 style='text-align:center;'>💀------------------⚔️</h2>", unsafe_allow_html=True)
        st.write(f"The {self.name} {self.spec_desc}")
        rng = (random.randint(self.atk_min,self.atk_max))
        dmg = max(0, self.spec_dmg - hero.defense + rng)
        if hero.fire_shield and hero.block:
            dmg = 0
        elif hero.block:
            dmg //= 2

        hero.take_dmg(dmg)

    def take_dmg(self, dmg): #applies dmg from hero attack
        st.write(f"{self.name} takes {dmg} damage")
        self.hp -= dmg
        if self.hp <= 0:
            st.write("🎉🎉🎉🎉🎉🎉")
            st.write(f"{hero.name} defeated {self.name}")
            st.divider()
            hero.hp = hero.max_hp
        else:
            st.write(f"{self.name} has {self.hp} hp left")

    def take_poison_dmg(self):
        dmg = random.randint(1, 3)
        st.write(f"☠️ {self.name} takes {dmg} poison damage ☠️")
        self.hp -= dmg

        
if "hero" not in st.session_state:
    st.session_state.hero = Hero("Hero", 20, 20, 1, 1, 3, 1, False, 3, "Shortsword", "Wood Shield", "No Armor", False, False, False, False)
hero = st.session_state.hero

if "wolf" not in st.session_state:
    st.session_state.wolf = Monsters(hero, "Wolf", 12, 2, 2, 4, 0, False, "none", 0, "", "")
wolf = st.session_state.wolf
if "roadbandit" not in st.session_state:
    st.session_state.roadbandit = Monsters(hero, "Road Bandit", 14, 3, 1, 3, 0, False, "none", 0, "", "")
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


def pause(text = "Continue"):
    st.button(text)

def gameover(hero):
    st.write(f"Is this the end of {hero.name}?")
    button("Continue", next_step="game_over")


def sleep_animation():
    sleep_lines = ["zzzz..", "zzzz......", "zzzz..........", "zzz...", "*snoooore*", "zz...", "z..."]
    placeholder = st.empty()

    for line in sleep_lines:
        placeholder.write(line)
        time.sleep(1)

    placeholder.empty()  # Clear the text after it's done (optional)

    
def click_button():
    st.session_state.clicked = True

def input_form(label, text_input, next_step):
    with st.form(label):
        name = st.text_input(text_input)
        submit = st.form_submit_button("Confirm")
    if submit and name:
        hero.name = name
        st.session_state.step = next_step
        st.rerun()

    

def radio_form(label, options, key, next_step=None, mapping=None):
    with st.form(f"{key}_form"):
        choice = st.radio(label, options)
        submit = st.form_submit_button("Confirm")
    if submit and choice:
        st.session_state[key] = choice
        step = mapping[choice] if mapping else next_step
        if step:
                st.session_state.step = step
        st.rerun()
    #     return True
    # return False

def combat_radio(label, options, key, next_step, mapping=None):
    with st.form(f"{key}_form"):
        choice = st.radio(label, options)
        submit = st.form_submit_button("Confirm")
    if submit and choice:
        st.session_state[key] = mapping[choice] if mapping else choice
        st.session_state.step = next_step
        return True
    return False
    

def button(label, next_step = None, extra_state: dict = None, key= None):
    if st.button(label, key=key or label): # use custom key or default to label
        if next_step:
            st.session_state.step = next_step
        if extra_state:
            for k, v in extra_state.items():
                st.session_state[k] = v
        # st.audio("music/village-background.mp3", format="audio/mpeg", loop= True, autoplay=True)
        st.rerun()

def combat_button(label, extra_state: dict = None):
    if st.button(label):
        if extra_state:
            for k, v in extra_state.items():
                st.session_state[k] = v
        return True
    return False

def dragon_drops():
    frames = [
        "          🐉   ", 
        "         🐉    ", 
        "        🐉     ", 
        "     🐉🔥      ", 
        "   🐉🔥🔥       ",
        " 💥🔥🔥🔥🔥💥     ",
    ]

    for i in frames:
        st.write(i)
        time.sleep(0.3)




if "step" not in st.session_state:
    st.session_state.step = "tomb_entrance"  #"intro"
step = st.session_state.step

scene_music()

if "clicked" not in st.session_state:
    st.session_state.clicked = False
    
clicked = st.session_state.clicked



# st.markdown(
#     """
#     <audio controls autoplay loop>
#         <source src="music/village-background.mp3" type="audio/mp3">
#     </audio>
#     """,
#     unsafe_allow_html=True
# )


# === COMBAT ===
if step == "combat_hero":
    monster = st.session_state.monster
    hero = st.session_state.hero

    st.write(f"Round {st.session_state.combat_round}")
    st.write(f"{hero.name}: {hero.hp} HP")
    st.write(f"{monster.name}: {monster.hp} HP")

    if "player_action_complete" not in st.session_state:
        st.session_state.player_action_complete = False
    if "monster_action_complete" not in st.session_state:
        st.session_state.monster_action_complete = False

    st.session_state.got_rewards = False

    # if not st.session_state.player_action_complete:    
    radio_form("Battle Options - ", battle_options, key = "hero_action", next_step="hero_action")
    combat_image()


elif step == "hero_action":
    monster = st.session_state.monster
    hero = st.session_state.hero
    sfx = SoundEffectManager()

    if not st.session_state.player_action_complete:
        action = st.session_state.hero_action
        if action == battle_options[2] and hero.potion == 0:
            st.write(f"Oh no! {hero.name} is out of potions")
            button("Choose another action", next_step="combat_hero", extra_state={"player_action_complete": False})

        else:    
            st.session_state.player_action_complete = True

            if action == battle_options[0]:
                hero.std_atk(monster)
                sfx.play("sword")
            elif action == battle_options[1]:
                hero.block_atk()                
            elif action == battle_options[2]:
                hero.heal_potion()
                sfx.play("potion")

    if st.session_state.player_action_complete:

        if monster.hp <= 0:
            button("Continue", next_step="combat_victory", extra_state={"player_action_complete": False})
        else:
            button("Continue", next_step="combat_monster", extra_state={"player_action_complete": False})


#copy of combat
    # if not st.session_state.player_action_complete:    
    #     if combat_radio("Battle Options - ", battle_options, key = "hero_action", next_step=None):
    #         action = st.session_state.hero_action
    #         st.session_state.player_action_complete = True
    #         if action == battle_options[0]:
    #             hero.std_atk(monster)
    #             if combat_button("Continue"):
    #                 st.session_state.player_action_complete = False
    #                 if monster.hp <= 0:
    #                     st.session_state.step = "combat_victory"
    #                 else:
    #                     st.session_state.step = "combat_monster"

    #         elif action == battle_options[1]:
    #             hero.block_atk()
    #         elif action == battle_options[2]:
    #             hero.heal_potion()

    # else:
    #     if button("Continue"):
    #         st.session_state.player_action_complete = False
    #         if monster.hp <= 0:
    #             st.session_state.step = "combat_victory"
    #         else:
    #             st.session_state.step = "combat_monster"



    # action = st.radio("Battle Options -", battle_options, key= "hero_action")

    # if st.button("Confirm Action"):
    #     if action == battle_options[0]:
    #         hero.std_atk(monster)
    #     elif action == battle_options[1]:
    #         hero.block_atk()
    #     elif action == battle_options[2]:
    #         hero.heal_potion()

    #     if monster.hp <= 0:
    #         st.session_state.step = "combat_victory"
    #     else:
    #         st.session_state.step = "combat_monster"



elif step == "combat_monster":
    monster = st.session_state.monster
    hero = st.session_state.hero
    round = st.session_state.combat_round
    sfx = SoundEffectManager()

    if not st.session_state.monster_action_complete:
        st.session_state.monster_action_complete = True
        if monster.special != "none" and round > 2 and (round + 1) % 4 == 0: #prep special attack before every 4th round
            monster.m_special_prep(hero)
            if monster.name == "Troll":
                sfx.play("low_monster_roar")

        elif monster.special != "none" and round % 4 == 0: #special attack every 4th round
            monster.m_special_atk(hero)
            if monster.name == "Troll":
                sfx.play("troll_special")

        else:
            monster.m_std_atk(hero)
            if monster.name == "Troll":
                sfx.play("monster_attack")
            else:
                sfx.play("block")
        st.session_state.player_action_complete = False
        st.session_state.combat_round += 1

    if st.session_state.monster_action_complete:
        button("Continue", next_step="combat_hero", extra_state={"monster_action_complete": False})

elif step == "combat_victory":
    scene_image()
    st.write("Victory!")
    monster = st.session_state.monster
    quest = st.session_state.quest

    if not st.session_state.got_rewards:
        if monster == roadbandit:
            st.write("GAIN LONGSWORD")
            st.write("GAIN 1 10HP HEAL POTION")
            hero.sword = "Longsword"
            hero.potion += 1
            hero.atk = equipment["Longsword"][0]
            hero.equipment_check()

        elif monster == goblin and quest == "slayer_intro":
            st.write("Among the hoard of goblin trash you notice a shield with solid metal plating circling the rim")
            st.write("GAIN REINFORCED SHIELD")
            hero.shield = "Reinforced Shield"
            hero.defense += 1
            hero.equipment_check()



        st.session_state.got_rewards = True
    
    button("Rest, heal, and continue", st.session_state.next_step)
    

# === GAME INTRODUCTION ===
elif step == "intro":
    # if step in ["intro", "story_begins", "elder_knocks"]:
    #     autoplay_music("music/village-background.mp3")
    # scene_music()
    # music_player()
    col1, col2 = st.columns([1.8, 1])
    with col2:
        st.write("PRESS PLAY TO BEGIN ⬆️ ")
    scene_image()

    # st.markdown("""
    # <div style='text-align: center; padding: 1rem; background-color: #f5fff5; border: 10px solid green; border-radius: 20px;'>
    #     <h1 style='color: green; font-weight: bold;'>⚔️ Codédex Quest ⚔️</h1>
    # </div>
    # """, unsafe_allow_html=True)

    input_form("name_form", "What is your name?", next_step= "story_begins")
    # st.audio("music/village-background.mp3", format="audio/mpeg", loop= True, autoplay=True)
    

elif step == "story_begins":

    st.write("## The Story Begins......")
    scene_image()
    st.write(f"{hero.name} is from a small village nestled in the shadow of the snowy peaks of a looming mountain range")
    st.write("Recently a dragon has moved into the mountains and the village is in danger")
    st.write(f"{hero.name}'s father, the village guardian, has fallen in battle and the people need a new champion...")
    st.divider()

    button("Continue", next_step="elder_knocks")

    # if st.session_state.clicked == False and button("Continue"):
    #     click_button()
    #     st.session_state.step = "elder_knocks"
    #     st.session_state.clicked = False
    # else:
    #     st.session_state.step = "elder_knocks"



elif step == "elder_knocks":
    sfx = SoundEffectManager()
    st.write("One morning you hear the Village Elder knocking on your door and calling your name")
    radio_form("Do you answer the door?", ["Yes", "No"], key= "q1", next_step="elder_enters")
    sfx.play("knock")

        # st.session_state.step = "elder_enters"
        # click_button()
        # st.session_state.clicked = False
        # st.write(step)
        # st.write(st.session_state.q1)

    # else:
    #     st.session_state.step = "elder_enters"

    
elif step == "elder_enters":
    sfx = SoundEffectManager()

    scene_image()
    if st.session_state.q1 == "No":
        st.write(f"'{hero.name}, this is too important - I hope you're dressed, I'm coming in'")
        st.divider()
    st.write("Village Elder enters and asks for your help. He describes several options to help protect the village from the dragon")
    st.divider()
    st.write("  1- The dwarves in the nearby Copper Hills may be convinced to help defend us")
    st.write("  2- A legendary dragon slayer's tomb lies on the coast and contains his magic sword")
    st.write("  3- The rangers in the forest are masterful archers and could take down a dragon")
    st.divider()
    st.write(f"'What say you, young {hero.name}, do you feel up to the task?'")

    radio_form("Answer - ", ["Yes", "No"], key = "q2", next_step="elder_sendoff")
    sfx.play("door")

    #     click_button()
    #     st.session_state.step = "elder_sendoff"
    #     st.session_state.clicked = False
    # else:
    #     st.session_state.step = "elder_sendoff"

elif step == "elder_sendoff":
    if "q2" in st.session_state and st.session_state.q2 == "No":
        st.write(f"'Oh {hero.name}, and that's precisely why you are the right person'")
    st.divider()

    radio_form("Where will you go for aid?", list(quests.keys()), key = "quest", next_step="intro_rewards", mapping = quests)
    #     click_button()
    #     st.session_state.step = "intro_rewards"
    #     st.session_state.clicked = False
    # else:
    #     st.session_state.step = "intro_rewards"

elif step == "intro_rewards":
    st.write("'A splendid choice, let's prepare you for your journey with some equipment'")
    st.write("(GAIN SHORTSWORD)")
    st.write("(GAIN SHIELD)")
    st.write("(GAIN 3 10hp HEAL POTIONS)")
    st.divider()
    hero.equipment_check()
    
    button("Begin Quest", next_step= st.session_state.quest)
    # if st.session_state.clicked == False and button("Begin Quest", next_step= st.session_state.quest):
    #     click_button()
    #     st.session_state.step = st.session_state.quest
    #     st.session_state.clicked = False
    # else:
    #     st.session_state.step = st.session_state.quest

# === DWARVES QUEST ===
elif step == "dwarves_intro":
    st.write("The Dwarves live in the Copper Hills to the south.")
    scene_image()
    radio_form("You can either - ", [
    "Take the well-traveled mining trail road, following it south then cut east to the Copper Hills",
    "Take a riskier, more direct route and head southeast across the plains"
    ], key= "dwarf_road", next_step="dwarf_road_combat")

elif step == "dwarf_road_combat":
    if "dwarf_road" in st.session_state and "riskier" in st.session_state.dwarf_road:
        st.write("You come across a bandit camp and 2 charge you. Get ready to fight!")
        st.session_state.monster = st.session_state.roadbandit
    else:
        st.write("Along the road you encounter an angry wolf. Get ready to fight!")
        st.session_state.monster = st.session_state.wolf

    if "combat_round" not in st.session_state:
            st.session_state.combat_round = 1
    
    button("Begin Combat", next_step="combat_hero", extra_state={"next_step": "dwarf_gate"})

elif step == "dwarf_gate":
    st.write("You arrive at the gates of the dwarven stronghold built into the rock face of the Copper Hills")
    st.write("A guard shouts down 'State your business here!'")
    radio_form("You shout back - ", [
        "I need to speak to your chief. My village needs help defending from the dragon",
        "I've heard the hill dwarves make the best ale - I have my doubts so I'm here to put that to the test"
    ], key= "dwarf_q1", next_step="dwarf_gate2")

elif step == "dwarf_gate2":
    sfx = SoundEffectManager()
    if "ale" in st.session_state.dwarf_q1:
        st.write("The guard scowls. 'There is NONE better! Durgrin! Open the gates and show this fool to the tavern.'")
        sfx.play("gate")
        button("Continue", next_step= "enter_dwarf_gate")
    else:
        st.write("The guard laughs. 'You are not fit to address the Thane. Durgrin, go teach this whelp a lesson.'")
        st.write("The gate opens and a burly dwarf approaches, cracking his knuckles. Get ready to fight!")
        st.session_state.monster = st.session_state.durgrin
        st.session_state.combat_round = 1
    
        button("Begin Combat", next_step="combat_hero", extra_state={"next_step": "enter_dwarf_gate"})

# === ENTER DWARVEN STRONGHOLD ===

elif step == "enter_dwarf_gate":
    if "monster" in st.session_state and st.session_state.monster == st.session_state.durgrin:
        st.write("Durgrin dusts himself off, laughing as you help him up")
        st.write("'I underestimated you, follow me friend, I could use a drink'")
    scene_image()
    st.write("Durgrin leads you through the gate into a long stone corridor sloping downwards. Glowing lanterns flicker above, casting shadows along the carved stone")
    st.write("You pass through an archway and emerge into a large open marketplace. The clinking of hammer on anvil echoes all around, a backdrop to gruff voices haggling at each vendor cart")
    st.write("Suddenly a group of heavily armored dwarves marches up and orders you to halt. 'Thaneguard - on your best behavior now' Durgrin whispers")
    st.write("'By order of Thane Brogdin, you are to come with us, outsider'")
    st.divider()
    st.session_state.dwarf_q2_dmg = False
    radio_form("You respond - ", [
        "1 - Ok, lead the way",
        "2 - I demand to know where you're taking me",
        "3 - Sure, but after I get some ale"
    ], key= "dwarf_q2", next_step="to_throneroom")

elif step == "to_throneroom":
    sfx = SoundEffectManager()
    if "1" in st.session_state.dwarf_q2:
        st.write("Durgrin nods, 'Wise choice'.")
        st.write(" You follow the guards past the marketplace to a towering set of bronze doors.")
        st.write("Inside, the throne room stretches upward into a dome with intricate ornamental etchings spiraling up the stone")
        button("Continue", next_step="dwarf_throneroom")
    else:
        sfx.play("block")
        st.write("'Insolent whelp! We'll teach you manners!' You're struck in the head and knocked unconscious")
        if not st.session_state.dwarf_q2_dmg:
            st.session_state.dwarf_q2_dmg = True
            hero.take_dmg(5)
        button("Continue", next_step="throneroom_floor")

elif step == "throneroom_floor":
    st.write("You awaken on the floor of a large room stretching upward into a dome.")
    st.write("Rubbing your head you look around and realize you're in the throne room")
    button("Continue", next_step="dwarf_throneroom")


# === DWARVEN THRONEROOM ===

elif step == "dwarf_throneroom":
    scene_image()
    st.write("Thane Brogdin's throne sits on a raised dais, carved from a single slab of granite with copper runes twisting up the armrests")
    st.write("The Thane watches you with deep-set eyes, his face expressionless and unreadable.")
    st.write("You feel a chill - his stare is every bit as cold as the polished stone surrounding him")
    button("Continue", next_step= "dwarf_throneroom2")

elif step == "dwarf_throneroom2":
    st.write("His advisor Ori, an older dwarf with a beard like braided chainmail, breaks the silence first -")
    st.write("'It was only a matter of time before the humans came seeking shelter. Those who choose to live under the sky will always be at the mercy of what falls from it'")
    radio_form("You respond - ", [
        "1 - Better the open sky than a hole in the ground",
        "2 - It's true, we seek protection and aid from the brave and mighty dwarves of the Copper Hills", 
        "3 - Say nothing. Let the Thane speak first"
    ], key= "dwarf_q3", next_step="dwarf_throneroom3")

elif step == "dwarf_throneroom3":
    if "1" in st.session_state.dwarf_q3:
        st.write("The advisor's nostrils flare and his eyes shoot daggers. He raises an arm, taking a deep breath and readying a verbal lashing")
        st.write("Thane Brogdin's booming laughter interrupts. 'This one has some courage, settle yourself Ori, we shall hear out our visitor'")
        st.image("images/thane-laughing.webp", caption=None, use_container_width=True)
    elif "2" in st.session_state.dwarf_q3:
        st.write("'Sniveling worm, do not insult us with your attempts to barter with flattery' Ori snarls")
        st.write("The Thane eyes you with thinly-veiled disdain")
    else:
        st.write("You hold your tongue and look to the Thane")

    button("Continue", next_step="dwarf_throneroom4")

elif step == "dwarf_throneroom4":
    st.divider()
    st.write("Thane Brogdin raises a gauntleted fist, instantly silencing the room")
    st.divider()
    st.write("'You come here seeking dwarven steel to protect your people, bringing great risk to mine'")
    st.write("'Why should we face your dragon? Why should dwarven blood pay for your salvation?'")
    st.write("")
    radio_form("How will you convince the Thane - ", [
        "1 - It is the right thing to do",
        "2 - If we fall, the dragon will come for your great halls next",
        "3 - We will share whatever treasure the dragon has hoarded",
        "4 - You'll earn glory that will echo through stone forever'"
    ], key="dwarf_q4", next_step="convince_thane")

elif step == "convince_thane":
    if "1" in st.session_state.dwarf_q4:
        st.write("'Noble, yet naive. The only right thing to do is what's best for my people'")
    elif "2" in st.session_state.dwarf_q4:
        st.write("'A fair warning, mayhap a true one")
    else:
        st.write("You see a flash in the Thane's eyes - you have clearly piqued his interest")
        st.image("images/thane-happy.webp", caption=None, use_container_width=True)

    button("Continue", next_step="thane_decision")

elif step == "thane_decision":
    if "1" in st.session_state.dwarf_q4 and "2" in st.session_state.dwarf_q3:
        st.write("'We'll not bleed for humans who run to us only when their roof catches fire. You'll find no allies here'")
        st.session_state.dwarf_quest_success = False
        st.session_state.step = "return_home"
    elif "2" or "4" in st.session_state.dwarf_q4 and "2" in st.session_state.dwarf_q3:
        st.write("'You come seeking aid with naught but words for compensation. I grow tired'")
        st.session_state.step = "thane_plead"
    elif "3" or "4" in st.session_state.dwarf_q4 and "2" not in st.session_state.dwarf_q3:
        st.session_state.dwarf_quest_success = True
        st.session_state.step ="dwarf_rewards"
    else:
        st.session_state.dwarf_bonus_quest = True
        st.session_state.step = "dwarf_bonus_quest"

    button("Continue")



elif step == "thane_plead":
    st.write("Thane Brogdin stands and turns to leave.")
    radio_form("Do you -", [
        "1 - Plead for aid, at the risk of angering the Thane",
        "2 - Quietly leave"
    ], key="dwarf_q5", next_step="thane_plead_result")
    scene_image()


elif step == "thane_plead_result":
    if "1" in st.session_state.dwarf_q5:
        st.write("You push the matter, pleading for your village one last time")
        st.write("The Thane pauses. With his back turned, you cannot read his face, but nods his head, seemingly in consideration")
        st.session_state.dwarf_bonus_quest = True
        st.session_state.step = "dwarf_bonus_quest"
    else:
        st.session_state.dwarf_quest_success = False
        st.session_state.step = "return home"
    
    button("Continue")

elif step == "dwarf_bonus_quest":
    st.write("'I remain unconvinced, but I shall give you opportunity to prove your worth'")
    st.write("'A troll has attacked our miners and must be dealt with. Do so, and you may yet deserve dwarven steel'")
    st.write("'Ori, send an escort to take our guest into the mines. We shall see how strong they are'")
    button("Venture into the mine", next_step="troll_intro")
    scene_image()


elif step == "troll_intro":
    sfx = SoundEffectManager()

    sfx.play("troll")
    st.write("As you descend deeper into the mines, a foul, rotting musk assaults your nostrils")
    st.write("Something shuffles ahead. A growl echoes from the shadows, low, guttural, and hungry")
    st.write("A hulking figure lurches into view, dragging a massive club that could crush a clydesdale")
    st.write("Gray skin slick with cave slime parts to reveal jagged teeth bared in a twisted grin")
    st.divider()
    st.write("You've found the troll........")
    st.write("and it looks hungry")
    st.session_state.monster = st.session_state.troll
    st.session_state.combat_round = 1

    button("Begin Combat", next_step="combat_hero", extra_state={"next_step": "dwarf_rewards"})


elif step == "dwarf_rewards":
    if "monster" in st.session_state and st.session_state.monster == st.session_state.troll:
        st.write("You return to the throne room covered in troll blood")

    st.image("images/thane-happy.webp", caption=None, use_container_width=True)
    st.write("Thane Brogdin nods approvingly. 'I can see now there is strength in you, mayhap enough to face the challenge ahead'")
    st.write("'You may have the courage to face dragon fire, but you lack the equipment. Easily remedied.'")
    st.write(f"'Ori, prepare a room for our guest. Go and rest {hero.name}, we shall speak more tomorrow'")
    
    button("Retire to your room", next_step= "sleep")
           
elif step == "sleep":
    if "slept" not in st.session_state:
        st.session_state.slept = False

    if not st.session_state.slept:
        sleep_animation()
        st.session_state.slept = True
    button("Wake up", next_step = "dwarf_rewards2")

elif step == "wake_up":
    button("Wake Up", next_step="dwarf_rewards2")

elif step == "dwarf_rewards2":
    st.divider()
    st.write("In the morning, you are summoned back to the throne room")
    st.write("Thane Brogdin welcomes you and presents you with the finest dwarven mail you have ever seen")
    st.write("'My smiths worked through the night. This armor is light enough for your kind, strong enough to turn a dragon's fang'")
    st.write("Another smith steps forward and presents you with a dark shield, its surface shimmers in the firelight")
    st.write("'And this, the Emberguard. Quenched in molten obsidian, cooled in troll-blooded oil. No fire will blister your skin while this guard is raised'")
    st.write("(GAIN DWARVEN MAIL ARMOR)")  
    st.write("(GAIN EMBERGUARD SHIELD)")  
    st.write("(GAIN 2 10hp HEAL POTIONS)")  
    hero.armor = "Dwarven Mail"
    hero.shield = "Emberguard Shield"
    hero.potion += 2
    hero.defense += 4
    hero.fire_shield = True
    hero.equipment_check()
    st.divider()
    st.write("'Take these gifts, may they serve you well in the battle ahead. I send with you a regiment to help defend your village.'")
    st.write(f"'May the Stonefather guide your sword and shield your back. Farewell {hero.name}'")
    hero.hp = hero.max_hp

# === SLAYER QUEST ===

elif step == "slayer_intro":
    st.write("The tomb lies on the coast to the west.")
    scene_image()
    radio_form("You can either - ",[
        "1- Take the well-traveled merchant road, following it north from the village and west to the coast", 
        "2- Take a riskier, more direct route and travel an old pilgrim trail west through the hills"
        ], key="slayer_road", next_step="slayer_road_combat")

elif step == "slayer_road_combat":
    if "slayer_road" in st.session_state and "riskier" in st.session_state.slayer_road:
        st.write("As you ascend the winding trail goblins leap out of hiding, weapons raised. Get ready to fight!")
        st.session_state.monster = st.session_state.goblin
    else:
        st.write("Along the road you encounter an angry wolf. Get ready to fight!")
        st.session_state.monster = st.session_state.wolf

    if "combat_round" not in st.session_state:
            st.session_state.combat_round = 1
    
    button("Begin Combat", next_step="combat_hero", extra_state={"next_step": "tomb_arrival"})

elif step == "tomb_arrival":
    scene_image()
    st.write("Carved into a cliff overlooking the sea, the tomb's entrance yawns like the mouth of a forgotten god")
    st.write("Weathered statues of armored warriors flank the stairs, their swords pointed downward in eternal vigil")

    button("Continue", next_step="tomb_entrance")


elif step == "tomb_entrance":
    st.session_state.door_puzzle = ["🛡️", "🛡️", "🛡️", "🛡️"]
    scene_image()
    st.write("Inside, the air is dry and cold. The stone walls bear faded murals")
    st.write("The scenes depict a lone warrior slaying beasts, rallying soldiers, and, at last, falling beneath a dragon’s shadow.")
    st.write("You step into a wide, circular chamber. The air here is still and cold, untouched by time")
    st.write("Directly ahead stands a massive stone door etched with patterns that gleam faintly under your torchlight")
    button("Continue", next_step="tomb_door_intro")

elif step == "tomb_door_intro":
    scene_image()
    st.write("Embedded into the face of the door are four round, bronze-like discs displaying shield symbols")
    st.write("Flanking the door on both sides are 4 short hallways leading to other rooms, each labeled with some kind of trial")
    
    button("Continue", next_step="tomb_explore")

elif step == "tomb_explore":

    tomb_explore_options = {
    "1 - Examine door": "tomb_door",
    "2 - Trial of Names - west passage": "trial_of_names",
    "3 - Trial of Light - northwest passage": "trial_of_light",
    "4 - Trial of Balance - northeast passage": "trial_of_balance",
    "5 - Trial of Sound - east passage": "trial_of_sound",
    }

    if "🛡️" not in st.session_state.door_puzzle:
        button("Enter the burial chamber", next_step= "tomb_door_open")
    else:
        radio_form("Choose - ", list(tomb_explore_options.keys()), key = "tomb_explore_choice", next_step= None, mapping = tomb_explore_options)




elif step == "tomb_door":  
    st.write("The shield symbols glow faintly with pale blue runes. You try to rotate the discs but they won't budge")
    st.write("Around the outer ring of each disc, you notice faint carvings: not just shields... but swords as well")
    st.write("Seems as if they’re meant to turn and reveal a second form")
    st.write("Below the door, a short inscription reads:")
    st.write("'When swords replace shields, the slayer shall rise again'")
    st.write(" ".join(st.session_state.door_puzzle))

    button("Step back", next_step="tomb_explore")
    

elif step == "puzzle_trigger":
    st.write("In the distance, you hear stone grinding — deep and resonant. You rush back to the burial chamber entrace")
    st.write("One of the shield symbols turns with a heavy click, and a sword now gleams where a shield once stood")
    st.write(" ".join(st.session_state.door_puzzle))
    button("Continue", next_step= "tomb_explore")

# === TRIAL OF NAMES WEST ===
elif step == "trial_of_names":
    scene_image()
    st.write("Entering the room you are confronted with an imposing mural of a warrior standing atop a fallen dragon")
    st.write("He lifts his glowing sword to the sky in celebration of this great victory")
    st.write("Below the mural on the floor are 4 pressure plates, each with a name written on them")
    st.write("On another wall there is a faded banner next to a cracked statue of a knight")
    st.write("A small table has what looks like a balanced stone scale")

    button("Continue", next_step="w_room_explore")

elif step == "w_room_explore":
    w_room_explore_options = {
        "1 - Inspect the named plates": "w_room_plates",
        "2 - Inspect statue": "w_room_statue",
        "3 - Inspect faded banner": "w_room_banner",
        "4 - Inspect small table": "w_room_table",
        "5 - Leave room": "tomb_explore"
    }
    radio_form("Choose - ", list(w_room_explore_options.keys()), key = "w_room_explore_choice", next_step= None, mapping = w_room_explore_options)

        
elif step == "w_room_plates":

    w_room_plates_options = {
        "1 - step on Kellumn Ironhand": "w_room_incorrect_choice",
        "2 - step on Ser Bryn of the Vale": "w_room_incorrect_choice",
        "3 - step on Kael the Nameless": "w_room_correct_choice",
        "4 - step on Durek Flameborn": "w_room_incorrect_choice",
        "5 - back away": "w_room_explore"
    }
    st.write("In the center of the plates an inscription reads 'Honor the Dragon Slayer'")
    radio_form("Choose - ", list(w_room_plates_options.keys()), key = "w_room_plates_choice", next_step= None, mapping = w_room_plates_options)
    st.write("WARNING - incorrect selections have consequence")

elif step == "w_room_incorrect_choice":
    sfx = SoundEffectManager()
    st.write("🩸" * 15)
    st.write("A flash of pain rushes up your leg as small spikes drive into your foot")
    st.write("A voice whispers - 'You chose poorly'")
    hero.take_dmg(5)
    sfx.play("you-chose-poorly")

    button("Continue", next_step= "w_room_plates")
    
elif step == "w_room_correct_choice":
    st.write("The plate makes a satisfying click as it falls into place and the name begins to glow")
    button("Continue", next_step= "puzzle_trigger")

elif step == "w_room_statue":
    st.write("The inscription reads - ")
    st.write("He walked alone where fire fell,")
    st.write("No crown, no kin, no tale to tell.")
    st.write("No banners waved, no crowds adored —")
    st.write("Yet still, the beast fell to his sword.")

    button("Continue", next_step= "w_room_explore")


elif step == "w_room_banner":
    st.write("Depicts three knights, all bearing house sigils. One figure stands apart — weapon drawn, no sigil on his cloak")
    
    button("Continue", next_step= "w_room_explore")

elif step == "w_room_table":
    st.write("A stone scale, perfectly level. Etched on the base it reads - ")
    st.write("Blade and bone, equal in death. Wood tips the balance")        

    button("Continue", next_step= "w_room_explore")

# === TRIAL OF LIGHT NORTHWEST ===
elif step == "trial_of_names":
    print("This chamber has 4 pillars, each with a stone sconce facing the center of the room")
    print("In the center a pedestal instructs - 'Light returns in rhythm'")
    print("The back wall displays a mural of warriors battling a dragon")
    print("A ceremonial torchstand sits in front")

    button("Continue", next_step= "nw_room_explore")


elif step == "nw_room_explore":

    nw_room_explore_options = {
    "1 - Inspect the pillars": "nw_room_pillars",
    "2 - Inspect mural": "nw_room_mural",
    "3 - Inspect torchstand": "nw_room_torchstand",
    "4 - Leave room": "tomb_explore"
}

    radio_form("Choose - ", list(nw_room_explore_options.keys()), key = "nw_room_explore_choice", next_step= None, mapping = nw_room_explore_options)

elif step == "nw_room_table":
    st.write("A stone scale, perfectly level. Etched on the base it reads - ")
    st.write("Blade and bone, equal in death. Wood tips the balance")        

    button("Continue", next_step= "w_room_explore")


















elif step == "ne_room_explore":

    ne_room_explore_options = {
        "1 - Inspect the scale": "ne_room_scale",
        "2 - Inspect urn": "ne_room_urn",
        "3 - Inspect remains": "ne_room_remains",
        "4 - Inspect walls": "ne_room_walls",
        "5 - Leave room": "tomb_explore"
    }

    radio_form("Choose - ", list(ne_room_explore_options.keys()), key = "ne_room_explore_choice", next_step= None, mapping = ne_room_explore_options)


elif step == "e_room_explore":

    e_room_explore_options = {
        "1 - Inspect the chimes": "e_room_chimes",
        "2 - Inspect arrow": "e_room_arrow",
        "3 - Inspect murals": "e_room_murals",
        "4 - Inspect painting": "e_room_painting",
        "5 - Leave room": "tomb_explore"
    }
    radio_form("Choose - ", list(e_room_explore_options.keys()), key = "e_room_explore_choice", next_step= None, mapping = e_room_explore_options)


elif step == "tomb_door_open":
    st.write("The stone doors grind open and your skin begins to tingle")
    st.write("Inside lies a massive stone sarcophagus, draped in faded crimson cloth and topped with floral wreaths")
    st.write("At its base, a sword rests — blade gleaming with a faint inner light that grows as you approach")
    st.write("A faint voice whispers - 'It senses your need and has awakened.'")
    pause("press Enter to pick up the sword")
    st.write("The blade thrums in your hands, seeming eager to be put to use")
    st.write("'Quench its thirst for dragon's blood, and then return it here to its slumber'")
    st.write("You nod your nead in silent agreement and exit the tomb, eager to feed your new companion")

    hero.slayer_sword = True
    st.write("GAIN SLAYER SWORD")
    hero.sword = "Slayer Sword"
    hero.atk += 4
    hero.atk_min += 1
    hero.atk_max += 2
    hero.equipment_check()
    hero.hp = hero.max_hp


elif step == "return_home":
    st.write("return home")

elif step == "game_over":
    scene_image()

    sys.exit()
