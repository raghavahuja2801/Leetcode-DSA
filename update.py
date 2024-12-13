import re

def update_readme(streak_file, readme_file):
    try:
        # Read the current streak value from the file
        with open(streak_file, "r") as sf:
            streak = sf.read().strip()

        # Read the content of the README file
        with open(readme_file, "r") as rf:
            content = rf.read()

        # Replace the streak badge URL with the updated streak value
        updated_content = re.sub(
            r"!\[Commit Streak\]\(https:\/\/img\.shields\.io\/badge\/Commit%20Streak-[0-9]*-brightgreen\?style=for-the-badge&labelColor=333333&color=00C851&label=Streak\)",
            f"![Commit Streak](https://img.shields.io/badge/Commit%20Streak-{streak}-brightgreen?style=for-the-badge&labelColor=333333&color=00C851&label=Streak)",
            content,
        )

        # Write the updated content back to the README file
        with open(readme_file, "w") as wf:
            wf.write(updated_content)

        print("README.md updated successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_readme("streak.txt", "README.md")
