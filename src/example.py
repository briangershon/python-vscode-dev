from typing import TypedDict

from IPython.display import Image, display
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph

# EXAMPLE LANGCHAIN
print("Example: Create a haiku with LangChain:\n\n")

llm = ChatOpenAI(temperature=0.9, model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_template("Create a haiku from:\n\n{content}")
chain = prompt | llm

response = chain.invoke({"content": "The quick brown fox jumps over the lazy dog."})
print(response.content)

# EXAMPLE LANGGRAPH
print(
    "\n\nExample: Determine if prompt is discussing colors or not with LangGraph:\n\n"
)


# Define the state of our graph
class State(TypedDict):
    prompt: str
    is_color: bool
    result: str


# Define our nodes
def ask_for_prompt(state: State) -> State:
    prompt = input("Please enter a prompt to indentify if it mentions a color or not: ")
    return {"prompt": prompt, "is_color": False, "result": ""}


def evaluate_prompt(state: State) -> State:
    prompt = state["prompt"]
    is_color = False

    llm = ChatOpenAI()
    prompt = ChatPromptTemplate.from_template(
        "Evaluate if this prompt discusses colors: '{prompt}'. Respond with 'Yes' or 'No'."
    )
    response = llm.invoke(prompt.format_prompt(prompt=state["prompt"]))
    if isinstance(response.content, str):
        is_color = response.content.strip().lower() == "yes"
    return {**state, "is_color": is_color}


def show_result(state: State) -> State:
    if state["is_color"]:
        result = f"The prompt '{state['prompt']}' contains a color!"
    else:
        result = f"The prompt '{state['prompt']}' does not contain a color."
    print(result)
    return {**state, "result": result}


# Create the graph
workflow = StateGraph(State)

# Add nodes
workflow.add_node("ask_prompt", ask_for_prompt)
workflow.add_node("evaluate", evaluate_prompt)
workflow.add_node("show_result", show_result)

# Add edges
workflow.add_edge("ask_prompt", "evaluate")
workflow.add_edge("evaluate", "show_result")
workflow.add_edge("show_result", END)

# Set entry point
workflow.set_entry_point("ask_prompt")

# Compile the graph
app = workflow.compile()

display(Image(app.get_graph().draw_png()))  # type: ignore

# Run the graph
for output in app.stream({"prompt": "", "is_color": False, "result": ""}):
    pass

# Example usage:
# This will run until a color is mentioned in the prompt
