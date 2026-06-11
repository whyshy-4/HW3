#!/bin/bash

CURRENT_DIR=$(pwd)

case "$1" in
    build_generator)
        docker build -t data-generator -f Dockerfile.generator .
        ;;
    run_generator)
        docker run --rm -v "$CURRENT_DIR/data:/data" data-generator
        ;;
    create_local_data)
        python3 generate.py local_data
        ;;
    build_reporter)
        docker build -t data-reporter -f Dockerfile.reporter .
        ;;
    run_reporter)
        docker run --rm -v "$CURRENT_DIR/data:/data" data-reporter
        ;;
    structure)
        ls -R
        ;;
    clear_data)
        rm -f data/*.csv data/*.html
        ;;
    inside_generator)
        docker run --rm -v "$CURRENT_DIR/data:/data" data-generator ls -la /data
        ;;
    inside_reporter)
        docker run --rm -v "$CURRENT_DIR/data:/data" data-reporter ls -la /data
        ;;
    *)
        exit 1
        ;;
esac