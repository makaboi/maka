"""An expanded Lord of the Rings choose-your-own-adventure game."""


def get_choice(options):
    """Prompt the user until they pick one of the given options."""
    while True:
        choice = input("Enter choice: ").strip()
        if choice in options:
            return choice
        print(f"Please choose one of: {', '.join(sorted(options))}")


def game_over(message: str) -> None:
    """Print the failure message and end the game."""
    print(message)
    print("Game over.")


def victory() -> None:
    """Print the victory message and end the game."""
    print("Peace returns to Middle-earth.")
    print("You win!")


def scene1():
    print("Scene 1 – The Shire")
    print("You've just received the One Ring. Gandalf has urged you to leave the Shire.")
    print("1. Gather allies before departing")
    print("2. Slip away quietly under cover of night")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("You invite Sam, Merry, and Pippin to accompany you.\n")
    else:
        print("You decide to travel alone toward Bree.\n")
    scene2()


def scene2():
    print("Scene 2 – On the Road")
    print("You're travelling east when a dark shape flies overhead—the Nazgûl search for you.")
    print("1. Hide in the underbrush and let them pass")
    print("2. Dash across open fields to make quicker progress")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("The Nazgûl pass without seeing you.\n")
    else:
        print("The Nazgûl spot you but you reach Bree just ahead of them.\n")
    scene3()


def scene3():
    print("Scene 3 – Bree")
    print("In Bree you find an inn. A mysterious Ranger offers to guide you.")
    print("1. Accept the Ranger's help (he says his name is Strider)")
    print("2. Refuse and continue on your own")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("Strider leads you across the wild and eventually to Rivendell.\n")
    else:
        print("You set out alone. The Nazgûl nearly capture you, but you stumble into Rivendell half-frozen.\n")
    scene4()


def scene4():
    print("Scene 4 – Rivendell")
    print("At the council, the fate of the Ring is decided: it must be destroyed in Mount Doom.")
    print("A fellowship forms—if you choose to join, you'll be the Ring-bearer.")
    print("1. Accept the role and go with the fellowship")
    print("2. Decline and hand the Ring to someone else")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("You join the fellowship and set out south.\n")
        scene5()
    else:
        game_over("Another takes up the Ring. Its corrupting influence dooms Middle-earth.")


def scene5():
    print("Scene 5 – The Misty Mountains")
    print("The fellowship debates how to cross the mountains.")
    print("1. Attempt the snowy pass of Caradhras")
    print("2. Enter the Mines of Moria")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("A fierce storm drives you back. You are forced to take the road through Moria.\n")
    else:
        print("You choose the dark of Moria.\n")
    scene6()


def scene6():
    print("Scene 6 – Moria")
    print("In the depths of Moria a Balrog appears on the Bridge of Khazad-dûm.")
    print("1. Stand with Gandalf against the Balrog")
    print("2. Flee while Gandalf holds the bridge")
    choice = get_choice({"1", "2"})
    if choice == "1":
        game_over("The Balrog drags you into the abyss alongside Gandalf.")
    else:
        print("You escape as Gandalf falls into shadow.\n")
        scene7()


def scene7():
    print("Scene 7 – Lothlórien")
    print("The Lady Galadriel offers boats and counsel for the road ahead.")
    print("1. Take the boats down the Anduin")
    print("2. Travel overland through the wild hills")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("The river carries you swiftly south.\n")
        scene8()
    else:
        game_over("Orcs ambush you in the hills; without the river you are overwhelmed.")


def scene8():
    print("Scene 8 – Amon Hen")
    print("The fellowship breaks under attack. Frodo slips away.")
    print("1. Follow Frodo and Sam toward Mordor")
    print("2. Stay to defend Boromir")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("You and Sam chase after Frodo, vowing to see the quest through.\n")
        scene9()
    else:
        game_over("Boromir falls and the Ring passes beyond your reach.")


def scene9():
    print("Scene 9 – Emyn Muil")
    print("Lost among the maze-like rocks, you encounter the creature Gollum.")
    print("1. Spare him and take him as a guide")
    print("2. Drive him away")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("Gollum leads you toward the Dead Marshes.\n")
        scene10()
    else:
        game_over("Without a guide you wander until orcs capture you.")


def scene10():
    print("Scene 10 – The Dead Marshes")
    print("Gollum urges you to follow his narrow path through the cursed wetlands.")
    print("1. Trust Gollum and follow exactly")
    print("2. Light your own way and choose the route yourself")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("You avoid the treacherous lights and reach the far side safely.\n")
        scene11()
    else:
        game_over("The dead faces in the water lure you in; you never surface.")


