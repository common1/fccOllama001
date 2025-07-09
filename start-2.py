import ollama

response = ollama.list()

# print(response)

# (variable) def chat(
#     model: str = '',
#     messages: Sequence[Mapping[str, Any] | Message] | None = None,
#     *,
#     tools: Sequence[Mapping[str, Any] | Tool | ((...) -> Any)] | None = None,
#     stream: Literal[False] = False,
#     think: bool | None = None,
#     format: JsonSchemaValue | Literal['', 'json'] | None = None,
#     options: Mapping[str, Any] | Options | None = None,
#     keep_alive: float | str | None = None
# ) -> ChatResponse
# Create a chat response using the requested model.

# === Chat example ===
res = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user", 
            "content": "Why is the sky blue?"
        },
    ],
)
# print(res["message"]["content"])

# === Chat example streaming ===
res = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user", 
            "content": "Why is the ocean so salty?"
        },
    ],
    stream=True,
)

# for chunk in res:
#     print(chunk["message"]["content"], end="", flush=True)

# ==================================================================================
# ==== The Ollama Python library's API is designed around the Ollama REST API ====
# ==================================================================================


# == Generate example ==
res = ollama.generate(
    model="llama3.2",
    prompt="why is the sky blue?",
)

# show
print(ollama.show("llama3.2"))