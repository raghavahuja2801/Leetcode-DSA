import yaml
import os

# Load questions from YAML file
with open("questions.yaml", "r") as file:
    data = yaml.safe_load(file)

# Ensure the 'solutions' directory exists
os.makedirs("solutions", exist_ok=True)

# Loop through each question in the YAML data
for item in data:
    # Extract the question ID and title from the question field
    question_id = item["question"].split(".")[0]
    question_title = item["question"].split(".")[1].strip()

    # Format the filename as <question_id>-<question_title>.md
    filename = f"{question_id}-{question_title.replace(' ', '-').lower()}.md"
    
    # Define the solution file path
    solution_file_path = os.path.join("solutions", filename)
    
    # Create the solution file (blank)
    with open(solution_file_path, "w") as solution_file:
        solution_file.write(f"# Solution for {item['question']}\n\n")
        solution_file.write("## Problem Statement\n\n")
        solution_file.write(f"[Leetcode Link]({item['url']})\n\n")
        solution_file.write("## Solution\n\n")  
        solution_file.write("```python\n")
        
    
    # Update the 'solution' field in the YAML data with the correct file path
    item["solution"] = solution_file_path

# Save the updated YAML file with the new solution paths
with open("questions.yaml", "w") as file:
    yaml.dump(data, file, default_flow_style=False)

print("Solution files have been created and YAML file updated.")
