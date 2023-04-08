import Replicate from "replicate";

const replicate = new Replicate({
  auth: process.env.REPLICATE_API_TOKEN,
});

const output = await replicate.run(
  "tstramer/midjourney-diffusion:436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b",
  {
    input: {
      prompt: "a photo of an astronaut riding a horse on mars"
    }
  }
);