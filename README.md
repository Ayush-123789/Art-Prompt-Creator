# 🎨 Art Prompt Creator ✨

**Generates unique and inspiring prompts for digital artists using the power of AI.**

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/framework-Flask-green.svg)](https://flask.palletsprojects.com/)
[![AI Model](https://img.shields.io/badge/AI-Google%20Gemini-purple.svg)](https://ai.google.dev/)
<!-- Optional: Add a Vercel deployment badge if you set it up -->
<!-- [![Deployment](https://vercel.com/YOUR_USERNAME/YOUR_PROJECT_NAME/deployments)] -->

---

<!-- **[IMPORTANT]** Add a screenshot or GIF of your app here! -->
<!-- ![App Screenshot](link_to_your_screenshot.png) -->
**(Replace the line above with an actual image link or embedded image showing your app's UI)**

---

## 🌟 Introduction

Are you a digital artist facing creative block? The **Art Prompt Creator** is here to help! This web application leverages Google's powerful Gemini AI model to generate unique, detailed, and imaginative prompts tailored to your desired themes and styles. Spark your next masterpiece with just a click!

Built with Python and Flask, and designed with a sleek, modern UI, this tool is easy to use and deployable on platforms like Vercel.

---

## 🔥 Features

*   **🤖 AI-Powered Prompts:** Utilizes Google Gemini for creative and diverse prompt generation.
*   **🎨 Customizable Input:** Specify desired **themes** (e.g., cyberpunk, fantasy, sci-fi) and **styles** (e.g., anime, watercolor, hyperrealistic).
*   **✨ Sleek User Interface:** Modern dark theme (purple & black) with a focus on usability.
*   **🚀 Deployable:** Ready for deployment on Vercel with included configuration (`vercel.json`).
*   **🌐 Web Accessible:** Simple web interface accessible from any browser.
*   **👤 Personalized:** Includes developer/student credits directly in the UI.

---

## 🔧 Tech Stack

*   **Backend:** Python 3.9+
*   **Framework:** Flask
*   **AI:** Google Generative AI SDK (for Gemini)
*   **Frontend:** HTML, CSS, JavaScript
*   **Deployment:** Vercel (optional, configured)
*   **Environment Variables:** python-dotenv

---

## ⚙️ Setup & Installation

Follow these steps to get the project running locally:

1.  **Prerequisites:**
    *   Python 3.9 or later installed.
    *   `pip` (Python package installer).
    *   Git (for cloning).

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
    ```
    *(Replace `YOUR_USERNAME/YOUR_REPOSITORY_NAME` with your actual GitHub details)*

3.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set Up Environment Variables:**
    *   You need a Google Gemini API key. Get one from [Google AI Studio](https://aistudio.google.com/app/apikey).
    *   Create a file named `.env` in the root directory of the project.
    *   Add your API key to the `.env` file like this:
        ```dotenv
        GEMINI_API_KEY=YOUR_API_KEY_HERE
        ```
    *(Replace `YOUR_API_KEY_HERE` with your actual key. The `.gitignore` file should prevent this file from being committed to Git.)*

---

## ▶️ Running Locally

Once the setup is complete, start the Flask development server:

```bash
flask run --port 5001
# or
python app.py