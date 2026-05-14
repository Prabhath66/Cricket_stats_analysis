# 🏏 Cricket Stats Dashboard

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=flat-square&logo=plotly&logoColor=white)](https://plotly.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Live Demo](https://img.shields.io/badge/🤗%20Hugging%20Face-Live%20Demo-yellow?style=flat-square)](https://huggingface.co/spaces/Prabhath6/Cricket_)

> **An interactive web application to explore and visualize cricket player statistics across Test, ODI, T20, and IPL formats.**

🌐 **[Live Demo → Try it on Hugging Face Spaces](https://huggingface.co/spaces/Prabhath6/Cricket_)**

---

## 📖 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [How to Use](#-how-to-use)
- [Data Overview](#-data-overview)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧠 About the Project

The **Cricket Stats Dashboard** is a data-driven web application built with **Streamlit** and **Plotly** that lets cricket fans and analysts explore detailed batting and bowling statistics for players across all major formats — **Test**, **ODI**, **T20**, and **IPL**.

Whether you want to compare a player's strike rate in T20s vs ODIs, check how many maiden overs a bowler has bowled in Tests, or simply visualize a batter's sixes across formats — this dashboard has you covered with clean, interactive charts and a minimal, easy-to-navigate UI.

> *"Cricket is not just a sport, it's an emotion."* 🌟

---

## ✨ Features

- 🌍 **Country-based Player Filtering** — Select a country to browse its players from the sidebar
- 👤 **Player Selection** — Drill down into any player's individual profile
- 📋 **Format Toggle** — Switch seamlessly between Test, ODI, T20, and IPL views
- 🧮 **Key Metrics at a Glance** — Instantly see Matches, Runs, Average, Strike Rate, Highest Score, Wickets, Economy, and Best Bowling figures
- 📊 **Interactive Batting Charts:**
  - Matches distribution across formats (Pie Chart)
  - Runs scored across formats (Bar Chart)
  - Fours vs Sixes comparison (Grouped Bar Chart)
- 🎯 **Interactive Bowling Charts:**
  - Matches distribution across formats (Pie Chart)
  - Wickets taken across formats (Bar Chart)
  - Overs bowled vs Maiden Overs (Grouped Bar Chart)
- 🗂️ **Expandable Raw Data Tables** — View the underlying stats in a clean table format

---

## 🎥 Demo

> 🔗 **[Launch the Live App](https://huggingface.co/spaces/Prabhath6/Cricket_)**

Navigate to the live demo on Hugging Face Spaces to try the app without any local setup. Select a country and player from the sidebar to start exploring their stats instantly.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.9+** | Core programming language |
| **Streamlit** | Web app framework & UI |
| **Pandas** | Data loading and manipulation |
| **Plotly Express** | Interactive visualizations |
| **NumPy** | Numerical operations |
| **Matplotlib / Seaborn** | Supporting visualization utilities |
| **openpyxl** | Reading Excel (.xlsx) data files |

---

## 📁 Project Structure

```
Cricket_/
│
├── app.py                      # Home page — introduction and navigation
├── requirements.txt            # Python dependencies
│
├── pages/
│   └── players_stats.py        # Main dashboard — filters, metrics & charts
│
├── total_teams_batting.csv     # Batting statistics dataset (all countries & players)
└── Bowling_Stats_Excel.xlsx    # Bowling statistics dataset (all countries & players)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Cricket-Stats-Dashboard.git
   cd Cricket-Stats-Dashboard
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

5. Open your browser and go to `http://localhost:8501`

---

## 📌 How to Use

1. **Home Page** — Read about the project and click **"Explore All Players Stats"** to navigate to the dashboard.

2. **Sidebar — Select Country** — Start typing or scroll through the dropdown to pick a country (e.g., India, Australia, England).

3. **Sidebar — Select Player** — Once a country is selected, choose a player from the filtered list.

4. **Choose Format** — Use the radio buttons to switch between **Test**, **ODI**, **T20**, and **IPL** views.

5. **Explore Stats:**
   - View **key batting metrics** (Matches, Runs, Average, Strike Rate, Highest Score)
   - View **key bowling metrics** (Wickets, Average, Economy, Strike Rate, Best Bowling)
   - Switch between the **🏏 Batting** and **🎯 Bowling** tabs for in-depth charts
   - Expand the **"Show Table"** section to inspect the raw numbers

---

## 📊 Data Overview

The app is powered by two datasets:

| File | Description |
|---|---|
| `total_teams_batting.csv` | Batting stats for players from multiple countries across Test, ODI, T20, and IPL formats. Includes: Matches, Runs, Average, Strike Rate, Fours, Sixes, Highest Score, and more. |
| `Bowling_Stats_Excel.xlsx` | Bowling stats for players across all formats. Includes: Wickets, Average, Economy Rate, Strike Rate, Maidens, Balls, Best Bowling Match (BBM), and more. |

Both datasets are structured in a long format keyed by `country`, `name`, and `ROWHEADER` (the stat name), making it straightforward to pivot and display per-player, per-format views.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add: your feature description"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

### Ideas for Contributions

- 📅 Add historical match-by-match data for timeline charts
- 🆚 Add a player comparison feature (compare two players side by side)
- 🌐 Scrape and auto-update live cricket stats
- 🎨 Theme customization or dark mode improvements
- 📱 Mobile responsiveness improvements

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

Made with ❤️ and 🏏 by [Prabhath66](https://github.com/Prabhath66)

⭐ **If you found this project useful, give it a star!** ⭐
