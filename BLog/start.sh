#!/bin/bash
python3 run.py
celery -A Blog.users.route:celery worker -l info