## Loops, conditions and parsing

####Task 0: Create a SSH RSA key pair
[0-RSA_public_key.pub](0-RSA_public_key.pub) contains the public key of the generated SSH RSA key pair

####Task 1: For Best School loop
[1-for_best_school](1-for_best_school) is a Bash script that displays `Best School` 10 times using a `for` loop

####Task 2: While Best School loop
[2-while_best_school](2-while_best_school) is a Bash script that displays `Best School` 10 times using a `while` loop

####Task 3: Until Best School loop
[3-until_best_school](3-until_best_school) is a Bash script that displays `Best School` 10 times using the `until` loop

####Task 4: If 9, say Hi!
[4-if_9_say_hi](4-if_9_say_hi) is a Bash script that displays `Best School` 10 times using a `while` loop but also prints `Hi` after the 9th iteration

####Task 5: 4 bad luck, 8 is your chance
[5-4_bad_luck_8_is_your_chance](5-4_bad_luck_8_is_your_chance) is a Bash script that loops from 1 to 10 using a `while` loop and:
- displays `bad luck` for the 4th loop iteration
- displays `good luck` for the 8th loop iteration
- displays `Best School` for the other iterations

####Task 6: Superstitious numbers
[6-superstitious_numbers](6-superstitious_numbers) is a Bash script that displays numbers from 1 to 20 and:
- displays `4` and then `bad luck from China` for the 4th loop iteration
- displays `9` and then `bad luck from Japan` for the 9th loop iteration
- displays `17` and then `bad luck from Italy` for the 17th loop iteration

####Task 7: Clock
[7-clock](7-clock) is a Bash script that displays the time for 12 hours and 59 minutes:
- display hours from 0 to 12
- display minutes from 1 to 59

####Task 8: For ls
[8-for_ls](8-for_ls) is a Bash script that displays the content of the current directory:
- In a list format
- Where only the part of the name after the first dash is displayed
- Does not display hidden files

####Task 9: To file, or not to file
[9-to_file_or_not_to_file](9-to_file_or_not_to_file) is a Bash script that gives you information about the school file.
- Checks if the file exists and prints:
	- if the file exists: `school file exists`
	- if the file does not exist: `school file does not exist`
- If the file exists, prints:
	- if the file is empty: `school file is empty`
	- if the file is not empty: `school file is not empty`
	- if the file is a regular file: `school is a regular file`
	- if the file is not a regular file: (nothing)

####Task 10: FizzBuzz
[10-fizzbuzz](10-fizzbuzz) is a Bash script that displays numbers from 1 to 100.
- Displays `FizzBuzz` when the number is a multiple of 3 and 5
- Displays `Fizz` when the number is multiple of 3
- Displays `Buzz` when the number is a multiple of 5
- Otherwise, displays the number
- In a list format


####Task 11: Read and cut
[100-read_and_cut](100-read_and_cut) is a Bash script that displays the content of the file `/etc/passwd`.
It displays
- username
- user id
- Home directory path for the user

####Task 12: Tell the story of passwd
[101-tell_the_story_of_passwd](101-tell_the_story_of_passwd) is a Bash script that displays the content of the file `/etc/passwd`, using the `while` loop + IFS.
Format: `The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO`

####Task 13: Let's parse Apache logs
[102-lets_parse_apache_logs](102-lets_parse_apache_logs) is  a Bash script that displays the visitor IP along with the HTTP status code from an Apache log file.
- Format: IP HTTP_CODE
	- in a list format
- Uses `awk`
- Does not use `while`, `for`, `until` and `cut`

###Task 14: Dig the data
[103-dig_the-data](103-dig_the-data) is a Bash script that groups visitors by IP and HTTP status code, and displays this data.
- Format : `OCCURENCE_NUMBER IP HTTP_CODE`
	- In list format
	- Ordered from the greatest to the lowest number of occurrences
- Uses `awk`
