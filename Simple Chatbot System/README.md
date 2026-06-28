# Simple FAQ Chatbot System

A Python implementation of a **rule-based FAQ chatbot** that answers
common questions using a pre-defined knowledge base (dictionary of
question-answer pairs).

---

## 1. Definition

A chatbot is a software application that simulates human conversation
through text input. This is a **rule-based (retrieval-based)
chatbot** — it does not "understand" language or generate new
responses. Instead, it works by matching the user's exact input
against a fixed set of known questions stored in a dictionary, and
returning the corresponding pre-written answer.

This is one of the simplest forms of a chatbot, often used as a
starting point before exploring more advanced techniques like fuzzy
matching, intent recognition, or AI/NLP-based chatbots (e.g., using
machine learning or large language models).

---

## 2. How It Works

- A dictionary (`FAQ`) stores **questions as keys** and **answers as
  values**, with all keys in lowercase.
- When the user types something, the input is cleaned (converted to
  lowercase and trimmed of extra spaces) before being checked against
  the dictionary.
- If an exact match is found, the chatbot replies with the
  corresponding answer.
- If no match is found, the chatbot replies with a default fallback
  message.
- The chatbot keeps running in a loop until the user types `bye`.

---

## 3. Features

- Answers a variety of pre-defined questions (greetings, tech
  definitions, programming concepts, etc.)
- Case-insensitive matching (`Hi`, `hi`, and `HI` all work the same)
- Ignores extra leading/trailing spaces in user input
- Clean exit using the `bye` command
- Easy to expand — just add new question-answer pairs to the `FAQ`
  dictionary
- Graceful fallback response for unrecognized questions

---

## 4. Uses in Artificial Intelligence

Rule-based chatbots like this one are a foundational concept in AI
and Natural Language Processing (NLP), used to introduce ideas such
as:

- **Knowledge representation** — storing facts/responses in a
  structured form (here, a dictionary) that a program can search
  through
- **Pattern matching** — the core technique behind many early chatbot
  systems, including ELIZA (one of the first chatbots ever built)
- **Human-Computer Interaction (HCI)** — designing systems that can
  respond to natural human input in a useful way
- **Customer support automation** — many real-world FAQ bots (on
  websites, apps) use a similar rule-based approach for handling
  common, repetitive questions
- A stepping stone toward more advanced techniques like **fuzzy
  string matching** (handling typos/variations), **intent
  classification**, and **NLP-based or LLM-based chatbots**

---

## 5. Algorithm Overview

**Steps:**

1. Store all known questions and their answers in a dictionary
   (`FAQ`).
2. Display a welcome message to the user.
3. Repeat the following in a loop:
   - Read the user's input.
   - If the input (case-insensitive) is `"bye"`, print a goodbye
     message and stop the loop.
   - Otherwise, clean the input (lowercase + strip spaces) and check
     if it exists as a key in the `FAQ` dictionary.
     - If found, print the corresponding answer.
     - If not found, print a default "I don't understand" message.
4. The loop continues until the user exits.

---

## 6. Time Complexity

**O(1)** per lookup

Since `FAQ` is a Python dictionary (a hash map), checking whether a
question exists and retrieving its answer both take constant time,
regardless of how many question-answer pairs are stored.

---

## 7. Space Complexity

**O(N)**

Where `N` is the number of question-answer pairs stored in the `FAQ`
dictionary. Space grows linearly as more questions are added.

---

## 8. How to Run

```bash
python chatbot.py
```

Type your question, and the chatbot will respond if it recognizes it.
Type `bye` to exit.

### Example Run

```
===================================
     Welcome to FAQ Chatbot
Type 'bye' to exit the chatbot.
===================================

You: hi
Bot: Hello! How can I help you?

You: what is python
Bot: Python is a popular programming language used for web development, AI, data science, and more.

You: who is the president
Bot: Sorry, I don't understand that question.

You: bye
Bot: Goodbye! Have a nice day.
```

---

## 9. Advantages

- Very simple and fast to implement
- Instant (constant-time) response lookup
- Easy to understand, debug, and extend with new questions
- No external libraries or training data required

## 10. Disadvantages

- Only understands **exact matches** — cannot handle typos, rephrased
  questions, or synonyms (e.g., "what's python" would fail even
  though "what is python" works)
- Cannot understand context or hold a multi-turn conversation
- Does not scale well for large, open-ended conversations — would
  need NLP techniques (like fuzzy matching, tokenization, or machine
  learning) to handle more natural and varied user input

---

## Author

Niharika Acharya
