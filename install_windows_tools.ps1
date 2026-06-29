# Optional helper. Run PowerShell normally; winget may ask for permission outside Codex.
winget install --id Python.Python.3.12 -e --silent --accept-package-agreements --accept-source-agreements
winget install --id Git.Git -e --silent --accept-package-agreements --accept-source-agreements
Write-Host "Restart PowerShell after installation, then run setup_windows.ps1."
