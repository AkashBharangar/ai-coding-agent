from langchain_core.messages import HumanMessage

from agent.graph import graph

print("=" * 60)
print("AI Coding Agent")
print("=" * 60)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=user_input)
            ]
        }, 
        config={
        "recursion_limit": 50
        }
    )

    print("\n Assistant:")
    print(result["messages"][-1].content)