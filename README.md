Rememberme.py is a program I made for fun that allows you to give your local ollama installed ai models persistent memories through .txt files stored in a database called Ai_conversations. 
Currently only supports linux

HOW TO USE: 
1. Install ollama and choose a model. Then download the .py file from github to whereever on your computer
2. Open your terminal and navigate to the directory the .py file is in. run the command "python Rememberme.py"
3. After the program loads your chosen ai model (ollama does not need to be running Rememberme will launch ollama for you) you can now talk to the ai through the terminal. Type "remember" with no quotations to feed your ai the conversation history (This may take longer depending on how big the file containing the history is, in most cases with REALLY long histories it takes about 15-25ish seconds)
4. The program will record your history with the ai, at any time type "exit" without quotes to exit the program.

Commands will not run in the context of a conversation. you have to type ONLY "remember" or "exit" to have the commands run. Try asking your ai to remember a word or to summarize your conversation history.

KNOWN BUGS
1.) Sometimes the text marker for the AI's response will double or even triple then dissapear the next response going back to normal. 
Ex: AI: Hi, how may I help you today ------> AI:AI:AI: Sure thing! 
2.) Is not compatible with a web UI.

Feel free to do whatever you want with the code and to let me know of any bugs that are not known
