#!/bin/bash

printf "Establecer el valor de <API_ID>\n"

printf "1. Prueba Create (POST)\n"

curl \
--header 'Content-Type: application/json' \
--data '{
 "id_number": "cf2ce02f-3e54-4509-927d-c9da9f29df8b",
 "city": "Kansas City",
 "country": "US",
 "first_name": "Taylor",
 "image_location": "clients/2024/01/27/cf2ce02f-3e54-4509-927d-c9da9f29df8b/1709092803.jpg",
 "last_name": "Swift",
 "zip_code": "64129"
}' \
-X POST "https://<API_ID>.execute-api.us-east-1.amazonaws.com/dev/client"

read
printf "2. Prueba Retrieve (GET)\n"
curl --location 'https://<API_ID>.execute-api.us-east-1.amazonaws.com/dev/client/cf2ce02f-3e54-4509-927d-c9da9f29df8b'

read
printf "3. Prueba Update (PUT)"
curl --location --request PUT 'https://<API_ID>.execute-api.us-east-1.amazonaws.com/dev/client' \
--header 'Content-Type: application/json' \
--data '{
 "id_number": "cf2ce02f-3e54-4509-927d-c9da9f29df8b",
 "city": "Kansas City",
 "country": "US",
 "first_name": "Travis",
 "image_location": "clients/2024/01/27/cf2ce02f-3e54-4509-927d-c9da9f29df8b/1709100040.jpg",
 "last_name": "Kelce",
 "zip_code": "64129"
}
'

read
printf "3.1. Prueba Retrieve (GET)\n"
curl --location 'https://<API_ID>.execute-api.us-east-1.amazonaws.com/dev/client/cf2ce02f-3e54-4509-927d-c9da9f29df8b'

read
printf "4. Prueba Delete (DELETE)"
curl --location --request DELETE 'https://<API_ID>.execute-api.us-east-1.amazonaws.com/dev/client/cf2ce02f-3e54-4509-927d-c9da9f29df8b'
