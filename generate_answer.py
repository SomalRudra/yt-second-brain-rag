from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8090/v1",api_key="not-needed-for-local")

def generate_answer(user_query, context):
    print(context)
    response = client.chat.completions.create(
        model="local-model",
        messages=[
            {
                "role": "system", 
                "content": (
                    "You are a precise technical QA bot. Your task is to answer questions "
                    "using ONLY the provided Context. \n\n"
                    "RULES:\n"
                    "1. If the answer is not contained within the Context, state 'I cannot find that in the video transcript.'\n"
                    "2. Do NOT use outside knowledge or make guesses (e.g., do not guess 'RagTime').\n"
                    "3. Keep answers concise and fact-based.\n"
                    "4. If a name is mentioned in the Context, provide it exactly as written."
                )
            },
            {
                "role": "user", 
                "content": f"Context for the video:\n{context}\n\nQuestion: {user_query}"
            },
        ],
        temperature=0.1 # This makes the model more deterministic and less "creative"
    )
    return response.choices[0].message.content