# Dialogue System

A reusable dialogue system built with Python.

This project is part of **Game-Systems-Lab**, a collection of reusable game systems developed to better understand game architecture and software design.

## Goal

* Understand how dialogue systems work internally.
* Learn how branching conversations are structured.
* Practice object-oriented design and tree-based data structures.
* Build a reusable dialogue system that can be used in future game projects.

## Features

* Dialogue nodes
* Dialogue choices
* Branching dialogue flow
* Current dialogue state management
* Choice selection system
* Dialogue completion detection
* Separated dialogue content from dialogue logic
* Demo dialogue runner for testing

## Project Structure

```text
DialogueSystem/
│
├── DialogueNode.py
├── DialogueChoice.py
├── DialogueSystem.py
├── demo.py
└── README.md
```

## How it works

The dialogue system uses a node-based structure.

Each `DialogueNode` contains:

* Dialogue text
* Available choices

Each `DialogueChoice` contains:

* Choice text
* Reference to the next dialogue node

The `DialogueSystem` manages the current node and moves through the dialogue tree based on player choices.

Example:

```
              Hello!
                 |
        ----------------
        |              |
    Who are you?   Goodbye
        |
        ↓
   I am the guard.
```

## Current Version

The first version of the system is complete.

Currently supported:

* Creating dialogue trees
* Moving between dialogue nodes
* Selecting player choices
* Detecting the end of a conversation
* Running a simple console-based dialogue demo

## Future Improvements

Possible future extensions:

* Dialogue conditions
* Event triggers
* Quest integration
* Save and load dialogue state
* Dialogue localization
* Loading dialogues from external files (JSON)

## Why did I start this project?

Most games use dialogue systems, but I wanted to understand how they are designed internally instead of only using existing implementations.

The goal of this project is to learn the architecture behind dialogue systems by building one from scratch and making it reusable for future projects.
