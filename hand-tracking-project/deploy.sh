#!/bin/bash

# Hand Tracking Project - Deployment Script
# This script helps automate building Docker image and pushing to GitHub

echo "=========================================="
echo "Hand Tracking Project - Deployment Helper"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print colored messages
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed. Please install Docker first."
    exit 1
fi
print_success "Docker is installed"

# Check if Git is installed
if ! command -v git &> /dev/null; then
    print_error "Git is not installed. Please install Git first."
    exit 1
fi
print_success "Git is installed"

echo ""
echo "What would you like to do?"
echo "1. Build Docker image"
echo "2. Test Docker container locally"
echo "3. Initialize Git and push to GitHub"
echo "4. Update existing GitHub repository"
echo "5. Complete deployment (Build + Push to GitHub)"
echo "6. Exit"
echo ""
read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        echo ""
        print_warning "Building Docker image..."
        docker build -t hand-tracker:latest .
        if [ $? -eq 0 ]; then
            print_success "Docker image built successfully!"
        else
            print_error "Docker build failed"
            exit 1
        fi
        ;;
    
    2)
        echo ""
        print_warning "Testing Docker container..."
        echo "Make sure XQuartz is running if on macOS!"
        echo ""
        read -p "Press Enter to continue or Ctrl+C to cancel..."
        
        # Try to get IP for macOS
        if [[ "$OSTYPE" == "darwin"* ]]; then
            IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
            echo "Your IP: $IP"
            echo "Running: xhost + $IP"
            xhost + $IP
            docker run -it --rm \
                --device=/dev/video0:/dev/video0 \
                -e DISPLAY=$IP:0 \
                -v /tmp/.X11-unix:/tmp/.X11-unix \
                hand-tracker:latest
        else
            # Linux
            xhost +local:docker
            docker run -it --rm \
                --device=/dev/video0:/dev/video0 \
                -e DISPLAY=$DISPLAY \
                -v /tmp/.X11-unix:/tmp/.X11-unix \
                hand-tracker:latest
        fi
        ;;
    
    3)
        echo ""
        print_warning "Setting up Git repository..."
        
        # Check if already initialized
        if [ -d .git ]; then
            print_warning "Git repository already initialized"
        else
            git init
            print_success "Git repository initialized"
        fi
        
        # Add files
        git add .
        print_success "Files staged for commit"
        
        # Commit
        read -p "Enter commit message (default: 'Initial commit'): " commit_msg
        commit_msg=${commit_msg:-"Initial commit: Hand tracking project with Docker support"}
        git commit -m "$commit_msg"
        print_success "Changes committed"
        
        # Add remote
        read -p "Enter your GitHub repository URL: " repo_url
        git remote add origin $repo_url
        print_success "Remote repository added"
        
        # Push
        git branch -M main
        print_warning "Pushing to GitHub..."
        git push -u origin main
        
        if [ $? -eq 0 ]; then
            print_success "Successfully pushed to GitHub!"
        else
            print_error "Failed to push to GitHub. Check your credentials and repository URL."
        fi
        ;;
    
    4)
        echo ""
        print_warning "Updating GitHub repository..."
        
        # Check for changes
        if [[ -z $(git status -s) ]]; then
            print_warning "No changes to commit"
        else
            git status
            echo ""
            read -p "Enter commit message: " commit_msg
            
            git add .
            git commit -m "$commit_msg"
            git push origin main
            
            if [ $? -eq 0 ]; then
                print_success "Successfully updated GitHub repository!"
            else
                print_error "Failed to push changes"
            fi
        fi
        ;;
    
    5)
        echo ""
        print_warning "Complete deployment starting..."
        
        # Build Docker
        echo "Step 1: Building Docker image..."
        docker build -t hand-tracker:latest .
        if [ $? -eq 0 ]; then
            print_success "Docker image built"
        else
            print_error "Docker build failed"
            exit 1
        fi
        
        # Git operations
        echo ""
        echo "Step 2: Git operations..."
        
        if [ ! -d .git ]; then
            git init
            print_success "Git initialized"
        fi
        
        git add .
        read -p "Enter commit message: " commit_msg
        commit_msg=${commit_msg:-"Update: Hand tracking project"}
        git commit -m "$commit_msg"
        
        # Check if remote exists
        if ! git remote | grep -q origin; then
            read -p "Enter your GitHub repository URL: " repo_url
            git remote add origin $repo_url
        fi
        
        git branch -M main
        git push -u origin main
        
        if [ $? -eq 0 ]; then
            print_success "Complete deployment successful!"
            echo ""
            echo "Your project is now:"
            echo "  ✓ Containerized with Docker"
            echo "  ✓ Published on GitHub"
        else
            print_error "GitHub push failed"
        fi
        ;;
    
    6)
        echo "Exiting..."
        exit 0
        ;;
    
    *)
        print_error "Invalid choice"
        exit 1
        ;;
esac

echo ""
print_success "Done!"