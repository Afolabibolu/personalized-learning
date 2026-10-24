# Network Auditing

## What it is and why it matters

Network auditing is the systematic examination and evaluation of an organisation's network infrastructure, configurations and activity, to ensure security, compliance and operational efficiency. Auditors review hardware such as routers, switches and firewalls, as well as software, protocols and user access controls. They analyse traffic, logs and configurations to find vulnerabilities, misconfigurations, unauthorised access and performance bottlenecks.

**Why it matters:**
- it finds weaknesses before attackers do;
- it checks compliance with regulations such as **ISO 27001, GDPR and HIPAA**, avoiding legal penalties and reputational damage;
- it verifies that only authorised users reach sensitive resources, preventing breaches and insider threats;
- it exposes inefficiencies and outdated systems, supporting maintenance, upgrades and accountability, especially with cloud and remote access.

## Types of audit

- **Security audits** look for vulnerabilities, misconfigurations and unauthorised access points in firewalls, IDS, access controls and encryption.
- **Compliance audits** check regulatory standards.
- **Performance audits** analyse bandwidth, latency, packet loss and hardware performance.
- **Operational audits** review day-to-day management: backups, patching and change control.

Audits can be manual (inspection and interviews) or automated (scanning tools).

## Key components

1. **Asset inventory:** every router, switch, firewall, server, endpoint and IoT device.
2. **Configuration review:** settings, firewall rules, access controls and patch levels.
3. **Traffic analysis:** data flow, anomalies and bottlenecks, using tools such as Wireshark or NetFlow.
4. **User access and authentication:** login records, privilege levels, passwords and MFA.
5. **Log and event review:** audit trails, errors and signs of compromise.
6. **Vulnerability assessment:** scans with tools such as Nessus or OpenVAS.
7. **Compliance mapping:** ISO 27001, GDPR, HIPAA, PCI-DSS.
8. **Documentation and reporting:** findings, risk levels and recommendations.

## The audit lifecycle

**Planning** sets the scope, objectives, resources, critical assets and risks. **Execution** collects data through scans, traffic analysis and configuration reviews. **Reporting** records vulnerabilities, risk levels and recommended actions. **Remediation** fixes them by patching, reconfiguring or updating policy. A **follow-up audit** confirms the fixes worked. The cycle then repeats.

## Tools

- **Nmap:** network discovery and vulnerability scanning.
- **Wireshark:** packet analysis.
- **Nessus and OpenVAS:** vulnerability assessment.
- **SolarWinds NCM and ManageEngine OpManager:** automated auditing.
- **PRTG, Zabbix and Nagios:** real-time monitoring.
- **Netwrix Auditor:** compliance and change tracking.

## Audit techniques

- **Log analysis** spots failed logins, odd access times and unexpected changes. With a **SIEM**, it triggers real-time alerts.
- **Vulnerability scanning** checks open ports, outdated software and misconfigured services.
- **Configuration auditing** compares settings with baselines to catch unauthorised changes.
- **Traffic analysis** watches bandwidth and anomalies. For example, a sudden rise in outbound traffic from one device may mean it is compromised.
- **User access auditing** tracks successful and failed logins and privilege escalations to detect brute-force attacks and misuse.

Source: Computer Security(Dr Abiola).docx
