# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:1.10.2

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
COPY requirements-actions.txt .

# The Rasa SDK image runs as non-root user by default. Hence, you have to switch
# back to the `root` user if you want to install additional dependencies
USER root

# Install extra requirements for actions code, if necessary (uncomment next line)
RUN pip3 install -r requirements-actions.txt

# Copy actions folder to working directory
COPY constants.py /app/actions/
COPY . /app/actions/

# Switch back to a non-root user
USER 1001
