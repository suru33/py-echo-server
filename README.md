# Py Echo Server

Simple echo server for testing, run `python3 main.py`

## Examples

1. ```shell
    curl --request POST \
    --url http://localhost:9000/ \
    --header 'Content-Type: application/json' \
    --data '{
    "date": "date"
    }'
    ```

   ```json
   {
     "date": "date"
   }
   ```

2. ```shell
   curl --request GET \
   --url http://localhost:9000/
   ```

   ```json
   {
     "int": 100,
     "str": "Hello World",
     "bool": false,
     "array": [
       1,
       2,
       3,
       4
     ],
     "obj": {
       "key": "value"
     }
   }
   ```
