# Monty Hall Simulation

This simulation plays the Monty Hall game 100,000 times.

## Background

A car is hidden behind 1 of 3 doors. The game begins with the player choosing one of the doors. Monty then eliminates one of the other two doors and gives the player the option of staying with their first guess or switching to the one remaining door. If the player correctly chooses the door, they win the car.

## Simulation Setup

Each game, the door with the car behind it and the player's initial guess are randomly chosen. Results are averaged over 100,000 games.

## Analysis

### Employing the "stay" strategy.

Since there's an equal chance for the car to be behind any of the three doors, if you stick with your initial choice for both rounds, you'll win the car just one out of every three games.

### Employing the "switch" strategy.

Say your initial guess is Door 1. After Monty eliminates either Door 2 or Door 3, you switch to the other remaining option. The car is behind Door 1 just 1/3 of the time, but the car is behind either Door 2 or Door 3 2/3 of the time. By switching your guess between rounds, you'll win two out of every three games.

## Summary

Since Monty can only eliminate a door without the car behind it, you have more information at the beginning of round 2 than you did before round 1. With fewer opportunities to be wrong, reevaluating your decision after the door elimination proves to be the winning strategy a higher percentage of the time.
