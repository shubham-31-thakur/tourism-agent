# # import os
# # import json
# # from openai import OpenAI

# # agent_endpoint = "https://hkuuczxyqrmn2xhh6nuslsfe.agents.do-ai.run/api/v1/"

# # agent_access_key = "NBt6OQaL36JMYM9Z_Zp5mMFpiV7iB8Kp"

# # # Your system instructions
# # user_prompt = """
# # You are a Tourism Agent specialized in Indian cities.
# # Answer queries about tourist attractions, entry fees, timings, and highlights from your knowledge base.
# # If a user asks about transport, budget, or weather, politely respond that this is handled by the Travel or Weather Agent.
# # Respond clearly in short JSON or text format, depending on the user query.
# # """

# # user_query = "Tell me about the top attractions in Jaipur."

# # if __name__ == "__main__":
# #     client = OpenAI(
# #         base_url = agent_endpoint,
# #         api_key = agent_access_key,
# #     )

# #     response = client.chat.completions.create(
# #         model = "n/a",
# #         messages = [
# #             {"role": "system", "content": user_prompt},
# #             {"role": "user", "content": user_query}
# #         ],
# #         extra_body = {"include_retrieval_info": True}
# #     )

# #     # Prints response's content
# #     for choice in response.choices:
# #         print(choice.message.content)
    
# #     response_dict = response.to_dict()

# #     print("\nFull retrieval object:")
# #     print(json.dumps(response_dict["retrieval"], indent=2))


# import os
# import json
# from openai import OpenAI

# agent_endpoint = "https://hkuuczxyqrmn2xhh6nuslsfe.agents.do-ai.run/api/v1/"
# agent_access_key = "NBt6OQaL36JMYM9Z_Zp5mMFpiV7iB8Kp"

# # tourism_system_prompt = """
# # You are a Tourism Agent specialized in Indian cities.
# # Answer queries about tourist attractions, entry fees, timings, and highlights from your knowledge base.
# # If a user asks about transport, budget, or weather, politely respond that this is handled by the Travel or Weather Agent.
# # Respond clearly in short JSON or text format, depending on the user query.
# # """

# tourism_system_prompt = """
# You are a smart Tourism Agent specialized in Indian cities and attractions. 

# Your job:
# 1. Answer queries about tourist places in India, including:
#    - Name of the attraction
#    - Description
#    - Highlights
#    - Timings
#    - Entry fee
#    - Best time to visit
# 2. Use the knowledge base (JSON) for all information.
# 3. If the user asks about transport, travel costs, budget, or weather, politely respond that these are handled by the Travel or Weather Agent.
# 4. Respond in clear text or simple JSON format depending on the user query.
# 5. Be concise, informative, and friendly.
# """


# # Initialize client once
# client = OpenAI(base_url=agent_endpoint, api_key=agent_access_key)

# # Tourism agent function
# def tourism_agent(query):
#     response = client.chat.completions.create(
#         model="n/a",
#         messages=[
#             {"role": "system", "content": tourism_system_prompt},
#             {"role": "user", "content": query}
#         ],
#         extra_body={"include_retrieval_info": True}
#     )
#     return response.choices[0].message.content

# # Travel agent function (stub for now)
# def travel_agent(query):
#     return f"Travel Agent would handle: {query}"

# # Route query to appropriate agent
# def route_query(user_query):
#     query = user_query.lower()
#     if any(word in query for word in ["weather", "rain", "temperature"]):
#         return "Weather Agent not ready yet."
#     elif any(word in query for word in ["travel", "transport", "flight", "bus", "train", "budget", "cost"]):
#         return travel_agent(user_query)
#     else:
#         return tourism_agent(user_query)

# # Optional: allow testing directly
# if __name__ == "__main__":
#     test_query = "Tell me about Jaipur attractions"
#     print(route_query(test_query))

from openai import OpenAI

agent_endpoint = "https://hkuuczxyqrmn2xhh6nuslsfe.agents.do-ai.run/api/v1/"
agent_access_key = "NBt6OQaL36JMYM9Z_Zp5mMFpiV7iB8Kp"

client = OpenAI(base_url=agent_endpoint, api_key=agent_access_key)

def tourism_agent(query, system_prompt):
    """
    Calls the Gradient AI Tourism Agent endpoint with:
    - user query
    - system instructions (prompt)
    """
    response = client.chat.completions.create(
        model="n/a",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ],
        extra_body={"include_retrieval_info": True}
    )
    return response.choices[0].message.content
