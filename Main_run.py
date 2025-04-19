name: Angel One Auto Login
on:
  workflow_dispatch:

jobs:
  run-script:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run login script
      run: python login_and_run.py
      env:
        API_KEY: ${{ secrets.API_KEY }}
        CLIENT_ID: ${{ secrets.CLIENT_ID }}
        PASSWORD: ${{ secrets.PASSWORD }}
        TOTP_SECRET: ${{ secrets.TOTP_SECRET }}
