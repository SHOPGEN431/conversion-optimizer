#!/bin/bash

# Conversion Rate Optimizer - Deployment Script
# This script helps deploy the project to GitHub and Vercel

echo "🚀 Starting deployment process..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Initialize git repository if not already done
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit: Conversion Rate Optimization Tool"
fi

# Add all files
echo "📝 Adding files to Git..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "Update: Enhanced CRO tool with before/after comparison"

# Add remote origin if not exists
if ! git remote get-url origin &> /dev/null; then
    echo "🔗 Adding GitHub remote..."
    git remote add origin https://github.com/SHOPGEN431/conversion-optimizer.git
fi

# Push to GitHub
echo "⬆️ Pushing to GitHub..."
git push -u origin main

echo "✅ Successfully pushed to GitHub!"
echo ""
echo "🌐 Next steps:"
echo "1. Go to https://github.com/SHOPGEN431/conversion-optimizer"
echo "2. Verify your code is uploaded"
echo "3. Install Vercel CLI: npm i -g vercel"
echo "4. Run: vercel"
echo "5. Follow the prompts to deploy"
echo ""
echo "🎉 Your Conversion Rate Optimization Tool will be live at:"
echo "   https://conversion-optimizer.vercel.app" 