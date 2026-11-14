from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6LtVOAyg2rLdj1isFCRZksP_dCQdkcHMwaY9SdOH4fbQQ"
)


interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words"
)

# print(response.output[0].content[0].text)
print(response.text)