
# 🏏 Cricket Net Run Rate (NRR) Calculator

A simple and interactive **Streamlit** web app to calculate the **Net Run Rate (NRR)** between two cricket teams based on match performance — including runs, overs, and wickets.

---

## 🚀 Features

- Input team names, runs, wickets, and overs
- Accurate overs conversion (e.g., 19.3 ➝ 19.5)
- Handles "all out" scenarios using default overs
- Displays Net Run Rate for both teams
- Built with Python and Streamlit

---

## 📦 Installation

Make sure you have Python 3.7 or later installed. Then, install Streamlit:

```bash
pip install streamlit
```

---

## ⚙️ How to Run

1. Clone this repository or save the script as `nrr_calculator.py`
2. Open your terminal or command prompt
3. Navigate to the project directory
4. Run the app with:

```bash
streamlit run nrr_calculator.py
```

---

## 🧠 Logic Details

### ➤ Net Run Rate Formula

```
NRR = (Total Runs Scored ÷ Total Overs Faced) − (Total Runs Conceded ÷ Total Overs Bowled)
```

### ➤ Overs Conversion

- In cricket, overs like `19.3` mean 19 overs and 3 balls.
- Conversion formula:

```
actual_overs = full_overs + (balls / 6)
```

- Example: `19.3` ➝ `19 + 3/6` ➝ `19.5`

### ➤ All-Out Rule

If a team is **all out before completing their quota**, the **full default overs** are used for Net Run Rate calculation (e.g., 20 in T20 or 50 in ODIs).

---

## 👨‍💻 Author

**Glaston Jiue**  
Feel free to fork, star, or contribute to this project!

---

## 📄 License

This project is licensed under an open-source license and is free to use and modify.
