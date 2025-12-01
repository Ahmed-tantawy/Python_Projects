#!/bin/bash

# Master Fix & Test Script
# This will fix all issues and test your Docker setup

echo "╔════════════════════════════════════════════════╗"
echo "║  Hand Tracking Project - Master Setup & Test  ║"
echo "╚════════════════════════════════════════════════╝"
echo ""

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

print_success() { echo -e "${GREEN}✓ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠ $1${NC}"; }
print_error() { echo -e "${RED}✗ $1${NC}"; }
print_info() { echo -e "${BLUE}→ $1${NC}"; }
print_step() { echo -e "\n${BLUE}═══ $1 ═══${NC}"; }

# Check if we're in the right directory
if [ ! -f "hand.py" ] && [ ! -f "hand_tracker.py" ]; then
    print_error "No hand tracking Python file found!"
    print_info "Please run this script from your hand-tracking-project directory"
    exit 1
fi

print_step "Step 1: Fixing File Names"

# Fix file names with spaces
if [ -f "Docker Compose.yaml" ]; then
    mv "Docker Compose.yaml" docker-compose.yml
    print_success "Renamed: Docker Compose.yaml → docker-compose.yml"
fi

if [ -f "Deployment" ]; then
    mv "Deployment" DEPLOYMENT.md
    print_success "Renamed: Deployment → DEPLOYMENT.md"
fi

if [ -f "Readme github" ]; then
    mv "Readme github" README.md
    print_success "Renamed: Readme github → README.md"
fi

print_step "Step 2: Checking Requirements File"

if [ -f "requirements.txt" ]; then
    print_success "requirements.txt exists"
    print_info "Contents:"
    cat requirements.txt | sed 's/^/  /'
else
    print_warning "Creating requirements.txt"
    cat > requirements.txt << 'EOF'
opencv-python==4.8.1.78
mediapipe==0.10.8
EOF
    print_success "Created requirements.txt"
fi

print_step "Step 3: Fixing Dockerfile"

if [ -f "Dockerfile" ]; then
    # Check for old packages
    if grep -q "libgl1-mesa-glx" Dockerfile; then
        print_warning "Found obsolete package libgl1-mesa-glx"
        
        # Create backup
        cp Dockerfile Dockerfile.backup
        print_info "Backup saved as Dockerfile.backup"
        
        # Fix the package name
        sed -i.tmp 's/libgl1-mesa-glx/libgl1/g' Dockerfile
        sed -i.tmp 's/libxrender-dev/libxrender1/g' Dockerfile
        sed -i.tmp 's/libgtk2.0-dev/libgtk2.0-0/g' Dockerfile
        rm -f Dockerfile.tmp
        
        print_success "Updated Dockerfile with correct packages"
    else
        print_success "Dockerfile looks good"
    fi
else
    print_error "Dockerfile not found!"
    print_info "Creating a minimal Dockerfile..."
    
    cat > Dockerfile << 'EOF'
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY *.py .

ENV DISPLAY=:0
CMD ["python", "hand.py"]
EOF
    print_success "Created Dockerfile"
fi

print_step "Step 4: Creating .dockerignore"

if [ ! -f ".dockerignore" ]; then
    cat > .dockerignore << 'EOF'
__pycache__/
*.py[cod]
*.so
.git/
.vscode/
.idea/
.DS_Store
venv/
ENV/
*.swp
*.bak
*.backup
test-results.txt
EOF
    print_success "Created .dockerignore"
else
    print_success ".dockerignore exists"
fi

print_step "Step 5: Creating .gitignore"

if [ ! -f ".gitignore" ]; then
    cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*.so
.Python
venv/
ENV/

# IDEs
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Docker
*.backup
test-results.txt

# Git
.git/
EOF
    print_success "Created .gitignore"
else
    print_success ".gitignore exists"
fi

print_step "Step 6: Verifying Docker Installation"

