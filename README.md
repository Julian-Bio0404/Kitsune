# Kitsune

![](https://img.shields.io/badge/python-v3.13.1-blue)
![](https://img.shields.io/badge/fastapi-v0.115.8-blue)
![](https://img.shields.io/badge/postgres-v17.2-blue)
![](https://img.shields.io/badge/mongodb-v7.0.15-blue)

## **Description**

Kitsune is the backend developed with FastAPI that uses Postgres and MongoDB to manage user authentication and the chat service, respectively.
It is built following a clean hexagonal architecture allowing clear decoupling between business logic and technological dependencies
and based on microservices and implements two fundamental microservices:

- **auth-service**: Responsible for user authentication (registration, login, and authentication validation), using Postgres.  
- **chat-service**: Manages the chat service between users, relying on MongoDB for message and conversation management.  

## **Microservices**  

### **auth-service**  
- **Description**: Manages user authentication, including signup, login, and authentication verification.  
- **Technology**: Developed with FastAPI and uses Postgres as the database management system.  
- **Features**:  
  - New user registration.  
  - Login.  
  - Management and validation of authentication tokens.  

### **chat-service**  
- **Description**: Provides a real-time chat service for user communication.  
- **Technology**: Implemented in FastAPI and uses MongoDB to store messages and manage conversations.  
- **Features**:  
  - Sending and receiving messages in real-time.
 
## **Installation**  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/tuusuario/kitsune.git  
   cd kitsune  
   ```  

2. **Create and activate a virtual environment** (optional but recommended):  
   ```bash
   python -m venv venv  
   source venv/bin/activate
   ```

3. **Create a `.env` file**  

    Use `.env.example` as a reference to create your `.env` file:  
  
    ```bash
    cp .env.example .env
    ```
    Then, edit the `.env` file and configure the necessary environment variables according to your setup.

4. **Build the images:**  
   ```bash
   docker compose -f local.yml build
   ```
5. **Run the services:**
   ```bash
   docker compose -f local.yml up -d
   ```
## API REST Documentation
You can test the API with Postman by following the documentation at: http://localhost:8000/docs#/

## API Websockets Documentation
To test the chat, you can follow these steps:
1. From Postman, you can create a WebSocket collection and query the following route:  
    ```bash
    ws://localhost:8001/api/v1/chat/channels/<user_id>/
    ```
    Where `<user_id>` is the ID of an existing user.

2. Add the Authorization header and press the Connect button located on the right side:
    <img width="857" alt="Screenshot 2025-02-24 at 11 16 33 PM" src="https://github.com/user-attachments/assets/a387f3fd-8300-4ec3-b645-e61bdfa83421" />

3. You will now be connected to send and receive messages. You can send a message using the structure shown in the example and press the Send button.
    <img width="859" alt="Screenshot 2025-02-24 at 11 16 56 PM" src="https://github.com/user-attachments/assets/f9fc48d1-1ac7-419e-8a43-231c07c4c4dc" />


