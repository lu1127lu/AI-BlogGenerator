from app_ollama import generate_blog

def test_length_and_keyword():
    topic = "renewable energy"
    print("Generating ...")          
    out = generate_blog(topic)
    assert len(out) > 50, "Too short"
    assert "renewable" in out.lower() or "energy" in out.lower()
    print("✅ Test passed!")

if __name__ == "__main__":
    test_length_and_keyword()
