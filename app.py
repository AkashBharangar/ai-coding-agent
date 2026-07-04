from groq import Groq

from utils.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import logger


def main():
    print("=" * 50)
    print("AI Coding Agent")
    print("=" * 50)

    if not GROQ_API_KEY:
        print("Groq API Key not found!")
        return

    client = Groq(api_key=GROQ_API_KEY)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": "Reply with Setup Successful"
            }
        ],
        temperature=1,
    )

    answer = response.choices[0].message.content

    print(answer)

    logger.info("Groq connection successful")


if __name__ == "__main__":
    main()