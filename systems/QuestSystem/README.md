# Quest System

A reusable quest management system built with Python.

This project is part of **Game-Systems-Lab**, a collection of reusable game systems and mechanics that I develop to better understand game development and system architecture.

## Goal

* Understand how quest systems work behind the scenes.
* Learn how quests and objectives can be structured.
* Build a reusable quest management system.
* Practice designing systems that are independent from specific game content.
* Create a foundation that can be expanded and used in future game projects.

## Features

The initial version of the system will focus on:

* Quest management
* Quest objectives
* Objective progress tracking
* Quest completion detection
* Multiple objectives per quest

## Basic Structure

A Quest represents a complete mission, while Objectives represent the individual tasks that must be completed.

```text
Quest
│
├── Objective 1
├── Objective 2
└── Objective 3
```

For example:

```text
Quest: Save the Village

├── Find the Sword
├── Defeat the Monster
└── Talk to the Village Chief
```

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

## Planned Improvements

Possible future extensions:

* Event System integration
* Quest rewards
* Quest dependencies
* Optional objectives
* Multiple quest states
* Save and load quest progress
* Dialogue System integration
* More advanced objective types

## Why did I start this project?

I started this project to understand how quest systems are designed and managed in games.

Instead of creating quest logic specifically for one game, I want to build a reusable system that can handle different types of quests and objectives.

The system will also provide an opportunity to connect different game systems together, such as the Dialogue System, Event System, and Inventory System.
