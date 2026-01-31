# Data Science Tool: PandasAI + Ollama (gemini-3-flash-preview:cloud)

This project is a simple data science helper app built with **Streamlit**, **pandas**, **PandasAI**, and a local **Ollama** gemini-3-flash-preview:cloud model.

You can:
- Upload a CSV file
- Preview the first few rows
- Ask questions about the data in natural language
- Let PandasAI generate and run code against your DataFrame using the local gemini-3-flash-preview:cloud model

---

## Project Structure

- `app.py` – Streamlit app with a custom `OllamaLLM` class that connects PandasAI to Ollama's gemini-3-flash-preview:cloud model
- `requirements.txt` – Python dependencies for this tool

---

## Requirements

- Python 3.8–3.11
- [Ollama](https://ollama.com) installed and running locally
- gemini-3-flash-preview:cloud model pulled in Ollama
- A virtual environment with the dependencies installed

### 1. Install and prepare Ollama

1. Install Ollama from the official website.
2. Pull the gemini-3-flash-preview:cloud model (run once):

   ```bash
   ollama pull gemini-3-flash-preview:cloud
   ```

3. (Optional) Test the model in a terminal:

   ```bash
   ollama run gemini-3-flash-preview:cloud
   ```

Ollama should expose an HTTP API on `http://localhost:11434`.

### 2. Set up the Python environment

From the `Projects` folder (where your `.venv` lives), activate your virtual environment and install dependencies:

```bash
cd "c:\Users\hp\Desktop\ai projects\Projects"

# (if the venv is not created yet)
# python -m venv .venv

# Activate on Windows (Command Prompt)
.venv\\Scripts\\activate

pip install -r "Data science tool/requirements.txt"
```

---

## Running the App

With the virtual environment activated and Ollama running:

```bash
cd "c:\Users\hp\Desktop\ai projects\Projects"
streamlit run "Data science tool/app.py"
```

Then open the URL shown in the terminal (usually `http://localhost:8501`).

In the UI:
- Upload a CSV file
- Check the preview of the data
- Type a question in the prompt box (e.g. *"What is the average of column X?"*)
- Click **Run** to let PandasAI + gemini-3-flash-preview:cloud analyze the data

---

## Notes and Known Issues

- **Sometimes the model does not respond** or the app may hang for a while. Common causes:
  - Ollama is not running or the gemini-3-flash-preview:cloud model is not loaded
  - The request times out or the model takes too long to answer
  - The response format from Ollama changes
- When this happens, you may see an error in the Streamlit terminal (or a traceback mentioning `Ollama call failed`). If the page seems stuck:
  - Make sure Ollama is running: `ollama run gemini-3-flash-preview:cloud` (or check the Ollama app)
  - Restart the Streamlit app: stop the process, then run `streamlit run "Data science tool/app.py"` again
  - Try a simpler, shorter question

If you keep getting errors, check that the API is reachable by opening `http://localhost:11434` in your browser or by running a simple `curl`/`requests` call to `/api/chat`.

---

## How It Works (High Level)

- `OllamaLLM` in `app.py` subclasses PandasAI's `LLM` base class and sends prompts to Ollama's `/api/chat` endpoint.
- A `Config` object is created with this `OllamaLLM` instance and passed to `SmartDataframe`.
- When you call `df.chat(prompt)`, PandasAI builds a prompt, sends it through `OllamaLLM` to gemini-3-flash-preview:cloud, gets back Python code, and executes it against your DataFrame.

This README is intended for GitHub, so anyone cloning the repo can set up Ollama and run the tool easily, while being aware that the local gemini-3-flash-preview:cloud model may occasionally be slow or unresponsive.