def scene11():
    print("Scene 11 – Ithilien")
    print("Men of Gondor led by Faramir capture you, suspicious of your quest.")
    print("1. Speak honestly of your mission")
    print("2. Keep the Ring a secret and attempt escape")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("Faramir releases you with supplies and counsel.\n")
        scene12()
    else:
        game_over("Your escape fails and you are delivered to Sauron's forces.")


def scene12():
    print("Scene 12 – The Black Gate")
    print("You stand before the Black Gate of Mordor.")
    print("1. Attempt to sneak through the main gate")
    print("2. Take Gollum's secret stair into the mountains")
    choice = get_choice({"1", "2"})
    if choice == "1":
        game_over("The Eye of Sauron sees you and the Ring is lost.")
    else:
        print("You climb the perilous stairs toward Cirith Ungol.\n")
        scene13()


def scene13():
    print("Scene 13 – Shelob's Lair")
    print("A monstrous spider blocks your path in the darkness.")
    print("1. Fight Shelob with sword and strength")
    print("2. Use the Phial of Galadriel to drive her back")
    choice = get_choice({"1", "2"})
    if choice == "1":
        game_over("Shelob's venom overcomes you in the dark.")
    else:
        print("The light blinds Shelob and you escape into Mordor.\n")
        scene14()


def scene14():
    print("Scene 14 – The Plains of Gorgoroth")
    print("Exhausted, you trudge across Mordor as the armies march to war.")
    print("1. Disguise yourselves in orc-gear and march with a company")
    print("2. Traverse the ash fields under cover of darkness")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("The ruse works; you break away near Mount Doom.\n")
        scene15()
    else:
        game_over("Orc patrols discover you sneaking through the ash dunes.")


def scene15():
    print("Scene 15 – Mount Doom")
    print("After countless hardships you reach the fiery heart of Mordor.")
    print("1. Cast the Ring into the fire")
    print("2. Claim the Ring for yourself")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("You cast the Ring into the fire. Mount Doom erupts around you.\n")
        scene16()
    else:
        game_over("The Ring enslaves you; Sauron triumphs.")


def scene16():
    print("Scene 16 – The Crumbling Mountain")
    print("Mount Doom shakes violently as lava bursts around you.")
    print("1. Search for Sam amid the smoke")
    print("2. Run for safety alone")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("You find Sam and together seek a way out.\n")
        scene17()
    else:
        game_over("Without Sam you lose your footing and perish in the fire.")


def scene17():
    print("Scene 17 – The Fiery Slope")
    print("The ground quakes as you scramble down the mountainside.")
    print("1. Cling to a rock and wait for the tremors to subside")
    print("2. Dash down the unstable path")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("The shaking lessens and you continue carefully.\n")
        scene18()
    else:
        game_over("The path collapses beneath you and the lava consumes all.")


def scene18():
    print("Scene 18 – The Ash Plain")
    print("Exhausted, you reach a plain of ash and ruin.")
    print("1. Wait on a rocky island for rescue")
    print("2. Attempt to trek across the molten ground")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("You and Sam collapse, hoping for salvation.\n")
        scene19()
    else:
        game_over("The heat overwhelms you as you sink into the ash.")


def scene19():
    print("Scene 19 – The Eagles")
    print("Great eagles wheel in the sky above the desolation.")
    print("1. Raise your hand to signal them")
    print("2. Ignore them and crawl onward")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("The eagles swoop down and lift you from the ruin.\n")
        scene20()
    else:
        game_over("You collapse alone and the darkness takes you.")


def scene20():
    print("Scene 20 – Healing in Ithilien")
    print("You awaken in soft beds beneath the trees of Ithilien.")
    print("1. Rest and recover your strength")
    print("2. Attempt to slip away toward home immediately")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("The healing arts of the elves restore you.\n")
        scene21()
    else:
        game_over("Still weak, you collapse before leaving the camp.")


def scene21():
    print("Scene 21 – The Field of Cormallen")
    print("A great celebration honors the destruction of the Ring.")
    print("1. Join the rejoicing of friends and kings")
    print("2. Stay apart from the festivities")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("Songs are sung of your deeds.\n")
        scene22()
    else:
        game_over("Your absence breeds suspicion and you are shunned.")


def scene22():
    print("Scene 22 – Road to Minas Tirith")
    print("The journey to the White City begins.")
    print("1. Travel with the king's escort")
    print("2. Strike off on your own ahead of the group")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("The road is safe and swift.\n")
        scene23()
    else:
        game_over("Alone on the road you fall prey to lingering foes.")


