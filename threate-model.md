## 1. Actors & Roles
- Admin: Full access to all data including secrets.
- Operator: Access to operational data (e.g., management IP).
- Viewer: Read-only access to non-sensitive public data.

## 2. Assets
- API Keys / Secrets (apiKey).
- Management IP Addresses (managementIpAddress).
- Incident summaaries (issueSummary).

## 3. Threat Analysis (STRIDE)
- Information Disclosure: Unprivileged roles (Viewer) accessing sensitive fields (apiKey, managementIpAddress).
- Elevation of Privilege: Bypassing role validation to retrieve restricted JSON entries.
