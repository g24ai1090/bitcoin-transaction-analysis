# Use Node.js as the base image
FROM node:18

WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy the rest of the app
COPY . .

# Build the React app
RUN npm run build

# Use a simple server to serve the frontend
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "3000"]
