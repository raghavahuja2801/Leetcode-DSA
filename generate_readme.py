import yaml

# Load questions from YAML file
with open("questions.yaml", "r") as file:
    data = yaml.safe_load(file)

# Create the markdown table header
header = ["Data Type", "Question", "URL", "Solution", "Difficulty", "Tried", "Reviewed", "Important"]
table = ["| " + " | ".join(header) + " |", "|-" + "|-" * (len(header) - 1) + "|"]

# Add each row from the YAML data
for item in data:
    row = [
        item["data_type"],
        item["question"],
        f"[Link]({item['url']})",
        f"[Solution]({item['solution']})",  # Adding the solution link
        item["difficulty"],
        "✅" if item["tried"] else "❌",
        "✅" if item["reviewed"] else "❌",
        "✅" if item["important"] else "❌"
    ]
    table.append("| " + " | ".join(row) + " |")

# Convert the table to a markdown string
markdown_table = "\n".join(table)

# Write the markdown table to README.md
with open("table.md", "w") as f:
    f.write("# Leetcode Problems\n\n")
    f.write("Here is the list of Leetcode problems I have worked on:\n\n")
    f.write(markdown_table)

print("Markdown table has been written to table.md")
