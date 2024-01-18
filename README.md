# PTLTool

## Utilities
* read - (`read.py`) - Reads in a CSV file, extracts the emails, and outputs the data to a JSON array.
  * Example
    ``` bash
    JSON_DATA=python3 read.py path/to/file.csv
    echo ${JSON_DATA}
    ```
  
* union - (`union.py`) - Union between two datasets that were read in with `read.py`
  * Example
    ``` bash
    JSON_DATA1=python3 read.py path/to/file.1csv
    JSON_DATA2=python3 read.py path/to/file2.csv
    JSON_RESULT_DATA=python3 union.py ${JSON_DATA1} ${JSON_DATA2}
    echo ${JSON_RESULT_DATA}
    ```
  
* intersection - (`intersection.py`) - Intersection between two datasets that were read in with `read.py`
  * Example
    ``` bash
    JSON_DATA1=python3 read.py path/to/file.1csv
    JSON_DATA2=python3 read.py path/to/file2.csv
    JSON_RESULT_DATA=python3 intersection.py ${JSON_DATA1} ${JSON_DATA2}
    echo ${JSON_RESULT_DATA}
    ```
  
* daily update
* write - (`write.py`) - Outputs the JSON array to a format you can use on Slack.
  * Example
    ``` bash
    FORMATTED_DATA=python3 write.py
    echo ${FORMATTED_DATA} | pbcopy
    # The text is now in your clipboard.
    ```
