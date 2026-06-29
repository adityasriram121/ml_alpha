# Run from PowerShell after installing Python and Git if they are not already available.
Set-Location -LiteralPath $PSScriptRoot
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --user --name ml_alpha --display-name "Python 3 (ml_alpha)"
Write-Host "Setup complete. Run .\launch_jupyter.ps1 to open JupyterLab."
