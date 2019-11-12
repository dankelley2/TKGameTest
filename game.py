from tkinter import *
import game_colors as color
from player import Player


def animate():
    # focus goes on the canvas to make sure we're sending events to it, not the window
    canvas.focus_set()
    # root.after is not a recursive function. It provides an async timer and a callback function to re-run this function on the
    # main thread after 1/60th of a second
    root.after(33, animate)


# Creates a sprite object and assigns it to each player, then adds a player to the global dictionary
def add_actor(actor):
    actor.sprite = canvas.create_rectangle(actor.aabb.x, actor.aabb.y, actor.aabb.mx, actor.aabb.my, fill=actor.color)
    playerList[actor.name] = actor


# Grabs the keycode, then loops through our actors and checks whether or not we can move. The python way is to handle
#  exceptions and just move on. No harm done.
# The astrisk before the delta argument tells us that we want to unpack what might be a list into
#  a list of parameters e.g. (unpack [0,10] to dx=0, dy=10).
# The movement_dict property doesn't even come standard on the Actor object, it's just something we added dynamically.
#  yay python.
def move_actor(event):
    key = str(event.keysym)

    for p in playerList.values():
        try:
            delta = p.movement_dict[key]
            p.move(*delta)
            canvas.move(p.sprite, *delta)
        except:
            pass

# Creating these here as a test. keymaps and pixel movements
map1 = {
    'w':[0 ,-10],
    's':[0 , 10],
    'a':[-10, 0],
    'd':[ 10, 0]
}
map2 = {
    'Up'   :[0 ,-10],
    'Down' :[0 , 10],
    'Left' :[-10, 0],
    'Right':[ 10, 0]
}

# Our root Graphics object
# Canvas is basically a panel in .NET
root = Tk()
canvas = Canvas(root, width=400, height=400, bg=color.bg_drygrass)

# Create global Player List; add players
playerList = {}
add_actor(Player(10, 10, 10, 10, name="Dan", color="red"))
add_actor(Player(50, 50, 10, 10, name="Connor", color="blue"))

# Assign keys for movement
playerList["Dan"].movement_dict = map1
playerList["Connor"].movement_dict = map2

# These event keys are kind of difficult to find
canvas.bind('<Key>', move_actor)

# can't remember what this does, but I think it's just like "Control.Add()" in .Net
#root.config(cursor="none")
canvas.pack()

# start animation loop
animate()

# start GUI Thread loop
root.mainloop()