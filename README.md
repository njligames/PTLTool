# PTLTool
I made this tool to make it easier to find emails from a list of emails.
Use cases:
* Given a list of emails given to you on Slack, determine if they are in your POD.
 * Example
   
   1. Download the CSV file from your (Team Lead Dashboard)[https://canary.remotasks.com/en/remoadmin/expert-management]
   2. Copy the list of emails that are separated by whitespace from Slack
   3. Read the CSV file in...
   `JSON_DATA1=\`python3 read.py path/to/file.1csv\``
   4. Run intersect.py and put the results in your clipboard
   `pbpaste | python3 union.py ${JSON_DATA} > pbcopy`
   
* Between two or more lists of emails given to you on Slack, find which ones are in common.
 * Example
   ``` bash
   # 1. Download the CSV file from your (Team Lead Dashboard)[https://canary.remotasks.com/en/remoadmin/expert-management]
   # 2. Copy the list of emails that are separated by whitespace from Slack
   JSON_DATA1=`pbpaste | python3 read.py`
   # 3. Copy the list of emails that are separated by whitespace from Slack
   JSON_DATA2=`pbpaste | python3 read.py`
   # 4. Run intersect.py and put the results in your clipboard
   python3 union.py ${JSON_DATA} ${JSON_DATA2} > pbcopy
   ```

## Utilities
* Read - (`read.py`) - Reads in a CSV file, extracts the emails, and outputs the data to a JSON array.
  * Example
    ``` bash
    JSON_DATA=`python3 read.py path/to/file.csv`
    echo ${JSON_DATA}

    # Read from a list of emails separated by white space
    JSON_DATA=`pbpaste | python3 read.py`
    echo ${JSON_DATA}
    ```
  
* Union - (`union.py`) - Union between two datasets that were read in with `read.py`
  * Example
    ``` bash
    JSON_DATA1=`python3 read.py path/to/file.1csv`
    JSON_DATA2=`python3 read.py path/to/file2.csv`
    JSON_RESULT_DATA=`python3 union.py ${JSON_DATA1} ${JSON_DATA2}`
    echo ${JSON_RESULT_DATA}
    ```
  
* Intersection - (`intersection.py`) - Intersection between two datasets that were read in with `read.py`
  * Example
    ``` bash
    JSON_DATA1=`python3 read.py path/to/file.1csv`
    JSON_DATA2=`python3 read.py path/to/file2.csv`
    JSON_RESULT_DATA=`python3 intersection.py ${JSON_DATA1} ${JSON_DATA2}`
    echo ${JSON_RESULT_DATA}
    ```
  
* Daily Update - (`daily.py`) - Outputs a daily update that you can use on Slack.
  * Example
    ``` bash
    # The name of the file that was exported by the Team Lead Dashboard     
    FORMATTED_DATA=`python3 daily.py path/to/file.csv`
    echo ${FORMATTED_DATA} | pbcopy
    # The text is now in your clipboard.
    ```
* Write - (`write.py`) - Outputs the JSON array to a format you can use on Slack.
  * Example
    ``` bash
    FORMATTED_DATA=`python3 write.py`
    echo ${FORMATTED_DATA} | pbcopy
    # The text is now in your clipboard.
    ```
