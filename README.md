# IBM Quantum Challenges

My repository to store my tries at IBM Quantum Challenges.

## Results

| Challenge   | Labs done | Last lab progress | Time Left |
| ----------- | :-------: | :---------------: | --------: |
| Spring 2023 | 3/5       | Lab 3, 100%       | Ongoing   |

## Setup

**Last updated for Spring 2023 Challenge**

*It is highly advised to use a venv*

Simply run `pip install -r requirements.txt` to install all required python package. This should allow you to run everyhting required.

If you also wish to use my repo as a template for the next challenges, you need to do some extra setuping.
First, export your environnement variables :

- `QXToken=YOUR_IBM_QUANTUM_TOKEN`
- `QC_GRADING_ENDPOINT=https://qac-grading.quantum-computing.ibm.com`
- `QXAuthURL=https://auth.quantum-computing.ibm.com/api `

and set your hub, group and project in the `provider_info` file.