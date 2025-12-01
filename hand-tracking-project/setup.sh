#!/bin/bash

# Setup script for hand tracking project
echo "=========================================="
echo "Hand Tracking Project - Setup Script"
echo "=========================================="
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

print_success() { echo -e "${GREEN}✓ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠ $1${NC}"; }
print_error() { echo -e "${RED}✗ $1${NC}"; }

echo "Checking project files..."
echo ""

# Check for Python files
if [ -f "hand.py" ]; then
    print_success "Found: hand.py"
elif [ -f "hand_tracker.py" ]; then
    print_success "Found: hand_tracker.py"
elif [ -f "hand_tracker_enhanced.py" ]; then
    print_success "Found: hand_tracker_enhanced.py"
else
    print_error "No hand tracking Python file found!"
    echo "Please ensure you have one of these files:"
    echo "  - hand.py"
    echo "  - hand_tracker.py"
    echo "  - hand_tracker_enhanced.py"
    exit 1
fi

# Check for requirements.txt
if [ -f "requirements.txt" ]; then
    print_success "Found: requirements.txt"
else
    print_warning "requirements.txt not found. Creating it..."
    cat > requirements.txt << 'EOF'
opencv-python==4.8.1.78
mediapipe==0.10.8
EOF
    print_success "Created: requirements.txt"
fi

# Check for Dockerfile
if [ -f "Dockerfile" ]; then
    print_success "Found: Dockerfile"
else
    print_warning "Dockerfile not found!"
    echo "Please download the Dockerfile from the outputs"
fi

# Check for docker-compose.yml
if [ -f "docker-compose.yml" ]; then
    print_success "Found: docker-compose.yml"
else
    print_warning "docker-compose.yml not found (optional)"
fi

# Check for .gitignore
if [ -f ".gitignore" ]; then
    print_success "Found: .gitignore"
else
    print_warning ".gitignore not found. Creating it..."
    cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
*.so
.Python
venv/
ENV/
.vscode/
.idea/
.DS_Store
EOF
    print_success "Created: .gitignore"
fi

# Check for README
if [ -f "README.md" ]; then
    print_success "Found: README.md"
else
    print_warning "README.md not found"
    echo "Consider creating a README.md file for your project"
fi

echo ""
echo "=========================================="
echo "File Check Complete!"
echo "=========================================="
echo ""

# Count required files
required_count=0
[ -f "hand.py" ] || [ -f "hand_tracker.py" ] || [ -f "hand_tracker_enhanced.py" ] && ((required_count++))
[ -f "requirements.txt" ] && ((required_count++))
[ -f "Dockerfile" ] && ((required_count++))

if [ $required_count -eq 3 ]; then
    print_success "All required files present! ✨"
    echo ""
    echo "You're ready to:"
    echo "  1. Build Docker image: docker build -t hand-tracker ."
    echo "  2. Push to GitHub: git init && git add . && git commit -m 'Initial commit'"
    echo ""
    echo "Or run: ./deploy.sh for guided deployment"
else
    print_warning "Some required files are missing"
    echo "Required files:"
    echo "  - Python file (hand.py, hand_tracker.py, or hand_tracker_enhanced.py)"
    echo "  - requirements.txt"
    echo "  - Dockerfile"
fi

echo ""
echo "Current directory structure:"
ls -la