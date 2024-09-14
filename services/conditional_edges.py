from .nodes import State
from langgraph.graph import END

def should_continue(state: State):
  if state['messages'][-1].content.startswith("Error:"):
    return "generate_query_node"
  else:
    return "finalize_answer"
