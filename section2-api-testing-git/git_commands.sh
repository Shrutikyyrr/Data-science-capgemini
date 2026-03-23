#!/bin/bash
# Section 2 – Git Workflow Commands
# Run these from the root of your project

# Step 1: Initialize repo
git init

# Step 2: Add all files
git add .

# Step 3: First commit
git commit -m "initial commit: student management API"

# Step 4: Create feature branch
git checkout -b feature/api

# Step 5: Push to GitHub (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/student-management.git
git push -u origin feature/api

# Step 6: Push main branch too
git checkout main
git push -u origin main
