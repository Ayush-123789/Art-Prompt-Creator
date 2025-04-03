import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template # Added render_template
from dotenv import load_dotenv

# Load environment variables (especially your API key)
load_dotenv()

app = Flask(__name__)

# Configure the Gemini API
# --- IMPORTANT: Store your API key securely! ---
# Best practice: Use environment variables. Create a .env file
# in your project root with: GEMINI_API_KEY=YOUR_API_KEY_HERE
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("⚠️ Warning: GEMINI_API_KEY not found in environment variables.")
    # Handle the missing key case gracefully - maybe raise an error or use a default?
else:
    genai.configure(api_key=api_key)

# Initialize the Gemini Model (choose the appropriate model)
# Check the Google AI documentation for available models
model = genai.GenerativeModel('gemini-1.5-flash') # Or another suitable model like 'gemini-pro'

# Route for a simple web interface (optional)
@app.route('/')
def home():
    # Renders an HTML file from the 'templates' folder
    return render_template('index.html')

# API endpoint to generate the art prompt
@app.route('/generate_prompt', methods=['POST', 'GET']) # Allow GET for simple testing
def generate_art_prompt():
    try:
        # --- Get optional input from user (e.g., style, theme) ---
        # For a POST request with JSON data:
        # data = request.get_json()
        # user_input = data.get('theme', 'anything') # Example: get 'theme' or default

        # For a GET request or simple POST form:
        user_input_theme = request.values.get('theme', 'fantasy') # Get theme from form/query param
        user_input_style = request.values.get('style', 'digital painting') # Get style

        # --- Craft the prompt for Gemini ---
        # Be descriptive to guide the AI effectively!
        prompt_for_gemini = (
            f"Generate a unique and inspiring art prompt for a digital artist. "
            f"The desired theme is '{user_input_theme}' and the preferred style is '{user_input_style}'. "
            f"The prompt should be creative, evocative, and provide enough detail to spark imagination, "
            f"but leave room for artistic interpretation. Avoid generic prompts. "
            f"Example: 'A lone astronaut discovering a bioluminescent forest on a forgotten moon, painted in a vibrant, impressionistic style.' "
            f"Now, create a new one:"
        )

        # --- Call the Gemini API ---
        print(f"🤖 Sending prompt to Gemini: {prompt_for_gemini}") # Log for debugging
        response = model.generate_content(prompt_for_gemini)

        # --- Extract the generated text ---
        generated_prompt = response.text.strip()
        print(f"✅ Gemini response received: {generated_prompt}") # Log for debugging

        # --- Return the result as JSON ---
        return jsonify({
            "success": True,
            "art_prompt": generated_prompt,
            "theme_requested": user_input_theme,
            "style_requested": user_input_style
        })

    except Exception as e:
        print(f"❌ Error generating prompt: {e}") # Log the error
        # --- Handle potential errors (API issues, etc.) ---
        return jsonify({"success": False, "error": str(e)}), 500

# --- Vercel expects the app object to be named 'app' ---
if __name__ == '__main__':
    # This runs the app locally for testing (not used by Vercel)
    app.run(debug=True, port=5001) # Use a port other than Vercel's default