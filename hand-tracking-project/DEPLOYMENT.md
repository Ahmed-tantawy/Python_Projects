# 🚢 Deployment Guide: Docker + GitHub

Complete guide to containerize and deploy your hand tracking project.

## 📋 Prerequisites Checklist

- [ ] Docker installed on your Mac
- [ ] GitHub account created
- [ ] Git installed locally
- [ ] Project files ready

## 🐳 Part 1: Docker Setup

### Step 1: Install Docker on Mac

```bash
# If not installed, download from:
# https://docs.docker.com/desktop/install/mac-install/

# Verify installation
docker --version
docker-compose --version
```

### Step 2: Prepare Your Project Directory

```bash
cd ~/hand-tracking-project

# Your directory should have:
ls -la
# hand.py (or hand_tracker_enhanced.py)
# requirements.txt
# Dockerfile
# docker-compose.yml
# .dockerignore
# .gitignore
# README.md
```

### Step 3: Build Docker Image

```bash
# Build the image
docker build -t hand-tracker:latest .

# Verify the image was created
docker images | grep hand-tracker
```

### Step 4: Test Docker Container Locally

**On macOS with XQuartz:**

```bash
# Install XQuartz if needed
brew install --cask xquartz

# Start XQuartz
open -a XQuartz

# In XQuartz preferences (XQuartz > Preferences):
# Go to Security tab
# Check "Allow connections from network clients"
# Restart XQuartz

# Get your IP address
IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
echo $IP

# Allow X11 forwarding
xhost + $IP

# Run the container
docker run -it --rm \
  --device=/dev/video0:/dev/video0 \
  -e DISPLAY=$IP:0 \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  hand-tracker:latest

# Or use docker-compose (easier)
docker-compose up
```

**Alternative: Run without GUI (for testing)**

```bash
# Modify your Python script to save output instead of displaying
docker run -it --rm \
  --device=/dev/video0:/dev/video0 \
  hand-tracker:latest
```

### Step 5: Push to Docker Hub (Optional)

```bash
# Login to Docker Hub
docker login

# Tag your image
docker tag hand-tracker:latest yourusername/hand-tracker:latest

# Push to Docker Hub
docker push yourusername/hand-tracker:latest
```

## 🐙 Part 2: GitHub Setup

### Step 1: Create GitHub Repository

```bash
# Go to github.com and:
# 1. Click "+" in top right > "New repository"
# 2. Name: "hand-tracking-project"
# 3. Description: "Real-time hand tracking with OpenCV and MediaPipe"
# 4. Choose Public or Private
# 5. DON'T initialize with README (we have one)
# 6. Click "Create repository"
```

### Step 2: Initialize Git in Your Project

```bash
# Navigate to your project
cd ~/hand-tracking-project

# Initialize git repository
git init

# Add all files
git add .

# Check what will be committed
git status

# Make your first commit
git commit -m "Initial commit: Hand tracking project with Docker support"
```

### Step 3: Connect to GitHub

```bash
# Add remote repository (replace with your username)
git remote add origin https://github.com/yourusername/hand-tracking-project.git

# Verify remote was added
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 4: Verify Upload

```bash
# Go to your GitHub repository URL:
# https://github.com/yourusername/hand-tracking-project

# You should see all your files!
```

## 📝 Part 3: Project Structure for GitHub

Your final directory should look like:

```
hand-tracking-project/
├── .dockerignore              ✅ Excludes files from Docker
├── .gitignore                 ✅ Excludes files from Git
├── Dockerfile                 ✅ Docker image definition
├── docker-compose.yml         ✅ Easy Docker management
├── hand_tracker.py            ✅ Basic version
├── hand_tracker_enhanced.py   ✅ Full-featured version
├── requirements.txt           ✅ Python dependencies
├── README.md                  ✅ Main documentation
├── README_ENHANCED.md         ✅ Feature details
├── DEPLOYMENT.md             ✅ This file
└── LICENSE                    ✅ MIT License (optional)
```

## 🔄 Part 4: Making Updates

### Update Your Code

```bash
# Make changes to your files
code hand_tracker_enhanced.py

# Check what changed
git status
git diff

# Stage changes
git add hand_tracker_enhanced.py

# Commit with descriptive message
git commit -m "Add new gesture recognition feature"

# Push to GitHub
git push origin main
```

### Rebuild Docker Image

```bash
# Rebuild after code changes
docker build -t hand-tracker:latest .

# Test the new image
docker-compose up

# Push new version to Docker Hub
docker tag hand-tracker:latest yourusername/hand-tracker:v1.1
docker push yourusername/hand-tracker:v1.1
```

## 🌟 Part 5: GitHub Best Practices

### Create a Good README

Your README should include:
- Project description
- Features list
- Installation instructions
- Usage examples
- Screenshots/GIFs (if possible)
- Contributing guidelines
- License information

### Add a License

```bash
# Add MIT License file
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

git add LICENSE
git commit -m "Add MIT License"
git push
```

### Add GitHub Topics

On GitHub repository page:
1. Click ⚙️ next to "About"
2. Add topics: `python`, `opencv`, `mediapipe`, `computer-vision`, `hand-tracking`, `docker`
3. Save changes

## 🎯 Quick Command Reference

### Docker Commands

```bash
# Build image
docker build -t hand-tracker .

# Run container
docker run -it --rm hand-tracker

# List images
docker images

# List running containers
docker ps

# Stop container
docker stop <container-id>

# Remove image
docker rmi hand-tracker

# Clean up everything
docker system prune -a
```

### Git Commands

```bash
# Check status
git status

# Add files
git add .

# Commit changes
git commit -m "message"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# View commit history
git log --oneline

# Create new branch
git checkout -b feature-name

# Switch branches
git checkout main

# Merge branch
git merge feature-name
```

## 🐛 Troubleshooting

### Docker Issues on Mac

**Issue: Cannot access camera**
```bash
# Check camera permissions in System Preferences
# System Preferences > Security & Privacy > Camera
# Enable Docker
```

**Issue: Display not working**
```bash
# Make sure XQuartz is running
ps aux | grep XQuartz

# Check DISPLAY variable
echo $DISPLAY

# Reset X11 permissions
xhost +localhost
```

### Git Issues

**Issue: Permission denied (publickey)**
```bash
# Set up SSH keys for GitHub
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub
# Add the output to GitHub: Settings > SSH Keys
```

**Issue: Remote already exists**
```bash
# Remove and re-add
git remote remove origin
git remote add origin https://github.com/yourusername/hand-tracking-project.git
```

## ✅ Final Checklist

Before sharing your project:

- [ ] Code is clean and commented
- [ ] README is complete and clear
- [ ] Docker image builds successfully
- [ ] Docker container runs without errors
- [ ] All files committed to Git
- [ ] Pushed to GitHub
- [ ] Repository is public (if you want to share)
- [ ] License file added
- [ ] .gitignore is working
- [ ] Requirements.txt is up to date

## 🚀 Next Steps

1. **Add CI/CD**: Set up GitHub Actions for automated testing
2. **Add Tests**: Write unit tests for your functions
3. **Documentation**: Add more detailed API documentation
4. **Docker Hub**: Set up automated builds
5. **Badges**: Add status badges to README
6. **Demo**: Record a video demo
7. **Blog Post**: Write about your project

## 📚 Resources

- [Docker Documentation](https://docs.docker.com/)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Markdown Guide](https://www.markdownguide.org/)

---

🎉 **Congratulations!** Your project is now containerized and on GitHub!