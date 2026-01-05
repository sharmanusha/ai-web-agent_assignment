Semi-Autonomous Web Interaction Agent

Project Overview
This project demonstrates a semi-autonomous web interaction agent that can observe a real website, make decisions at runtime, and perform browser actions. Instead of relying on fully hard-coded automation, the agent follows an observe–decide–act approach to handle dynamic web pages in a controlled and explainable way.

Problem Chosen
Modern websites frequently change their structure and behavior, which makes traditional scripted automation brittle and unreliable. The goal of this project is to design an agent that can adapt to the current page context and perform meaningful interactions based on observation and decision-making rather than fixed scripts.

Agent Architecture
Observer: Observes the current web page and extracts contextual information.
Decision Maker: Determines the next action based on the observation.
Actor: Executes browser interactions such as clicking elements.
Logger: Records agent behavior for traceability.
Main Controller: Orchestrates the overall workflow.

Decision-Making Logic
The agent follows an observe–decide–act loop to dynamically interact with the website and determine actions at runtime.

Website Used
https://books.toscrape.com

Output
The browser opens, observes the page, clicks a book, navigates to the book detail page, and logs actions for later analysis.

Limitations
The agent performs a single visible interaction, has limited error recovery, and uses simple decision logic.

Future Improvements
Support for multi-step workflows, improved error handling, deeper AI-based reasoning, and better state management across pages.

Conclusion
This project demonstrates a reliable and explainable semi-autonomous web interaction agent capable of observing a real website, making runtime decisions, and performing meaningful browser actions.
