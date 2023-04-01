# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the required packages
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \
    && apt-get -y install git

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Expose port 80 on the container
EXPOSE 80

# Set the environment variable for the OpenAI API key
ENV CHATGPT_API_KEY=${CHATGPT_API_KEY}
ENV DISCORD_ACCOUNT_TOKEN=${DISCORD_ACCOUNT_TOKEN}
ENV DISCORD_SERVER_ID=${DISCORD_SERVER_ID}
ENV DISCORD_CHANNEL_ID=${DISCORD_CHANNEL_ID}
ENV MIDJOURNEY_DOWNLOAD_BOT_TOKEN=${MIDJOURNEY_DOWNLOAD_BOT_TOKEN}
ENV DATABASE_URL=${DATABASE_URL}