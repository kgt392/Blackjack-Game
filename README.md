# ♠️ Blackjack Game - Python Terminal Version

## 📚 Project Description

This project is a simple implementation of the classic **Blackjack (21)** card game built using Python.  
Players compete against the dealer (computer) by trying to get a hand total as close to 21 as possible, without going over!

This project helps reinforce understanding of **loops, functions, conditionals, lists, and random module** in Python.

---

## 🎯 Features

- Play against a computer dealer.
- Random card drawing using Python's `random` module.
- Automatic Ace (1 or 11) handling.
- Simple user inputs: Hit (Draw card) or Stand (Hold current hand).
- Win, lose, and draw outcomes displayed clearly.

---

## 🛠️ Technologies Used

- Python 3.x
- No external libraries needed (only built-in modules).



## 🎮 How to Play

- You and the dealer are each dealt two cards initially.
- Cards have point values:  
  - 2-10: Face value  
  - Jack/Queen/King: 10 points  
  - Ace: 1 or 11 points, whichever is favorable
- Your goal is to have cards that add up to **21 or less**, but **higher than the dealer**.
- Choose to:
  - **Hit**: Draw another card.
  - **Stand**: Hold your current total.
- If your total exceeds 21, you **bust** and lose.

---

## 📸 Example Game Play

```plaintext
Your cards: [8, 9]  - current score: 17
Dealer's first card: 6

Type 'y' to get another card, type 'n' to pass: y
Your cards: [8, 9, 2] - current score: 19

Dealer's cards: [6, 7, 8] - final score: 21
You lose 😭
```
