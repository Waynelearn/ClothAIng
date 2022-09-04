import requests
import base64

def generate_img(text, num_images=3):

    URL = "https://oliver-hewlett-motors-fold.trycloudflare.com/dalle"

    data = {"text": text, "num_images": num_images}

    resp = requests.post(URL, json=data)

    for i in range(num_images):

        generated_img = resp.json()["generatedImgs"][i]


        with open(f"out_{i}.jpg", "wb") as f:
            f.write(base64.b64decode(generated_img))

if __name__=="__main__":
    generate_img("blue shirt white jeans")