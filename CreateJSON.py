import json


def text_message(phone_number: int, message_content: str, preview_url: bool = False):
    return json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": f"+91{phone_number}",
        "type": "text",
        "text": {
            "preview_url": preview_url,
            "body": message_content
        }
    }, indent=4)


def reaction_message(phone_number: int, msg_id: str, emoji: str):
    return json.dumps({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": f"+91{phone_number}",
        "type": "reaction",
        "reaction": {
            "message_id": msg_id,
            "emoji": emoji
        }
    }, indent=4)


def media_message(phone_number: int, media_url: str = None, media_object_id: str = None):
    if media_url:
        return json.dumps({
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": f"+91{phone_number}",
            "type": "image",
            "image": {
                "link": media_url
            }
        }, indent=4)
    elif media_object_id:
        return json.dumps({
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": f"+91{phone_number}",
            "type": "image",
            "image": {
                "id": media_object_id
            }
        }, indent=4)


def location_message(phone_number: int, longitude_no: str, latitude_no: str, location_name: str, location_address: str):
    return json.dumps({
        "messaging_product": "whatsapp",
        "to": f"+91{phone_number}",
        "type": "location",
        "location": {
            "longitude": longitude_no,
            "latitude": latitude_no,
            "name": location_name,
            "address": location_address
        }
    }, indent=4)
