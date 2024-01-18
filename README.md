# PTLTool

## Utilities
* read - Reads in a CSV file, extracts the emails, and outputs the data to a JSON array.
  * Example
    ``` bash
    JSON_DATA=python3 read.py path/to/file.csv
    echo ${JSON_DATA}
    ```
  
* union - union between two 
* intersection
* daily update
* write - Outputs the JSON array to a format you can use on Slack.
  * Example
    ``` bash
    FORMATTED_DATA=python3 write.py
    echo ${FORMATTED_DATA} | pbcopy
    # the text is now in your clipboard.
    ```
