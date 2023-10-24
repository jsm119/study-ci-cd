import os

import openai

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        characteristic = request.form["characteristic"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(characteristic),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(characteristic):
    return """Suggest Nickname for an friend of mine in korean.

        Characteristics: 키가 크고 뚱뚱해
        Nicknames: 전봇대 돼지
        Characteristics: 키가 작고 달리기가 빨라
        Nicknames: 터보 땅콩
        Characteristics: 역도를 좋아하고 도마뱀을 좋아해
        Nicknames: 스내치 도마뱀
        Characteristics: {}
        Names:""".format(characteristic)


if __name__ == "__main__":
    app.run()