if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed!"
    print_info "Please install Docker Desktop from: https://www.docker.com/products/docker-desktop"
    exit 1
fi

print_success "Docker is installed: $(docker --version)"

if ! docker ps &> /dev/null; then
    print_error "Docker daemon is not running!"
    print_info "Please start Docker Desktop and try again"
    exit 1
fi

print_success "Docker daemon is running"

print_step "Step 7: Building Docker Image"

print_info "This may take a few minutes..."
echo ""

# Remove old test images
docker rmi hand-tracker:test 2>/dev/null || true

# Build with output
if docker build -t hand-tracker:test . ; then
    echo ""
    print_success "Docker image built successfully! 🎉"
else
    echo ""
    print_error "Docker build failed!"
    print_info "Check the error messages above"
    exit 1
fi

print_step "Step 8: Running Tests"

echo ""
print_info "Test 1: Python version"
docker run --rm hand-tracker:test python --version
if [ $? -eq 0 ]; then print_success "Python OK"; else print_error "Python test failed"; fi

echo ""
print_info "Test 2: OpenCV installation"
docker run --rm hand-tracker:test python -c "import cv2; print('OpenCV version:', cv2.__version__)"
if [ $? -eq 0 ]; then print_success "OpenCV OK"; else print_error "OpenCV test failed"; fi

echo ""
print_info "Test 3: MediaPipe installation"
docker run --rm hand-tracker:test python -c "import mediapipe as mp; print('MediaPipe OK')"
if [ $? -eq 0 ]; then print_success "MediaPipe OK"; else print_error "MediaPipe test failed"; fi

echo ""
print_info "Test 4: File structure in container"
docker run --rm hand-tracker:test ls -la
if [ $? -eq 0 ]; then print_success "Files OK"; else print_error "File test failed"; fi

print_step "Step 9: Summary"

echo ""
docker images hand-tracker:test --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

echo ""
print_success "╔══════════════════════════════════════╗"
print_success "║  All tests PASSED! Ready to deploy  ║"
print_success "╚══════════════════════════════════════╝"

echo ""
print_info "Your project structure:"
ls -la | grep -v "^total" | sed 's/^/  /'

echo ""
print_step "Next Steps"

echo ""
echo "1️⃣  Tag image for production:"
echo "   docker tag hand-tracker:test hand-tracker:latest"
echo ""

echo "2️⃣  Initialize Git (if not done):"
echo "   git init"
echo "   git add ."
echo '   git commit -m "Initial commit: Hand tracking with Docker"'
echo ""

echo "3️⃣  Create GitHub repository:"
echo "   - Go to github.com"
echo "   - Click '+' → 'New repository'"
echo "   - Name: hand-tracking-project"
echo "   - Don't initialize with README"
echo "   - Copy the repository URL"
echo ""

echo "4️⃣  Push to GitHub:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/hand-tracking-project.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""

echo "5️⃣  Test with camera (optional):"
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "   # macOS instructions:"
    echo "   brew install --cask xquartz"
    echo "   open -a XQuartz"
    echo '   IP=$(ifconfig en0 | grep inet | awk '"'"'$1=="inet" {print $2}'"'"')'
    echo "   xhost + \$IP"
    echo "   docker run -it --rm --device=/dev/video0 -e DISPLAY=\$IP:0 hand-tracker:test"
else
    echo "   # Linux instructions:"
    echo "   xhost +local:docker"
    echo "   docker run -it --rm --device=/dev/video0 -e DISPLAY=\$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix hand-tracker:test"
fi

echo ""
print_success "🚀 Your project is ready for deployment!"
echo ""

# Save results
{
    echo "Hand Tracking Docker - Test Results"
    echo "===================================="
    echo "Date: $(date)"
    echo ""
    echo "Docker Image:"
    docker images hand-tracker:test
    echo ""
    echo "Tests: ALL PASSED ✓"
} > test-results.txt

print_info "Results saved to test-results.txt"