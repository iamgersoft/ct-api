# CashToday API

## Detalles de la solución

Se utilizó AWS Amplify, que permite crear APIs completas aprovechando los siguientes servicios:

- _CloudFormation_ para la Infraestructura como Código (IaC)
- _Lambda_ para la ejecución del código (serverless)
- _API Gateway_ como puerta de entrada para el llamado a los servicios CRUD (API REST)
- _DynamoDB_ como solución de base de datos NoSQL
- _IAM_ para la gestión de permisos entre los servicios utilizados, antes mencionados

## CI/CD

Identificar cambios en el código desde

- GitHub Actions
- Amazon CodeCommit

Para cada cambio, se ejecuta el comando

```bash
amplify push -y
```

## Ventajas de la solución

- Se orienta a las soluciones serverless de AWS
- Se optó por el uso de Flask como framework para los endpoints CRUD, lo que facilita una eventual migración a un entorno de contenedores de ser necesaria
- El uso de Amplify permite la creación de una aplicación base con IaC, tablas de DynamoDB, una función Lambda con un handler "esqueleto", así como un esquema de permisos necesarios para ejecutar la aplicación, lo que reduce la cantidad de _boilerplate code_ a cargo del programador

## Consideraciones

### Tabla DynamoDB

- El índice de la tabla es el número de identificación del cliente (`id_number`)
- A la tabla se agregó un GSI (Global Secondary Index) sobre los atributos `last_name` (_partition key_) y `first_name` (_sort key_) para facilitar la búsqueda de registros a partir del criterio de nombre del cliente en lugar de la búsqueda por defecto (sobre el número de identificación)
- Es posible agregar más índices que obedezcan a otros criterios de búsqueda; no obstante, el diseño debe considerar un eventual aumento de costos de tener la información almacenada y el acceso a consultas sobre dichos índices (sobre todo si los índices se crean con todos los atributos proyectados)

### CI/CD

- Considerar la instalación de _Amplify CLI_ desde Node.js/NPM o ejecutable en el entorno que ejecutará las tareas CI/CD. Más información sobre la instalación de Amplify CLI en https://docs.amplify.aws/javascript/tools/cli/start/set-up-cli/

### Pruebas

- Se incluye el script `test.sh` para validar las 4 operaciones CRUD. Solicitar URL del entorno donde se encuentra publicado.
