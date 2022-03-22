import matplotlib.pyplot as plt
from random import randint, choice

# Play 100,000 games.
numGames = 100000
# Play the game with 3 doors.
allDoors = set(range(0, 3))

# Randomly assign the door with the car and the initial guess
# for each game played.
randDoor = [randint(0, 2) for _ in range(numGames)]
randGuess = [randint(0, 2) for _ in range(numGames)]

cmap = plt.get_cmap('magma')
low = cmap(0.5)
medium = cmap(0.25)
high = cmap(0.8)
colors = (low, medium, high)

# Plot the distribution of doors with the car and the initial 
# guesses. These are randomly distributed.
fig, axes = plt.subplots(1, 2)
N0, bins0, patches0 = axes[0].hist(randDoor, bins=[0, 1, 2, 3], rwidth=0.9)
N1, bins1, patches1 = axes[1].hist(randGuess, bins=[0, 1, 2, 3], rwidth=0.9)
axes[0].set_title('Door with car behind it -- randomly generated distribution')
axes[1].set_title('Initial guess -- randomly generated distribution')

for patch0, patch1, color in zip(patches0, patches1, colors):
    patch0.set_facecolor(color)
    patch1.set_facecolor(color)

correctGuesses = [randDoor[i] == randGuess[i] for i in range(numGames)].count(True)

print('Number of times the car was won when the "stay" strategy was employed:')
print(correctGuesses / numGames)

def playSwitchStrategy(i):
    # Eliminate one of the two doors that was not initially selected.
    openedDoor = choice(list(allDoors.difference([randDoor[i], randGuess[i]])))

    # Switch guess based on the previous guess and the eliminated door.
    newGuess = next(iter(allDoors.difference([openedDoor, randGuess[i]])))

    return randDoor[i] == newGuess

correctGuesses = [playSwitchStrategy(i) for i in range(numGames)].count(True)

print('Number of times the car was won when the "switch" strategy was employed:')
print(correctGuesses / numGames)

plt.show()
