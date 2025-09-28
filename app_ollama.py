import subprocess

def generate_blog(topic: str) -> str:
    prompt = f"Write a short blog post about {topic} in English."
    result = subprocess.run(
        ["ollama", "run", "llama2:7b", prompt],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    return result.stdout.strip()

if __name__ == "__main__":
    topic = input("Enter blog topic: ")
    print("\n===== Ollama Llama-2 Generated Blog =====\n")
    print(generate_blog(topic))
