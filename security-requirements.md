# Security Requirements

1. RBAC Enforcement: The json_search() function must validate the provided role against policy.py before returning values.
2. Least Priviledge: If a role lacks permission for a key, the function must return an empty list [].
3. Default Deny: If role=None or an unrecognized role is provided, access to restricted fields must be denied.
