import requests
responce = requests.get("https://coinmarketcap.com")
responce_text = (responce.text)
responce_parse = responce_text.split("<span>")
for parse_elem_1 in responce_parse:
    if parse_elem_1.startswith("$"):
        print(parse_elem_1)