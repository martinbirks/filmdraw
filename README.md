# Film draw

A quick script for generating a pick of categories for film club.

## Usage

`filmdraw.py [-h] [--count COUNT] [--members MEMBERS] [--categories CATEGORIES] [--previous PREVIOUS] [--output OUTPUT]`

 * count - the number of categories to pick this round
 * members - name of a file containing a list of film club member names, each on a new line
 * categories - name of a file containing a list of film categories, each on a new line
 * previous - name of a file containing a list of film categories previously picked by a member. The list should be comma seperated with the line of the list corresponding to the line in the members file.
 * output - name of a file to write the new version of the "previous" file after the pick has been made. All contents will be overwritten.

The filmdraw may fail if it reaches a deadlock. In that case try running again and check you have enough categories and few enough previous for everyone.
