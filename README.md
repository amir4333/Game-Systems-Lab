# Game Systems Lab

A personal collection of reusable game systems and mechanics developed from scratch with Python.

The goal of this project is not to build a single game. Instead, I am building independent and reusable systems that can be understood, improved, tested, and eventually used as building blocks in different game projects.

---

## Goals

* Build reusable game systems and mechanics from scratch.
* Understand how game systems work internally.
* Practice software architecture and object-oriented design.
* Keep systems independent from specific game content whenever possible.
* Improve systems through iteration and real usage.
* Validate systems by combining them in small playable or interactive demos.
* Build a personal library of game-development systems for future projects.

---

## Why did I start this project?

I wanted to go beyond simply making games.

Instead of learning game development only by building complete games, I wanted to understand the systems that exist behind them: how inventory works, how quests are managed, how dialogue flows, how different systems communicate, and how these parts can be combined without creating unnecessary dependencies.

This project is my laboratory for exploring those ideas.

The systems themselves are the main product of the project, while mini-games and demos are used to validate how well those systems work together.

---

## Current Systems

| System           | Status        |
| ---------------- | ------------- |
| Inventory System | ✅ V1 Complete |
| Event System     | ✅ V1 Complete |
| Dialogue System  | ✅ V1 Complete |
| Quest System     | ✅ V1 Complete |

---

## Current Integration

The first integration demo combines the four current systems into a small gameplay scenario.

The current flow demonstrates how different systems can communicate without being directly dependent on each other:

```text
Player
  │
  ▼
Dialogue System
  │
  │ START_QUEST
  ▼
Event System
  │
  ▼
Quest System
  │
  │
  ▼
Exploration
  │
  │ EXPLORE_ENDED
  ▼
Event System
  ├──────────────► Inventory System
  │
  └──────────────► Quest System
```

This demonstrates the current event-driven communication between the systems.

---

## Project Structure

```text
Game-Systems-Lab/
│
├── systems/
│   ├── InventorySystem/
│   ├── EventSystem/
│   ├── DialogueSystem/
│   └── QuestSystem/
│
├── demos/
│   └── MiniGame/
│
└── README.md
```

The `systems/` directory contains the reusable core systems.

The `demos/` directory contains examples and small projects that use these systems together.

---

## Systems

### Inventory System

Responsible for storing and managing items.

Current concepts include:

* Items
* Inventory slots
* Adding items
* Removing items
* Item lookup
* Basic item stacking properties

---

### Event System

Provides event-driven communication between different parts of the game.

Current functionality includes:

* Event subscription
* Event unsubscription
* Event emission
* Listener-based communication

The system is currently used as a communication layer between other systems in the integration demo.

---

### Dialogue System

A node-based dialogue system for creating branching conversations.

Current functionality includes:

* Dialogue nodes
* Dialogue choices
* Branching dialogue
* Current dialogue state
* Choice selection
* Dialogue completion detection
* Choice actions
* Console-based testing

---

### Quest System

A reusable system for managing quests and objectives.

Current functionality includes:

* Quest creation
* Quest objectives
* Objective progress
* Multiple objectives
* Quest completion detection
* Active quests
* Completed quests

The Quest System is also integrated with the Event System in the current demo.

---

## Project Philosophy

The project follows a few core principles:

### Reusable

Systems should be useful beyond a single game or scenario.

### Independent

Core systems should avoid unnecessary dependencies on specific game content or presentation layers.

### Understandable

The implementation should remain understandable enough that I can explain why the system works the way it does.

### Extensible

Systems should have a structure that allows future features to be added without completely rewriting them.

### Practical

A system should eventually be tested through real usage, not only isolated code.

---

## Design Principles

* Separate reusable systems from game-specific content.
* Prefer composition over unnecessary coupling.
* Keep core logic independent from UI and presentation.
* Use events when systems need to communicate without direct dependencies.
* Build small systems first, then improve their architecture through real usage.
* Use demos to validate how systems behave when combined.

---

## Development Approach

The project is developed iteratively.

The general process is:

```text
Idea
  ↓
Basic System
  ↓
V1 Implementation
  ↓
Integration
  ↓
Architecture Review
  ↓
V2 Improvements
  ↓
Testing
  ↓
More Advanced Systems
  ↓
Larger Demos
```

The project is currently moving from the basic V1 implementation and initial integration stage toward architecture refinement and V2 improvements.

---

## Planned Systems

Potential future systems include:

* Save / Load System
* Finite State Machine (FSM)
* Grid System
* A* Pathfinding
* Behavior Tree
* Skill System
* NPC / AI Systems
* Other systems that become useful through the development process

The exact priority of future systems will be decided based on the needs of the project and the architecture developed along the way.

---

## Technologies

* Python
* Pygame
* Git
* GitHub

---

## Project Status

The first major milestone of the project has been completed:

* Four core systems have been implemented.
* The systems have individual demos and documentation.
* A first MiniGame integrates the systems together.
* Event-driven communication has been demonstrated between systems.

The next stage focuses on improving the architecture and APIs of the existing systems before expanding the library with more advanced systems.

---

## Long-Term Goal

The long-term goal is to build a well-structured personal library of game systems that can be:

* Reused in future projects.
* Combined to create different gameplay experiences.
* Extended without unnecessary rewrites.
* Used as a practical demonstration of software architecture and game-development knowledge.

This repository is both a learning laboratory and a growing collection of reusable game-development systems.
