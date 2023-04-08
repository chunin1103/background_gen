import replicate
output = replicate.run(
    "tstramer/midjourney-diffusion:436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b",
    input={
    "prompt": "Kobe Bryant (basketball legend) holding a pink lighsaber (starwar), riding a black horse on mars, 8k, closeup",
    "width":1024,
    "height":512,
    "scheduler": "K_EULER",
    "num_outputs": 1,
    "prompt_strength":0.8,
    }
)
print(output)