from groq import Groq

client = Groq(api_key="API Input")

def chat(msg):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": msg,
            }
        ],
        model="llama3-8b-8192",
        )

    for i in range(0,len(chat_completion.choices[0].message.content),2000):
        return chat_completion.choices[0].message.content[i:i+2000]
