#!/usr/bin/env python
import sys
from research_crew.crew import MyProjectCrew 

def get_topic():
    """
    Prompt the user to input the research topic.
    """
    return input("Enter the topic for feature extraction research: ").strip()


def run():
    """
    Run the crew.
    """
    topic = get_topic()
    inputs = {
        'topic': topic  # Accept input from the console
    }
    MyProjectCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    topic = get_topic()
    inputs = {
        "topic": topic
    }
    try:
        MyProjectCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MyProjectCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    topic = get_topic()
    inputs = {
        "topic": topic
    }
    try:
        MyProjectCrew().crew().test(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py [run|train|replay|test] <args>")
        sys.exit(1)

    action = sys.argv[1]

    if action == "run":
        run()
    elif action == "train":
        train()
    elif action == "replay":
        replay()
    elif action == "test":
        test()
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)
