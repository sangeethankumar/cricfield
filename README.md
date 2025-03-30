# 🏏 CricField


**CricField** is an interactive visualizer for placing cricket fielders on a ground. Designed just for fun exploration.

**Made with ❤️ and a love for cricket**

---

## 📦 Features

- Add and move
- Enforces field restrictions (e.g., number of players outside inner ring)
- Right/Left-handed batter support
- Visual guide to standard fielding positions
- Minimalist design with full-screen experience

---

## 🛠️ Installation

I recommend using **Miniforge** and Python **3.12** for compatibility.

### 1. Clone the repository

```bash
git clone https://github.com/sangeethankumar/cricfield.git
cd cricfield
```

### 2. Create and activate a conda environment

```bash
conda create -n cricfield python=3.12
conda activate cricfield
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the app locally (editable mode)

```bash
pip install .
```

---

## 🚀 Launch the App

After installation:

```bash
cricfield
```

If everything is working, you should see the **CricField Settings Menu** pop up!

---

## 🎮 Controls

- **Mouse Click** – Place or select a player
- **Arrow Keys** – Move selected player
- **ESC** – Quit

---

## 🧩 Settings Menu

Choose:

- Total players on field
- Max players outside inner ring
- Fielder movement speed
- Fullscreen or windowed
- Right- or Left-handed batter

---

## 📁 Folder Structure (Simplified)

```
cricfield/
├── src/cricfield/
│   ├── main.py
│   ├── adapters/
│   ├── core/
│   └── domain/
├── assets/
│   └── icon.png
├── requirements.txt
├── README.md
├── pyproject.toml
```

---

## 🧪 Development Mode

Install the app in editable mode

```bash
pip install -e .
```

> The `-e` flag lets you make changes to the code and re-run without reinstalling.

This project is modular and extensible. To make changes:

1. Modify code inside `src/cricfield/`
2. Run `cricfield` again — no reinstall needed!

---

## 📃 License

MIT License. Use it, modify it, fork it — just give credit.

---

## 🤝 Contributions

Pull requests and feedback are welcome! Feel free to open an [issue](https://github.com/sangeethankumar/cricfield/issues).

---

