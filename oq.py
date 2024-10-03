import config
import ollama

c = config.get_config()


def ollama_query(prompt: str, model: str = "llama3.2") -> str:
    try:
        # Create a client (might read this host naturally)
        client = ollama.Client(host=c["OLLAMA_HOST"])

        # Generate a response
        response = client.generate(model=model, prompt=prompt)

        # Return the generated text
        return response["response"]
    except Exception as e:
        return f"Error: {str(e)}"


# Example usage
if __name__ == "__main__":
    user_prompt = "Explain the concept of quantum entanglement in simple terms."
    result = ollama_query(user_prompt)
    print(result)
