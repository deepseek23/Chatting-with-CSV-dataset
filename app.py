import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.config import Config
from pandasai.llm.base import LLM
from pandasai.core.prompts.base import BasePrompt
from pandasai.agent.state import AgentState
import requests


class OllamaLLM(LLM):
    """LLM implementation that calls a local Ollama server (llama3)."""

    def __init__(
        self,
        model: str = "llama3",
        base_url: str = "http://localhost:11434",
        api_key: str | None = None,
    ) -> None:
        super().__init__(api_key=api_key)
        self._type = "ollama"
        self.model = model
        self.base_url = base_url.rstrip("/")

    @property
    def type(self) -> str:
        return self._type

    def call(self, instruction: BasePrompt, context: AgentState | None = None) -> str:
        """Send the prompt to Ollama's /api/chat endpoint."""
        prompt = instruction.to_string()
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        }
        try:
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()
            data = response.json()
            # Ollama /api/chat returns {"message": {"role": ..., "content": ...}, ...}
            return data.get("message", {}).get("content", "")
        except Exception as e:
            raise RuntimeError(f"Ollama call failed: {e}") from e


ollama_llm = OllamaLLM(model="llama3", base_url="http://localhost:11434")
config = Config(llm=ollama_llm)

st.title("PandasAI + Ollama (LLaMA3)")

uploaded_file = st.file_uploader("Upload CSV", type=['csv'])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head(3))

    df = SmartDataframe(data, config=config)
    prompt = st.text_area("enter your prompt")
    if st.button("Run"):
        if prompt:
            with st.spinner("getting response.."):
                    st.write(df.chat(prompt))
                