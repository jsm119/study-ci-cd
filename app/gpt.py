def generate_prompt(characteristic: str):
    return """Suggest Nickname for an friend of mine in korean.

        Characteristics: 키가 크고 뚱뚱해
        Nicknames: 전봇대 돼지
        Characteristics: 키가 작고 달리기가 빨라
        Nicknames: 터보 땅콩
        Characteristics: 역도를 좋아하고 도마뱀을 좋아해
        Nicknames: 스내치 도마뱀
        Characteristics: {}
        Names:""".format(
        characteristic
    )
