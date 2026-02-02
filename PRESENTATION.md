# Data Science Tool: "InsightStream Local"

## PROJECT TITLE
**InsightStream Local: Privacy-First Conversational Data Analyst**

## PROBLEM STATEMENT
In the modern data-driven landscape, extracting insights from raw data typically requires technical expertise in programming languages like Python or SQL. Business analysts and non-technical stakeholders often face significant bottlenecks:
1.  **Technical Barrier**: Dependency on data scientists for simple queries (e.g., "What were the sales last month?").
2.  **Privacy Concerns**: Hesitancy to upload sensitive corporate data to cloud-based AI tools (like ChatGPT) due to data leakage risks.
3.  **Time Efficiency**: Writing and debugging code for routine data exploration is time-consuming even for skilled professionals.

## DESCRIPTION
**InsightStream Local** is a secure, offline-capable analytical tool that allows users to "chat" with their data. By bridging a friendly web interface (Streamlit) with a local Large Language Model (Ollama/LLaMA 3), it translates natural language questions into executable Pandas code instantly. This solution empowers users to perform data cleaning, visualization, and deep analysis on CSV files without writing a single line of code, all while ensuring that sensitive data never leaves the local machine.

## SCOPE
The scope of this project is to develop an interactive, AI-powered data science assistant that democratizes data analysis for non-technical users. 

**Key Objectives:**
- **Simplified Data Interaction**: Enable users to upload datasets (CSV) and interact with them using natural language instead of writing complex Python/Pandas code.
- **Local AI Processing**: Utilize a generic local Large Language Model (via Ollama) to ensure data privacy and reduce reliance on external cloud APIs.
- **Automated Insight Generation**: Automate the process of generating data summaries, filtering, and analysis through a conversational interface.

## TECHNOLOGIES USED
This agent is built using a modern Python stack integrating web interfaces with generative AI.

- **Programming Language**: Python
- **User Interface**: Streamlit (for rapid web application development)
- **Data Manipulation**: Pandas (for efficient data handling and processing)
- **AI Agent Framework**: PandasAI (SmartDataframe for conversational data analysis)
- **LLM Runtime**: Ollama (for running large language models locally)
- **Language Model**: gemini-3-flash-preview:cloud (via Ollama)
- **Networking**: Requests (for API communication between the app and Ollama)

## PROTOTYPE DIAGRAM
*Architecture Flow:*

```mermaid
graph LR
    User[User] -- Uploads CSV --> UI[Streamlit UI]
    User -- "Ask Question (e.g., 'Show top 5 sales')" --> UI
    UI -- Raw Data --> Pandas[Pandas DataFrame]
    Pandas -- Data Context --> PandasAI[PandasAI Agent]
    PandasAI -- "Prompt + Schema" --> Connector[Custom OllamaLLM Connector]
    Connector -- HTTP Post --> Ollama[Ollama Server (Localhost:11434)]
    Ollama -- Generated Python Code --> Connector
    Connector -- Code --> PandasAI
    PandasAI -- "Executes Code on Data" --> Result[Analysis Result]
    Result -- Display --> UI
```

**Workflow:**
1. User uploads a CSV file via Streamlit.
2. The file is converted to a Pandas DataFrame.
3. User inputs a natural language query.
4. PandasAI constructs a prompt including the dataframe schema.
5. The `OllamaLLM` class sends this prompt to the local Ollama instance running `gemini-3-flash-preview:cloud`.
6. The model generates Python code to solve the query.
7. PandasAI executes the code and returns the result to the user.

## BASE PAPERS
*foundational concepts supporting this agent:*

1.  **"Attention Is All You Need" (Vaswani et al., 2017)**
    *   Basis for the Transformer architecture used in LLaMA 3.
2.  **"LLaMA: Open and Efficient Foundation Language Models" (Touvron et al., 2023)**
    *   Foundational paper for the LLaMA model family used in this project.
3.  **"Program Synthesis using Large Language Models"**
    *   Research regarding the capability of LLMs to generate executable code (Python/Pandas) from natural language specifications.

## REFERENCES
1.  **PandasAI Documentation**: https://docs.pandas-ai.com/
2.  **Streamlit Documentation**: https://docs.streamlit.io/
3.  **Ollama**: https://ollama.com/
4.  **Pandas Documentation**: https://pandas.pydata.org/docs/
5.  **Project Source**: Local workspace `Data science tool`
