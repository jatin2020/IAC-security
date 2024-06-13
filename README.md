# IAC-security

Click Ops
Introduction
This Click Ops project utilizes a Python script to streamline the identification of Click Ops operations within a specific context. It effectively distinguishes between read and write operations based on input JSON code and leverages user agent information to refine the classification process.

Key Functionalities:

Read/Write Operation Detection: Analyzes the structure and content of the input JSON code. Employs custom logic or predefined patterns to accurately classify the operation type (read or write).
User Agent-Based Click Ops Identification: Extracts the user agent string from relevant sources (e.g., headers, environment variables). Compares the user agent against a whitelist of authorized tools (e.g., CircleCI, TF, CDK). Classifies an operation as Click Ops only if the user agent does not match the whitelist.

Installation
Prerequisites:

Ensure you have Python (version 3.x recommended) and the pip package manager installed on your system. You can verify this by running in your terminal:

python --version
pip --version
Clone or Download the project's source code using Git or download the project zip manually.

Pre run process :

We have included multiple test json files.
Before running the main iacproject.py , include the test case in line 42 of the code.
Initiate the run
Output:

The python code, will give the out put as Read Operation , Write Operation , Click ops
