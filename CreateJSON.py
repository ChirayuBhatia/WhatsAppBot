import json


def text_message(phone_number: int, message_content: str, preview_url: bool = False):
    mess = \
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": f"91{phone_number}",
            "type": "text",
            "text": {
                "preview_url": preview_url,
                "body": message_content
            }
        }
    return json.dumps(mess, indent=4)


def reaction_message(phone_number: int, msg_id: str, emoji: str):
    mess = \
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": f"91{phone_number}",
            "type": "reaction",
            "reaction": {
                "message_id": msg_id,
                "emoji": emoji
            }
        }
    return json.dumps(mess, indent=4)


def image_message(phone_number: int, image_url: str = None, ):
    if image_url:
        mess = \
            {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": f"91{phone_number}",
                "type": "image",
                "image": {
                    "link": image_url
                }
            }
        return json.dumps(mess, indent=4)


print(image_message(7992243804, "https://upload.wikimedia.org/wikipedia/commons/2/27/FG_1400_%C3%97_1400.jpg"))
