# PlagiaGuard – AI-powered Plagiarism Checker

PlagiaGuard is an intuitive, fast, and reliable plagiarism checker designed to help educators, students, and content creators quickly detect text similarities between essays, assignments, or articles.

## 🌟 Features

* **Real-time Similarity Analysis**: Instantly calculates the similarity score between two text inputs.
* **Grammar Word Filtering**: Excludes common grammar words (e.g., "the", "is", "in") to focus on significant content words.
* **Clear Results**: Provides a clear breakdown including the similarity percentage, common words, and unique words.
* **User-friendly Interface**: Designed with an intuitive, clean, and responsive UI.
* **Educational Tips**: Includes useful advice on how to avoid plagiarism.

## 🚀 Technologies

* **Backend**: Python (Flask)
* **Frontend**: HTML, CSS
* **Template Engine**: Jinja2

## 🛠️ How It Works

1. Paste or type the **Original Source Essay** and the **Suspected/Flagged Essay** into their respective input boxes.
2. Click on the **"Compare"** button.
3. PlagiaGuard instantly generates:

   * A **Similarity Score** indicating the degree of match.
   * Lists of **Common Words** and **Uncommon Words**.
   * A qualitative assessment (High, Medium, Low similarity).

## 📌 Similarity Score Formula

```
Similarity Score = (Matching Important Words ÷ Total Important Words in Original Essay) × 100
```

## ✅ Usage Example

* **Original Essay** has 10 significant words.
* **Suspected Essay** contains 6 of those words.
* **Similarity score** = (6 ÷ 10) × 100 = **60%**.

## 🔗 Live Demo

Try the live version here: [PlagiaGuard.xyz](https://plagiaguard.xyz)

## ⚙️ Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/plagiarism-checker.git
cd plagiarism-checker
```

### Step 2: Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # MacOS/Linux
.\env\Scripts\activate  # Windows
```

### Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:5000`

## 🤝 Contribution

Contributions are always welcome! Feel free to fork the repository and create a pull request.

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.
