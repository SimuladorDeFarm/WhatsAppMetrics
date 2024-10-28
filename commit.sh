#! /bin/bash

echo "Commit name:"
read title
git add .
git status
git commit -m "$title"
