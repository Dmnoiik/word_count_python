**Word Counting Application**
Description
The Word Counting Application is a Python program designed to count the occurrences of a specific word in a text file. The program provides a user-friendly interface that allows users to select from available text files and input the word they want to count. It then analyzes the text file, filters out special characters, and accurately counts the occurrences of the specified word, both in a case-sensitive and case-insensitive manner.

The application includes the following features:

File Selection Menu: Users can choose from available text files using a menu-based interface, eliminating the need to manually type file names.

Word Counting: The program correctly counts the occurrences of a specified word within the selected text file.

Special Character Handling: Special characters like commas, periods, and newlines are removed before word counting to ensure accurate results.

Error Handling: The application gracefully handles scenarios such as selecting non-existent files or entering invalid input.

How to Use
Clone or download the repository to your local machine.

Add some text files for which count shall be provided

Open a terminal and navigate to the project directory.

Run the Python script using the command: python word_counter.py

Follow the prompts to select a text file and input the word you want to count.

The application will display the number of occurrences of the specified word in the selected file.

Sample Usage
sql
Copy code
Please select a file to count specific words in, out of:
1: sample_text1.txt
2: sample_text2.txt
3: sample_text3.txt
...
Enter the number corresponding to your choice: 1

Which word would you like to make a count for? apple

There are 3 occurrences of the word 'apple' in the selected file.
Dependencies
Python 3.x
Credits
This Word Counting Application was created by Dmnoiik.
