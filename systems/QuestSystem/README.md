# Quest System

A reusable quest management system built with Python.

This system provides a foundation for creating quests, managing objectives, tracking progress, and detecting quest completion.

It is designed to remain independent from specific game content and to be usable as a reusable game-development system.

---

## Goal

The goal of this system is to understand how quest systems work internally and to build a reusable foundation that can be expanded for different types of games.

The system also serves as an example of how a gameplay system can communicate with other systems through an event-driven architecture.

---

## Current Features

* Quest creation
* Quest descriptions
* Quest objectives
* Multiple objectives per quest
* Objective progress tracking
* Objective completion detection
* Quest completion detection
* Active quest management
* Completed quest management
* Adding quests
* Removing quests
* Event-driven integration with the Event System

---

## Basic Structure

A `Quest` represents a complete mission.

Each quest can contain multiple `QuestObjective` objects.

```text
Quest
│
├── Objective 1
├── Objective 2
└── Objective 3
```

For example:

```text
Quest: Find the Lost Sword

└── Find the Lost Sword
       Progress: 1 / 1
       Status: Complete
```

A more complex quest can contain multiple objectives:

```text
Quest: Save the Village

├── Find the Sword
├── Defeat the Monster
└── Talk to the Village Chief
```

---

## Core Classes

### `Quest`

Represents a complete quest.

It contains:

* Quest name
* Description
* Objectives
* Completion detection

---

### `QuestObjective`

Represents an individual task within a quest.

It contains:

* Objective description
* Required amount
* Current progress
* Completion detection

---

### `QuestSystem`

Manages the quests currently being tracked.

It currently maintains:

* Active quests
* Completed quests
* All registered quests

It is also responsible for checking quest completion.

---

## Project Structure

```text
QuestSystem/
│
├── Quest.py
├── QuestObjective.py
├── QuestSystem.py
├── demo.py
└── README.md
```

---

## Quest Lifecycle

The current system follows a simple lifecycle:

```text
Quest Created
     ↓
Quest Added
     ↓
Active Quest
     ↓
Objectives Progress
     ↓
All Objectives Complete
     ↓
Completed Quest
```

---

## Integration

The Quest System is currently integrated with the Event System.

In the current MiniGame demo, a dialogue choice can trigger an event that starts a quest.

Later, another gameplay event can update the progress of a quest objective.

Example:

```text
Dialogue
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
Active Quest

Exploration
   │
   │ EXPLORE_ENDED
   ▼
Event System
   ├──────────────► Inventory System
   │
   └──────────────► Quest System
```

This allows the Quest System to react to gameplay events without requiring direct communication with the systems that generated those events.

---

## Current Version

**V1**

The first functional version of the Quest System is complete.

The current version provides the basic foundation required to create quests, track objectives, and detect completion.

---

## Current Limitations

The current version intentionally keeps quest logic simple.

It does not yet provide:

* Quest rewards
* Quest dependencies
* Optional objectives
* Advanced objective types
* Detailed quest states
* Quest persistence
* Save/load support
* Automatic objective matching against arbitrary gameplay events
* A formal reward system

These are potential areas for future versions.

---

## Planned Improvements

Possible future improvements include:

* Quest rewards
* Quest dependencies
* Optional objectives
* Multiple quest states
* More advanced objective types
* Better event-driven objective tracking
* Save/load support
* Quest persistence
* Dialogue integration improvements
* Better testing
* More flexible quest progression rules

---

## Design Goals

The Quest System should remain:

* Reusable
* Independent from specific game content
* Easy to extend
* Easy to test
* Compatible with other game systems
* Independent from UI and presentation

---

## Development Status

The basic V1 implementation is complete.

The next stage of development will focus on reviewing the architecture, improving the quest API, strengthening the event integration, and preparing the system for more advanced quest mechanics.
