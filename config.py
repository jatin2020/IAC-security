config = {
"clickops_user_agents": ["console.amazonaws.com", "Coral/Jakarta", "AWS CloudWatch Console"],
"clickops_prefixes": ["S3Console/", "[S3Console", "Mozilla/"],
 "read_operation_pattern": "\\b(?:Get|Describe|List|Scan|Read)[A-Za-z]+(?:[A-Z][a-z]+)?|(DownloadDBLogFilePortion|TestScheduleExpression|TestEventPattern|LookupEvents|listDnssec|Decrypt|REST\\.GET\\.OBJECT_LOCK_CONFIGURATION|ConsoleLogin)\\b"
}
