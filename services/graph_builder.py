from . import nodes
from .conditional_edges import should_continue
from langgraph.graph import StateGraph, START, END

workflow = StateGraph(nodes.State)
workflow.add_node("query_rewrite", nodes.query_rewrite)
workflow.add_node("first_tool_call", nodes.first_tool_call)
workflow.add_node("list_table_node", nodes.list_table_node)
workflow.add_node("model_schema_node", nodes.model_schema_node)
workflow.add_node("get_schema_node", nodes.get_schema_node)
workflow.add_node("generate_query_node", nodes.generate_query_node)
workflow.add_node("execute_query_node", nodes.execute_query_node)
workflow.add_node("finalize_answer", nodes.finalize_answer)

workflow.add_edge(START, "query_rewrite")
workflow.add_edge("query_rewrite", "first_tool_call")
workflow.add_edge("first_tool_call", "list_table_node")
workflow.add_edge("list_table_node", "model_schema_node")
workflow.add_edge("model_schema_node", "get_schema_node")
workflow.add_edge("get_schema_node", "generate_query_node")
workflow.add_edge("generate_query_node", "execute_query_node")
workflow.add_conditional_edges("execute_query_node", should_continue)
workflow.add_edge("finalize_answer", END)

app = workflow.compile()
