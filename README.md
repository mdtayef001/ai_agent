# AI Agent with Google Gemini (gemini-2.5-flash)

This project is an AI agent built using **Google Gemini’s free API**.  
The agent can **read files, write files, and retrieve directory information** from a given target directory.

The main idea of this project is to give the AI agent a **set of predefined functions** and allow it to **decide which function to use based on the user prompt**.

---

## How It Works

- I implemented **4 core Python functions**.
- These functions are exposed to the AI agent as available tools.
- Based on the **user prompt**, the agent analyzes the intent and **automatically selects the appropriate function**.
- The agent **runs in a loop**, continuously reasoning and executing actions until the task is completed.
- To prevent infinite loops, the agent execution is **limited to a maximum of 20 steps**.

---

## Agent Execution Loop

1. The user provides a prompt.
2. The agent analyzes the prompt and current context.
3. The agent selects one of the available functions.
4. The function is executed on the target directory.
5. The result is fed back to the agent.
6. Steps 2–5 repeat **until the task is finished or the step limit is reached**.

⛔ The agent will automatically stop after **20 iterations**, even if the task is not fully completed.

---

## Available Functions

The agent has access to the following functions:

1. **Read File**

2. **Write File**

3. **Run python file**

4. **Get Directory Info**

The agent dynamically chooses which function to call based on the prompt.

---

## Features

- 🤖 AI agent powered by Google Gemini (free tier)
- 🧠 Dynamic function selection based on prompt intent
- 🔁 Loop-based execution until task completion
- ⛔ Built-in safety limit of **20 agent steps**
- 📂 Read, write, and inspect files
- 🔒 Controlled access to a target directory

---

## Requirements

- **Python 3.8+**
- **uv** (Python package manager)
- **Google Gemini API Key**
