from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="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")  # 🔑 Replace with your actual key

# Load your website text
with open("website_content.txt", "r", encoding="utf-8") as f:
    website_text = f.read()

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.get_json().get("question", "")

    prompt = f"""
    You are an AI assistant on a website.
    Answer the user's question using only the information below.
    If you cannot find the answer, say: "I don’t have that information on this website."

    Website content:
    {website_text}

    User question: {user_question}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )

    answer = response.choices[0].message.content
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