def scene23():
    print("Scene 23 – Gates of Minas Tirith")
    print("The restored city shines before you.")
    print("1. Enter the city in honor")
    print("2. Decline entry and remain outside")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("Crowds cheer as you pass through the gates.\n")
        scene24()
    else:
        game_over("Refusing the honor, you are taken for a spy and jailed.")


def scene24():
    print("Scene 24 – The Coronation")
    print("Aragorn is to be crowned King of Gondor.")
    print("1. Attend the coronation ceremony")
    print("2. Skip the ceremony to rest")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("You witness the return of the king.\n")
        scene25()
    else:
        game_over("Offending the new king, you are sent away in disgrace.")


def scene25():
    print("Scene 25 – Farewell to the Fellowship")
    print("Your companions prepare to part ways.")
    print("1. Bid farewell and begin the journey home")
    print("2. Refuse to leave the city")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("With tears and laughter you set out.\n")
        scene26()
    else:
        game_over("You linger too long and your purpose fades into legend.")


def scene26():
    print("Scene 26 – Through Rohan")
    print("On the road north you pass through the fields of Rohan.")
    print("1. Rest in Edoras for the night")
    print("2. Travel without rest to save time")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("Hospitality renews your strength.\n")
        scene27()
    else:
        game_over("Exhaustion overcomes you on the empty road.")


def scene27():
    print("Scene 27 – Into Fangorn")
    print("The ancient forest of Fangorn looms ahead.")
    print("1. Visit Treebeard and seek guidance")
    print("2. Skirt the forest and hurry on")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("Treebeard blesses your journey.\n")
        scene28()
    else:
        game_over("Lost in the tangled woods, you vanish without trace.")


def scene28():
    print("Scene 28 – Return to Rivendell")
    print("You arrive once more at the house of Elrond.")
    print("1. Speak with Bilbo and rest")
    print("2. Hurry past without stopping")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("Bilbo's tales hearten you for the final leg.\n")
        scene29()
    else:
        game_over("Weariness overcomes you in the wilds beyond Rivendell.")


def scene29():
    print("Scene 29 – Crossing the Misty Mountains")
    print("The mountains must be crossed once more.")
    print("1. Take the safer High Pass")
    print("2. Attempt the Mines of Moria again")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("Though cold, the pass is clear.\n")
        scene30()
    else:
        game_over("Moria's darkness claims you a second time.")


def scene30():
    print("Scene 30 – Bree Again")
    print("The familiar inn of the Prancing Pony awaits.")
    print("1. Spend the night and share your tales")
    print("2. Refuse to stop and press on")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("Old friends provide comfort and supplies.\n")
        scene31()
    else:
        game_over("Without rest, you fall ill on the lonely road.")


def scene31():
    print("Scene 31 – The Shire's Border")
    print("You reach the borders of your homeland.")
    print("1. Scout the gate quietly before entering")
    print("2. March in openly")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("You see ruffians controlling the land and plan your move.\n")
        scene32()
    else:
        game_over("Ruffians seize you before you can warn anyone.")


def scene32():
    print("Scene 32 – Raising the Shire")
    print("The Shire is under the thumb of invaders.")
    print("1. Rally the hobbits to resist")
    print("2. Confront the ruffians alone")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("The hobbits prepare for battle.\n")
        scene33()
    else:
        game_over("Outnumbered, you are thrown into the Lockholes.")


def scene33():
    print("Scene 33 – Battle of Bywater")
    print("The final fight for the Shire begins.")
    print("1. Lead the charge against the ruffians")
    print("2. Hold back and let others fight")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("Victory is yours and the Shire is freed.\n")
        scene34()
    else:
        game_over("Without your leadership the revolt fails.")


def scene34():
    print("Scene 34 – Rebuilding the Shire")
    print("Peace returns but much has been damaged.")
    print("1. Plant Galadriel's gift to heal the land")
    print("2. Do nothing and leave the fields barren")
    choice = get_choice({"1", "2"})
    if choice == "1":
        print("A mallorn tree blossoms and hope is renewed.\n")
        scene35()
    else:
        game_over("Without care the Shire withers in sorrow.")


def scene35():
    print("Scene 35 – The Grey Havens")
    print("Years later you are drawn to the sea and the ships of the elves.")
    print("1. Sail into the West with the elves")
    print("2. Remain in Middle-earth")
    choice = get_choice({"1", "2"})
    if choice == "1":
        victory()
    else:
        game_over("The wounds of the past never heal and you fade into obscurity.")


if __name__ == "__main__":
    scene1()

