# LangGraph Chatbot

A simple conversational AI chatbot built with **LangGraph**, **LangChain**, **Groq**, and **Streamlit**.

This project demonstrates how to build an LLM-powered chatbot using a graph-based workflow. It includes conversation state management, thread-based checkpointing, and real-time response streaming.

## Features

- Connects to a Groq-hosted LLM.
- Maintains conversation history.
- Uses LangGraph nodes and edges.
- Uses graph state to manage messages.
- Supports thread-based checkpointing.
- Streams AI responses in real time.
- Provides an interactive Streamlit interface.
- Keeps API keys outside the source code.

## Technologies Used

- Python
- LangGraph
- LangChain
- Groq
- Streamlit
- python-dotenv

## Project Structure

```text
LangGraph_Chatbot/
│
├── app.py
├── backend.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How the Project Works

The chatbot follows this workflow:

```text
User Input
    ↓
Streamlit Interface
    ↓
LangGraph State
    ↓
Chat Node
    ↓
Groq LLM
    ↓
Assistant Response
    ↓
Updated Conversation History
```

When a user sends a message:

1. Streamlit receives the user input.
2. The input is converted into a human message.
3. The message is passed to the LangGraph workflow.
4. The graph sends the conversation messages to the LLM.
5. The LLM generates a response.
6. The response is added to the graph state.
7. Streamlit displays the response to the user.
8. The response is streamed in real time.

## LangGraph Concepts Used

### State

The chatbot state stores the messages exchanged between the user and the assistant.

The state is updated whenever a new user message or AI response is generated. This allows the chatbot to maintain the context of the conversation.

### Nodes

A node represents a step in the chatbot workflow.

This project contains a chat node that:

1. Receives the current conversation state.
2. Sends the messages to the Groq LLM.
3. Returns the generated AI response.

### Edges

Edges define the execution flow between nodes.

The current graph follows this flow:

```text
START → chat_node → END
```

- `START` begins graph execution.
- `chat_node` processes the conversation.
- `END` completes the execution.

### Persistence

The project uses a thread-based checkpointer to store the graph state during execution.

A `thread_id` identifies a conversation. When the same thread ID is used, LangGraph can associate new messages with the corresponding conversation.

The current project uses in-memory persistence, which is useful for learning and testing. For production applications, a database-backed checkpointer should be used.

### Response Streaming

The chatbot streams the response while the LLM is generating it.

This gives users a faster and smoother experience because they do not need to wait for the complete response before seeing any output.

## Requirements

Before running the project, make sure you have:

- Python 3.10 or newer.
- Git.
- A Groq API key.
- An internet connection.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/LangGraph_Chatbot.git
```

Replace `YOUR_USERNAME` with your GitHub username.

Move into the project directory:

```bash
cd LangGraph_Chatbot
```

### 2. Create a Virtual Environment

On Windows:

```powershell
python -m venv myenv
myenv\Scripts\activate
```

On macOS or Linux:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you need to create the `requirements.txt` file, add:

```text
streamlit
langgraph
langchain
langchain-core
langchain-groq
python-dotenv
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your actual Groq API key.

Do not upload the `.env` file to GitHub.

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## Git Configuration

Create a `.gitignore` file in the project root:

```gitignore
# Virtual environments
myenv/
venv/
.venv/
env/

# Python cache
__pycache__/
*.py[cod]

# Environment variables
.env
.env.*

# Streamlit secrets
.streamlit/secrets.toml

# IDE files
.vscode/
.idea/

# Operating system files
.DS_Store
Thumbs.db
```

Do not upload these files or folders:

```text
myenv/
venv/
.env
__pycache__/
```

Virtual environments contain installed packages and can add thousands of unnecessary files to your GitHub repository.

## Push the Project to GitHub

If Git has not been initialized:

```bash
git init
```

Add the project files:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Add LangGraph chatbot"
```

Rename the branch to `main`:

```bash
git branch -M main
```

Add your GitHub repository:

```bash
git remote add origin https://github.com/YOUR_USERNAME/LangGraph_Chatbot.git
```

Push the project:

```bash
git push -u origin main
```

For future updates, use:

```bash
git add .
git commit -m "Update chatbot"
git push
```

## Deploy on Streamlit Community Cloud

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Sign in with GitHub.
4. Click **Create app**.
5. Select your repository.
6. Select the `main` branch.
7. Set the main file path to `app.py`.
8. Click **Deploy**.

After creating the application, add the Groq API key through the Streamlit Cloud Secrets section:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Do not commit the API key to GitHub.

## Persistence Limitation

This project uses in-memory persistence.

This means that conversation state may be lost when:

- The application restarts.
- The server shuts down.
- The application is redeployed.
- The hosting environment clears its memory.

For a production-ready application, use a persistent storage system such as:

- PostgreSQL.
- Redis.
- SQLite.
- MongoDB.
- A cloud database.

You should also generate a unique thread ID for each user or conversation.

## Possible Improvements

- Add a clear-chat button.
- Support multiple chat sessions.
- Add user authentication.
- Store conversations in a database.
- Add a conversation sidebar.
- Add custom chatbot instructions.
- Add document upload support.
- Build a Retrieval-Augmented Generation pipeline.
- Integrate Qdrant or another vector database.
- Add LangSmith monitoring.
- Add error handling and rate-limit handling.
- Improve the Streamlit interface.

## Learning Outcomes

By building this project, I learned:

- How to connect an application with an LLM.
- How to build a workflow using LangGraph.
- How nodes and edges work in a graph.
- How to manage messages using graph state.
- How thread-based persistence works.
- How to stream LLM responses.
- How to build an AI interface with Streamlit.
- How to manage API keys securely.
- How to deploy a Python project using GitHub and Streamlit Cloud.

## Security

- Never hardcode API keys in source files.
- Never commit the `.env` file.
- Never upload your virtual environment.
- Use Streamlit Secrets for deployed applications.
- Rotate your API key if it is exposed.
- Use unique thread IDs for multiple users.

## Future Roadmap

- [ ] Add multiple conversation threads.
- [ ] Add persistent database storage.
- [ ] Add user authentication.
- [ ] Add a clear-chat feature.
- [ ] Add document upload support.
- [ ] Build a RAG chatbot.
- [ ] Integrate Qdrant vector database.
- [ ] Add LangSmith tracing.
- [ ] Improve the user interface.
- [ ] Deploy a production-ready version.

## Author

This project was created as a learning project while exploring LangGraph, LangChain, LLM applications, state management, persistence, streaming, and AI application deployment.

## License

This project is available for educational and learning purposes.
