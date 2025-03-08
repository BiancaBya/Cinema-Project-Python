# 🎬 Cinema Management Application 

This Python-based application allows for the management of cinema operations, focusing on client management and movie scheduling. The system helps cinema administrators track clients, manage movie listings, and handle bookings in an organized, efficient manner.

## 📌 Key Features

- **Client Management:**
  - Allows the addition, modification, and removal of client details.
  - Track client bookings and view their past interactions with the cinema.

- **Movie Scheduling:**
  - Movies can be added, edited, or removed from the cinema’s schedule.
  - Allows management of movie screenings, including dates, times, and available seats.

- **Booking System:**
  - Clients can book tickets for available movie screenings.
  - Ensures that each booking is linked to the client and movie, preventing overbooking.

- **Search and Filter:**
  - Users can search for specific movies and filter based on genres, times, or availability.
  
## ⚙️ Technologies Used

- **Python:**
   Core programming language used to build the application logic and data management.
    
- **File Handling:**
   Application stores data in text files for persistence.

## 🌐 Architecture

- **Domain :**
  - Encapsulates the core business logic and entities such as **Client**, **Movie**, and **Booking**.
  - Represents the real-world data and behavior crucial for cinema management.

- **Repository Layer:**
  - Responsible for interacting directly with the file, ensuring data is stored, retrieved, and manipulated securely.
  - Provides an abstraction layer for data access, keeping the application’s business logic separate from the underlying data layer.

- **Service Layer:**
  - Coordinates the operations and integrates various domain functionalities.
  - Handles business rules, input validation, and transaction management, ensuring a smooth flow of operations.

- **Command Line Interface (CLI):**
  - Interacts with the user through the terminal, allowing administrators to perform tasks such as adding movies, registering clients, or making bookings.
  - A simple and efficient interface to control the application.
