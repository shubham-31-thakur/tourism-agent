# 🌏 ExploreIndia AI

## 🧠 Project Overview
**ExploreIndia AI** is a multi-agent AI system designed to help users explore India smartly.  
It integrates three specialized AI agents:
1. **Tourism Agent** – Provides details about tourist attractions, timings, and entry fees.  
2. **Travel Agent** – Suggests transport, routes, and budgets for trips.  
3. **Weather Agent** – Shares weather conditions, forecasts, and travel safety insights.  

This project uses **Gradient AI Agents (DigitalOcean)** with **FastAPI** for the web interface and **OpenAI client** for communication with the agent endpoints.

---

## 🚀 Features
- 🏛️ Get detailed info about Indian tourist places.  
- 🚗 Plan travel routes and compare transport options.  
- ☀️ Check weather before traveling.  
- 🔍 Powered by a custom knowledge base (JSON) uploaded to DigitalOcean Agent.  
- 💬 Simple web interface to ask questions interactively.  

---

## 🗂️ Project Structure
Tourism_Agent/
│
├── agent.py # Agent query and API connection logic
├── main.py # FastAPI backend + route setup
├── templates/
│ └── index.html # Web UI for user input/output
├── requirements.txt # Project dependencies
└── README.md # Project documentation

🔑 Setup & Configuration

Clone the Repository

git clone https://github.com/yourusername/Tourism_Agent.git
cd Tourism_Agent


Add Your Agent Credentials

You’ll need:

agent_endpoint → from DigitalOcean Gradient Agent

agent_access_key → your private key

Either set them as environment variables:

set AGENT_ENDPOINT=https://your-agent-endpoint.agents.do-ai.run/api/v1/
set AGENT_ACCESS_KEY=your-access-key


Or hardcode them in agent.py for testing (⚠️ not recommended for production).

(Optional) Add Your Knowledge Base

Upload a JSON file containing Indian tourist data to your Gradient AI agent’s knowledge base via the web dashboard.

▶️ How to Run the Project Locally

Start the FastAPI server:

uvicorn main:app --reload


Open your browser and go to:

http://127.0.0.1:8000/


Use the Web Interface:

Field 1 → “Agent Instructions” (paste system prompt)

Field 2 → “User Query” (e.g., Tell me about Amber Fort in Jaipur)

💡 Example Prompts

Tourism Agent

Instructions:

You are a Tourism Agent specialized in Indian cities. 
Provide information about tourist attractions, entry fees, timings, and highlights.


User Query:

Tell me about the top attractions in Udaipur.

Weather Agent

Instructions:

You are a Weather Agent specialized in Indian cities.
Provide current weather, temperature, and travel advice.


User Query:

Will it rain in Mumbai tomorrow?

🧩 Future Work

Integrate all three agents (Tourism, Travel, Weather) with function routing.

Add budget-based travel suggestions.

Implement map visualization for routes.

Support multilingual queries (Hindi, Marathi, etc.)

🏁 Hackathon Note

This prototype is part of a hackathon project aimed at showcasing multi-agent collaboration using DigitalOcean Gradient AI.

| Name    | Role                    |
| ------- | ----------------------- |
| Shubham | Tourism Agent Developer |
| Shreyas | Travel Agent Developer  |
| Saurabh | Weather Agent Developer |
