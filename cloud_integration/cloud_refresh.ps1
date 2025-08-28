# PowerShell Script: Trigger Power BI Dataset Refresh
# This script uses Power BI REST API to refresh a dataset published to Power BI Service
# Prerequisites: Register an Azure AD app, grant permissions, and get an access token

$clientId = "<Your-Client-Id>"
$clientSecret = "<Your-Client-Secret>"
$tenantId = "<Your-Tenant-Id>"
$groupId = "<Your-Workspace-Id>"
$datasetId = "<Your-Dataset-Id>"

# Get access token
$body = @{ 
    grant_type    = "client_credentials"
    client_id     = $clientId
    client_secret = $clientSecret
    resource      = "https://analysis.windows.net/powerbi/api"
}
$tokenResponse = Invoke-RestMethod -Method Post -Uri "https://login.microsoftonline.com/$tenantId/oauth2/token" -Body $body
$accessToken = $tokenResponse.access_token

# Trigger refresh
$headers = @{ Authorization = "Bearer $accessToken" }
$refreshUrl = "https://api.powerbi.com/v1.0/myorg/groups/$groupId/datasets/$datasetId/refreshes"
Invoke-RestMethod -Method Post -Uri $refreshUrl -Headers $headers

Write-Output "Refresh triggered for Power BI dataset $datasetId in workspace $groupId."
