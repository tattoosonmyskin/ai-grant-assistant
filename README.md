# AI Grant Assistant

AI-driven grant matching and application assistance platform for the empowerment of all.

## 🌟 Features

- **Smart Profile Creation**: Multi-step onboarding to capture your unique profile
- **AI-Powered Matching**: Intelligent grant matching based on persona, region, GPA, income, and other criteria
- **Top 5 Recommendations**: Get your top 5 grant matches with detailed explanations
- **Application Packets**: Generate professional grant application packets in PDF or DOCX format
- **Firestore Integration**: Cloud-based data storage with CRUD operations
- **RESTful API**: FastAPI backend with comprehensive endpoints
- **Modern UI**: Next.js frontend with responsive design

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- npm or yarn

### Local Development Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/tattoosonmyskin/ai-grant-assistant.git
cd ai-grant-assistant
```

#### 2. Set Up Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# For Firestore emulator (recommended for local development)
# Add this to your .env file:
# FIRESTORE_EMULATOR_HOST=localhost:8080
```

Create frontend environment file:

```bash
cp frontend/.env.local.example frontend/.env.local
```

#### 3. Start the Backend Server

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Start the backend server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend API will be available at `http://localhost:8000`

API documentation is available at `http://localhost:8000/docs`

#### 4. Start the Frontend Development Server

In a new terminal:

```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install

# Start the development server
npm run dev
```

The frontend will be available at `http://localhost:3000`

#### 5. (Optional) Load Seed Data

To populate the database with sample grants:

```bash
# Using curl
curl -X POST http://localhost:8000/grants/seed

# Or visit in browser
# http://localhost:8000/docs and use the /grants/seed endpoint
```

### Using Docker

You can also run the entire application using Docker Compose:

```bash
# Build and start all services
docker-compose up --build

# Backend: http://localhost:8000
# Frontend: http://localhost:3000
# Firestore Emulator: http://localhost:8080
```

## 📁 Project Structure

```
ai-grant-assistant/
├── backend/                  # FastAPI backend
│   ├── app/
│   │   ├── models.py        # Data models (Profile, Grant, Match)
│   │   ├── routes/          # API endpoints
│   │   │   ├── profiles.py
│   │   │   ├── grants.py
│   │   │   ├── matches.py
│   │   │   └── packets.py
│   │   └── services/        # Business logic
│   │       ├── firestore_service.py    # Firestore CRUD operations
│   │       ├── matching_service.py     # Grant matching engine
│   │       └── packet_service.py       # Packet generation
│   ├── main.py              # FastAPI application entry point
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile
├── frontend/                # Next.js frontend
│   ├── app/
│   │   ├── page.tsx         # Home page
│   │   ├── onboarding/      # Profile creation (multi-step)
│   │   ├── dashboard/       # Dashboard with top 5 matches
│   │   ├── grants/[id]/     # Grant detail page
│   │   └── packets/         # Packet generation page
│   ├── lib/
│   │   └── api.ts           # API client
│   ├── package.json
│   └── Dockerfile
├── data/
│   └── grants_seed.json     # Sample grant data
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI workflow
├── docker-compose.yml       # Docker Compose configuration
├── .env.example             # Example environment variables
└── README.md
```

## 🔧 API Endpoints

### Profiles
- `POST /profiles/` - Create a profile
- `GET /profiles/{profile_id}` - Get a profile
- `GET /profiles/` - List all profiles
- `PUT /profiles/{profile_id}` - Update a profile
- `DELETE /profiles/{profile_id}` - Delete a profile

### Grants
- `POST /grants/` - Create a grant
- `GET /grants/{grant_id}` - Get a grant
- `GET /grants/` - List all grants
- `PUT /grants/{grant_id}` - Update a grant
- `DELETE /grants/{grant_id}` - Delete a grant
- `POST /grants/seed` - Load seed data from JSON

### Matches
- `POST /matches/find/{profile_id}` - Find matches for a profile
- `POST /matches/refresh/{profile_id}` - Refresh matches (delete old, create new)
- `GET /matches/profile/{profile_id}` - Get all matches for a profile
- `GET /matches/{match_id}` - Get a match by ID
- `DELETE /matches/{match_id}` - Delete a match

### Packets
- `POST /packets/generate` - Generate application packet
- `GET /packets/download` - Download generated packet

## 🎯 Grant Matching Rules

The matching engine evaluates grants based on the following criteria:

1. **Persona Match** (20 points): Student, Researcher, or Entrepreneur
2. **Region Match** (15 points): Geographic eligibility
3. **GPA Requirement** (20 points): Minimum GPA threshold
4. **Minority Status** (15 points): Required or not required
5. **Disability Status** (15 points): Required or not required
6. **Income Level** (15 points): Low, Medium, or High
7. **Deadline**: Grants with expired deadlines are excluded

Each match includes a score (0-100) and a detailed explanation.

## 📄 Packet Generation

Generate professional application packets that include:
- Applicant information
- Selected grant details
- Eligibility criteria
- Application deadlines
- Organization information

Supported formats:
- **PDF**: Professional, print-ready documents
- **DOCX**: Editable Word documents

## 🧪 Running Tests

### Backend Tests

```bash
cd backend
# Tests can be added here
pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

## 🔐 Production Deployment

For production deployment with Firebase/Firestore:

1. Create a Firebase project at https://console.firebase.google.com
2. Enable Firestore Database
3. Download service account credentials
4. Set environment variable:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/serviceAccountKey.json
   ```
5. Remove or comment out `FIRESTORE_EMULATOR_HOST` in your `.env` file

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Built with FastAPI and Next.js
- Cloud storage with Firebase/Firestore
- Document generation with python-docx and ReportLab
