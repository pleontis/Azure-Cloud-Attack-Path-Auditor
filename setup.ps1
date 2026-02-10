# -----------------------------
# Clean Setup for Azure Pentesting Project
# Works on Windows + Python 3.10
# -----------------------------

# Go to project folder (adjust path if needed)
cd "C:\Users\User1\Desktop\Azure Pentesting"

# Remove old virtual environment if exists
if (Test-Path "venv") { Remove-Item -Recurse -Force "venv" }

# Create new virtual environment with Python 3.10
py -3.10 -m venv venv

#  Activate venv
.\venv\Scripts\Activate.ps1

# Upgrade pip, setuptools, wheel
python -m pip install --upgrade pip setuptools wheel

# Install required dependencies (prebuilt binaries)
pip install six cryptography --prefer-binary

# Install specific Azure SDK versions that work with SubscriptionClient
pip install azure-identity azure-mgmt-resource==20.0.0 azure-mgmt-authorization azure-mgmt-storage azure-mgmt-network --prefer-binary

# Quick test for Azure SDK
python -c "from azure.identity import DefaultAzureCredential; print('Azure SDK OK')"

Write-Host "`n Setup completed successfully! Your venv is ready and Azure SDK works."
