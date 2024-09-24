<div align="center">

# **ResearchCrew**

🤖🧠 **ResearchCrew**: CrewAI project to automates the process of researching, coding, and reviewing feature extraction techniques for a specified topic, especially for use in Scikit-learn transformers.

</div>

Welcome to the ResearchCrew project, powered by CrewAI. This project is designed to set up a multi-agent AI system that facilitates collaboration between agents to complete complex research tasks. It leverages CrewAI’s flexible framework to orchestrate these interactions, empowering your agents to work collectively toward a common goal.

## Installation

Ensure you have Python between >=3.10 and <=3.13 installed on your system. This project uses Poetry for dependency management, providing a streamlined setup process.

Step 1: Install Poetry
If you don't have Poetry installed, you can install it with:


```bash
pip install poetry
```

Step 2: Install Project Dependencies
Next, navigate to your project directory and install the dependencies by running the following command:

```bash
crewai install

```
This command locks the dependencies and installs them for your project using the CrewAI CLI.

## Customization

You can easily customize the behavior of your agents and tasks by editing the relevant configuration files:

Modify src/research_crew/config/agents.yaml to define and customize your agents.
Modify src/research_crew/config/tasks.yaml to define and customize your tasks.
Modify src/research_crew/crew.py to add your own logic, tools, and arguments for the agents.
Modify src/research_crew/main.py to handle custom inputs, such as allowing user inputs for research topics.
Note: You can now enter the research topic directly from the console, making it easy to run your project with different research subjects dynamically.

## Running the Project

To initiate your AI agents and begin task execution, run the following command from the root directory of the project:

```bash
crewai run

```
You will be prompted to enter a research topic from the console, allowing for dynamic task execution based on the topic you provide.

For example, you might input:

```bash
EEG Motor Imagery

```

This will execute the task pipeline and return the research results specific to that topic.

The ResearchCrew project consists of multiple AI agents, each with unique roles and tools designed for research and analysis. The agents work together to complete tasks, which are defined in config/tasks.yaml. These tasks guide the agents through the research process and prompt them to produce specific outputs.

Each agent's role, goal, and tools are defined in config/agents.yaml. You can customize their behavior by modifying this file to suit your research objectives.

## Key Components

Agents: Defined in agents.yaml, each agent has a specific role, such as researcher, coder, or reviewer. They are tasked with different parts of the research process.
Tasks: Defined in tasks.yaml, tasks are the actual research operations the agents will perform, like gathering information or synthesizing findings.

## Example Use Case

When you run the project, the agents can generate a report on various topics such as LLMs, EEG Motor Imagery, or any other field you specify. For example, the default setup will create a report.md file summarizing the findings of the agents on the selected research topic.

Support

For support or questions regarding the ResearchCrew project or CrewAI, feel free to reach out:

Visit our documentation
Check out the GitHub repository
Join our community on Discord
Chat with our documentation
Let’s unlock the potential of AI and multi-agent collaboration together with the power and flexibility of CrewAI.
