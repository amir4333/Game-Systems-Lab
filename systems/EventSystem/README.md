# Event System

This project is a reusable event system that I developed for learning game architecture and communication between different game systems.

## Why did I start this project?

Game systems should not always directly communicate with each other.
A good architecture allows different parts of a game to interact without creating strong dependencies.

The goal of this project is to understand how event-driven systems work and how they can be used to create flexible and scalable game systems.

## Goals

The goals of this project are:

1. Learning event-driven architecture deeply.
2. Creating a reusable event manager.
3. Allowing different systems to communicate without direct dependency.
4. Understanding the relationship between events, listeners, and publishers.
5. Using this system in future game projects.

## How it works

The Event System contains three main parts:

- Event:
  Represents an action or change that happened in the game.

- Event Manager:
  Manages events and sends them to interested listeners.

- Listener:
  A system that subscribes to specific events and reacts when they happen.

## Example

A player picks up an item:

Player
→ ItemPickedUp Event
→ Event Manager
→ Inventory / UI / Quest System

## Future Improvements

- [ ] Support event priority
- [ ] Add event history
- [ ] Add one-time listeners
- [ ] Improve event data handling