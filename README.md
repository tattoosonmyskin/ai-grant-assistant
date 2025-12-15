# AI Grant Assistant

AI-powered platform for finding and applying to grants - empowering all through accessible grant opportunities.

## Overview

The AI Grant Assistant helps students and individuals discover grant opportunities that match their unique profile, educational background, and goals. The platform simplifies the grant search and application process through intelligent matching and automated document preparation.

## Features

- **Smart Matching**: AI-powered grant matching based on your profile
- **Easy Onboarding**: Multi-step profile creation with autosave
- **Grant Dashboard**: View your top matched grants with explanations
- **Application Support**: Automated packet generation for grant applications
- **Secure & Private**: Your data is encrypted and never sold

## Project Structure

```
ai-grant-assistant/
├── backend/          # FastAPI backend
│   ├── main.py       # API entry point with /ping endpoint
│   └── requirements.txt
├── frontend/         # Next.js frontend
│   ├── app/          # Next.js app directory
│   │   ├── page.tsx  # Home page
│   │   └── layout.tsx
│   └── package.json
├── docs/             # Documentation
│   ├── onboarding_flow.md
│   └── security-privacy.md
└── README.md
```

## Quick Start

### Prerequisites

- **Python 3.9+** for backend
- **Node.js 18+** and **npm** for frontend

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration (optional for basic setup)
   ```

5. **Run the backend server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

   The backend API will be available at: **http://localhost:8000**
   
   API documentation: **http://localhost:8000/docs**

### Frontend Setup

1. **Navigate to frontend directory** (in a new terminal)
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env.local
   # The default values should work for local development
   ```

4. **Run the development server**
   ```bash
   npm run dev
   ```

   The frontend will be available at: **http://localhost:3000**

### Verify Everything Works

1. **Test the backend**: Visit http://localhost:8000/ping
   - You should see: `{"message": "pong"}`

2. **Test the frontend**: Visit http://localhost:3000
   - You should see the AI Grant Assistant home page

## Development

### Backend Development

- **Auto-reload**: The server automatically reloads when you change code
- **API Docs**: FastAPI provides automatic interactive docs at `/docs`
- **CORS**: Configured to allow requests from `http://localhost:3000`

### Frontend Development

- **Hot Reload**: Changes appear instantly in the browser
- **TypeScript**: Full TypeScript support for type safety
- **CSS Modules**: Scoped styling with `.module.css` files

## Environment Variables

### Backend (.env)
```
BACKEND_URL=http://localhost:8000
```

### Frontend (.env.local)
```
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
```

The `NEXT_PUBLIC_` prefix makes the variable available in the browser.

## Documentation

- **[Onboarding Flow](docs/onboarding_flow.md)**: User onboarding process details
- **[Security & Privacy](docs/security-privacy.md)**: Security practices and privacy policy

## Technology Stack

### Backend
- **FastAPI**: Modern, fast Python web framework
- **Uvicorn**: ASGI server for running FastAPI
- **Python 3.9+**: Programming language

### Frontend
- **Next.js 15**: React framework with App Router
- **React 18**: UI library
- **TypeScript**: Type-safe JavaScript
- **CSS Modules**: Scoped component styling

## API Endpoints

### Current Endpoints

- `GET /ping`: Health check endpoint
  - Returns: `{"message": "pong"}`

### Coming Soon

- `POST /profiles`: Create user profile
- `GET /profiles/{id}`: Get user profile
- `GET /grants`: List available grants
- `GET /profiles/{id}/matches`: Get matched grants for user
- `POST /packets`: Generate application packet

## Contributing

Contributions are welcome! Please ensure your code:

- Follows existing code style
- Includes helpful comments for beginners
- Is tested before submission

## License

[Add your license here]

## Support

For questions or issues:
- Open an issue on GitHub
- Check the documentation in `/docs`

---

**Built with ❤️ for grant seekers everywhere**
