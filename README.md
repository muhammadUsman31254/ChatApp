# README.md

# 🤖 AI Chat Assistant

A powerful conversational AI assistant built with LangGraph and Streamlit, featuring persistent chat threads, real-time streaming, and an intuitive web interface.

## ✨ Features

- 💬 **Real-time Chat**: Stream responses token-by-token for immediate feedback
- 🧵 **Thread Management**: Create multiple chat threads and switch between conversations
- 💾 **Persistent Memory**: Chat history persists across sessions using SQLite
- 🔄 **State Management**: Advanced conversation state handling with LangGraph
- 🎨 **Clean UI**: Intuitive Streamlit interface with sidebar navigation
- ⚡ **Fast Responses**: Powered by Groq's high-performance language models

## 🚀 Live Demo

**[Try it live on Streamlit Cloud](https://chat-app.streamlit.app)** 

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Framework**: LangGraph + LangChain
- **Language Model**: Groq (OpenAI GPT-OSS-120B)
- **Database**: SQLite with LangGraph checkpointing
- **Deployment**: Streamlit Cloud

## 📋 Prerequisites

- Python 3.10+
- Groq API key ([Get one here](https://console.groq.com/keys))

## 🔧 Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/muhammadUsman31254/ChatApp.git
   cd langgraph-chat-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Create .env file
   echo "GROQ_API_KEY=your_groq_api_key_here" > .env
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** and navigate to `http://localhost:8501`

## 🚀 Deployment

### Streamlit Cloud Deployment

1. **Fork this repository** to your GitHub account

2. **Go to [Streamlit Cloud](https://share.streamlit.io)**

3. **Create new app** and connect to your forked repository

4. **Add secrets** in Streamlit Cloud dashboard:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```

5. **Deploy** and your app will be live!

### Local Docker Deployment (Optional)

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 📁 Project Structure

```
langgraph-chat-app/
├── app.py                 # Main Streamlit application
├── workflow.py           # LangGraph workflow definition
├── requirements.txt      # Python dependencies
├── .streamlit/
│   ├── secrets.toml     # Environment variables 
├── .gitignore           # Git ignore file
└── README.md           # This file
```

## 🎯 How It Works

1. **LangGraph Workflow**: Defines a simple chat node that processes messages
2. **State Management**: Uses TypedDict to maintain conversation state
3. **Checkpointing**: SQLite database stores conversation history
4. **Streaming**: Real-time token streaming for better user experience
5. **Thread Management**: Each conversation gets a unique thread ID

## 🙏 Acknowledgments

- [LangGraph](https://langchain-ai.github.io/langgraph/) for the powerful agent framework
- [LangChain](https://langchain.com/) for the foundational tools
- [Streamlit](https://streamlit.io/) for the amazing web app framework  
- [Groq](https://groq.com/) for lightning-fast language model inference

## 📞 Support

If you have any questions or run into issues, please [open an issue](https://github.com/muhammadUsman31254/ChatApp/issues) on GitHub.

---

**Made with ❤️ using LangGraph and Streamlit**
