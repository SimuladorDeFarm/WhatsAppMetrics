#! /bin/bash

git add .
git status
echo "Commit name:"
read title
git commit -m "$title"
