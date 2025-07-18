import subprocess
import time
import os
CONVERSATION_FOLDER = os.path.expanduser("~/Desktop/ai conversations")
CONVERSATION_FILE = os.path.join(CONVERSATION_FOLDER, "conversation.txt")
def is_ollama_running():
    print("Starting Ollama daemon...")
    try:
        subprocess.Popen(["ollama", "start"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(10):
            if is_ollama_running():
                break
            time.sleep(0.5)
        else:
            raise RuntimeError("Ollama daemon did not start in time.")
    except Exception as e:
        print("Failed to start Ollama daemon:", e)
        exit(1)
def get_loaded_model():
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
        lines = result.stdout.strip().splitlines()
        return [line.split()[0] for line in lines[1:]]
    except Exception as e:
        print("Failed to list models:", e)
        return []
def prompt_model_choice(models):
    os.makedirs(CONVERSATION_FOLDER, exist_ok=True)
    with open(CONVERSATION_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")
def load_saved_conversation():
    if os.path.exists(CONVERSATION_FILE):
        with open(CONVERSATION_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    return ""
def main():
    if not is_ollama_running():
        start_ollama_daemon()
    model = get_loaded_model()
    if model is None:
        models = list_models()
        if not models:
            print("No models installed. Please install a model first.")
            exit(1)
        model = prompt_model_choice(models)
    print(f"Using model: {model}")
    remembering = False
    while True:
        user_input = input("You: ").strip()
        lower = user_input.lower()
        if lower == "exit":
            print("Exiting...")
            break
        elif lower == "remember":
            remembering = True
            print("AI: I will now remember the conversation history.")
            continue
        elif lower == "forget":
            remembering = False
            print("AI: I have forgotten the conversation history.")
            continue
        if remembering:
            past_conversation = load_saved_conversation()
            prompt_input = f"{past_conversation}\nYou: {user_input}"
        else:
            prompt_input = f"You: {user_input}"
        try:
            process = subprocess.Popen(
                ["ollama", "run", model],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            process.stdin.write(prompt_input)
            process.stdin.close()
            response_lines = []
            for line in process.stdout:
                print(line, end='')
                response_lines.append(line)
            response = ''.join(response_lines).strip()
        except Exception as e:
            response = f"Error communicating with Ollama: {e}"
            print(response)
        save_conversation(f"You: {user_input}")
        save_conversation(f"AI: {response}")
if __name__ == "__main__":
    main()