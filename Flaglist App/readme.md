# NEAR Protocol Security Tool : Flagging Feature

Welcome to the NEAR Protocol Security Tool repository! This tool allows you to flag and search addresses for security purposes on the NEAR Protocol blockchain.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This NEAR Protocol Security Tool feature is a Node.js application that provides a simple interface to flag and search addresses. It helps users identify and report potentially malicious or vulnerable addresses on the NEAR Protocol blockchain.

## Installation
1. Clone this repository to your local machine.
 ``` git clone https://github.com/krypto-kiddo/Haven.git ```
2. Install the required dependencies by running the following command:
   ```
   npm install ioredis
   ```
3. Make sure you have Redis or Memurai installed and running on your machine. If you're using windows, I'd suggest using Memurai.
4. Update the Redis or Memurai connection details in the `app.js` file.
5. Start the server by running the following command in the home directory:
   ```
   node app.js
   ```

## Usage
Once the server is running, you can access the tool by visiting the provided URL (usually localhost:3000) in your web browser. The tool provides two main functionalities:

- **Flag/Report an Address**: Enter an address to flag/report it as potentially malicious or vulnerable. This information will be stored and can be searched later.
- **Search an Address**: Enter an address to search for any reported flags. The tool will display the number of times the address has been reported.

![image](https://github.com/krypto-kiddo/Haven/assets/97212160/6c267a47-ab7f-4933-8244-6c713b0997fd)

## Contributing
Contributions to this project are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. For major changes, please open an issue first to discuss the changes with the project maintainers.

## Special Mentions
This code is brought to you by @Krypto-Kidddo and @Sassycular. Special thanks to GPT-4. 
