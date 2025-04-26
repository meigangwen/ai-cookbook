from openai import OpenAI

client = OpenAI()

# web search seem to require more expensive models, looks like gpt-40-mini is not being called here

# --------------------------------------------------------------
# Basic web search
# --------------------------------------------------------------

response = client.responses.create(
    model="gpt-4o-mini",
    tools=[
        {
            "type": "web_search_preview",
        }
    ],
    input="What are the best restaurants around de Dam?",
)

print(response.output_text)

# --------------------------------------------------------------
# Basic web search with location
# --------------------------------------------------------------

response = client.responses.create(
    model="gpt-4o-mini",
    tools=[
        {
            "type": "web_search_preview",
            "user_location": {
                "type": "approximate",
                "country": "NL",
                "city": "Amsterdam",
            },
        }
    ],
    input="What are the best restaurants around de Dam?",
)

print(response.output_text)
print(response.output[1].content[0].annotations)
print(response.output[1].content[0].annotations[0].url)