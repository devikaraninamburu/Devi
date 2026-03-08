# Real-Time Multilingual Voice AI Agent

This project implements a voice AI agent capable of booking clinical appointments.

## Features

- Voice-based appointment booking
- Appointment cancellation
- Multilingual support (English, Hindi, Tamil)
- Contextual session memory
- Real-time WebSocket communication

## Tech Stack

Python
FastAPI
Redis
WebSockets
Langdetect
gTTS

## Setup

Clone repository

pip install -r requirements.txt

Run backend

uvicorn backend.main:app --reload

Run websocket server

python websocket/socket_server.py

## Architecture

Speech → STT → Language Detection → LLM Agent → Appointment Engine → TTS

## Latency

STT: 120 ms  
Agent: 180 ms  
TTS: 100 ms  

Total: 400 ms
