# CashToday API

## Detalles de la solución

Para la solución se estableció como prioridad aprovisionar un entorno funcional en la nube. Para el efecto se utilizó AWS Amplify, que permite crear APIs completas aprovechando los siguientes servicios:

- **CloudFormation** para la Infraestructura como Código (IaC)
- **Lambda** para la ejecución del código (serverless)
- **API Gateway** como puerta de entrada para el llamado a los servicios CRUD (API REST)
- **DynamoDB** como solución de base de datos NoSQL
- **IAM** para la gestión de permisos entre los servicios utilizados, antes mencionados

## Ejecución inicial

- Instalar **Amplify CLI** desde Node.js/NPM o ejecutable en el entorno que ejecutará las tareas CI/CD. Más información sobre la instalación de Amplify CLI en https://docs.amplify.aws/javascript/tools/cli/start/set-up-cli/
- Configurar las credenciales de acceso (Access Key ID y Secret Access Key) en el archivo `~/.aws/credentials`. El usuario asociado a las credenciales debe contar con los [permisos necesarios](https://docs.amplify.aws/javascript/tools/cli/start/set-up-cli/) para ejecutar los comandos de Amplify CLI.
- Descargar el código fuente (checkout) a repositorio local:

```bash
git clone https://github.com/iamgersoft/ct-api.git
```

- Inicializar el proyecto Amplify:

```bash
amplify init
```

- Crear el entorno. Para este caso se crea un entorno llamado `dev`:

```bash
amplify env add dev
```

- Hacer `push` del código fuente de la aplicación Python al entorno Amplify:

```bash
amplify push -y
```

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
