FastAPI Photo & Video Sharing Application
A full-stack photo and video sharing platform built with FastAPI, demonstrating modern backend development practices including JWT authentication, database integration, and cloud media management.

🚀 Project Overview
This project is a production-ready API similar to early Instagram, featuring user authentication, media uploads, and social feed functionality. It covers everything from basic API concepts to advanced features like JWT tokens, database relationships, and cloud-based image/video processing.

✨ Key Features
User Authentication & Authorization: JWT-based authentication with FastAPI Users for secure login, registration, and session management

Media Management: Upload, store, and serve photos and videos using ImageKit for optimized delivery and transformations

Social Feed: Retrieve posts with user information, timestamps, and ownership verification

CRUD Operations: Create, read, update, and delete posts with proper authorization checks

Database Integration: SQLAlchemy ORM with async support for efficient database operations

API Documentation: Auto-generated interactive API docs with FastAPI's built-in Swagger UI

🛠️ Tech Stack
Backend
FastAPI: Modern, fast web framework for building APIs

Uvicorn: ASGI server for running the application

SQLAlchemy: Async ORM for database operations

FastAPI Users: Pre-built authentication and user management

Pydantic: Data validation using Python type annotations

Database
SQLite (development) with async support via aiosqlite

Easily swappable for PostgreSQL/MySQL in production

Media Storage
ImageKit: Cloud-based image and video API with AI-powered transformations

Automatic optimization, cropping, and format conversion

URL-based transformations for dynamic media manipulation

Frontend (Demo)
Streamlit: Simple web UI for testing and demonstration

📋 API Endpoints
Authentication
POST /auth/jwt/login - User login with JWT token generation

POST /auth/register - New user registration

GET /users/me - Get current user information

Posts
GET /feed - Retrieve all posts with user details

POST /upload - Upload photo/video with caption

DELETE /post/{post_id} - Delete post (owner only)

🔐 Security Features
JWT Token Authentication: Secure, stateless authentication

Password Hashing: User passwords securely hashed before storage

Owner-based Authorization: Users can only delete their own posts

Protected Endpoints: Dependency injection for authenticated-only routes

📊 Database Schema
User Model
UUID primary key

Email (unique)

Hashed password

Active/verified status

One-to-many relationship with posts

Post Model
UUID primary key

Caption (text)

File URL (from ImageKit)

File type (image/video)

File name

Created timestamp

Foreign key to user (owner)

🎨 ImageKit Integration
Media files are uploaded to ImageKit, which provides:

Automatic optimization: Reduced file sizes without quality loss

Dynamic transformations: Width, height, cropping via URL parameters

Video thumbnails: Extract frames from videos for previews

Text overlays: Add captions directly on images

Example transformation:

text
# Original image
https://ik.imagekit.io/your-id/image.jpg

# Resized with text overlay
https://ik.imagekit.io/your-id/tr:w-500,h-300,l-text,fs-100/image.jpg
🚀 Getting Started
Prerequisites
Python 3.8+

UV package manager (recommended) or pip

Installation
Clone the repository

bash
git clone <your-repo-url>
cd fastapi-photo-video-sharing
Initialize UV project

bash
uv init .
Install dependencies

bash
uv add fastapi uvicorn[standard] fastapi-users[sqlalchemy] imagekit python-dotenv aiosqlite
Set up environment variables
Create a .env file with your ImageKit credentials:

text
IMAGEKIT_PRIVATE_KEY=your_private_key
IMAGEKIT_PUBLIC_KEY=your_public_key
IMAGEKIT_URL=your_imagekit_url
Run the application

bash
uv run main.py
The API will be available at http://localhost:8000
Interactive docs at http://localhost:8000/docs

📁 Project Structure
text
app/
├── app.py          # Main FastAPI application and routes
├── db.py           # Database models and connection setup
├── schemas.py      # Pydantic schemas for request/response validation
├── users.py        # User authentication and JWT configuration
└── images.py       # ImageKit integration
main.py             # Application entry point
frontend.py         # Streamlit demo UI (optional)
.env                # Environment variables
🔄 Development Workflow
Define Pydantic schemas for input validation

Create database models with SQLAlchemy

Implement API endpoints with type hints

Add authentication dependencies for protected routes

Test with interactive docs at /docs endpoint

🎓 Learning Outcomes
This project demonstrates:

✅ RESTful API design principles

✅ Async/await patterns in Python

✅ Database relationships (one-to-many)

✅ JWT authentication flow

✅ File upload handling

✅ Cloud service integration

✅ Request/response validation

✅ Status code management

📚 Resources
FastAPI Documentation

FastAPI Users

ImageKit Python SDK

SQLAlchemy Async

🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

📝 License
This project is open source and available under the MIT License.

💡 Future Enhancements
Add comments and likes functionality

Implement user profiles with avatars

Add post editing capability

Implement pagination for feed

Add search and filtering options

Deploy to production (Docker + cloud hosting)

Add comprehensive test suite

Built with ❤️ using FastAPI and ImageKit

