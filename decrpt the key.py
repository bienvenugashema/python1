import base64

# Given encrypted string
encoded_text = "rnGgpKUZJzNsFLtBOLx5R5t52niqh3MACVfdxYYiZ-EAgKLeq!TTO-zFb-wFPaDVZRYFwDZDEpvAtjUIxGNJVfIcyrFfJg0KowtLwuuPZHEgSht6Q76bgDvQStLETReoqZNR1Cuakrv6B0v6q9jxDpnVk6TYdiINSkTOCw2T35NhbsUvzkX--Zo948BgM34il4wosbNbPaCwaDvszMqeIA~~"

# Convert to standard Base64
encoded_text = encoded_text.replace("!", "+").replace("-", "/").replace("~", "=")

# Decode Base64
try:
    decoded_bytes = base64.b64decode(encoded_text)
    print("Decoded Bytes:", decoded_bytes)
except Exception as e:
    print("Decoding Error:", e)
