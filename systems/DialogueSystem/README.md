# Dialogue System

A reusable dialogue system built with Python.

This project is part of **Game-Systems-Lab**, a collection of reusable game systems developed to better understand game architecture and software design.

## Goal

* Learn how dialogue systems work internally.
* Design a reusable dialogue architecture instead of creating one for a specific game.
* Practice object-oriented design and tree-based data structures.
* Build a flexible foundation that can be extended with conditions, quests, localization, and other dialogue features in the future.

## Features

* Dialogue nodes
* Dialogue choices
* Branching conversations
* Reusable architecture
* Demo project for testing

## Project Structure

```text
dialogue_system/
│
├── DialogueNode.py
├── DialogueChoice.py
├── DialogueSystem.py
├── demo.py
└── README.md
```

## Current Version

This is the first version of the system.

Currently supported:

* Basic dialogue nodes
* Dialogue choices
* Branching dialogue flow

Planned improvements:

* Conditional dialogues
* Quest integration
* Events
* Dialogue serialization (JSON)
* Localization support
* Save & load dialogue state

## Why did I start this project?

Most games use dialogue systems, but I wanted to understand how they are designed internally rather than simply using an existing engine implementation.

The goal of this project is to learn the architecture behind dialogue systems by building one from scratch, making it reusable for future projects.
