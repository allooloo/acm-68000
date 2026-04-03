# Azure Hyperscale Deployment

ACM-68000 runs on **Microsoft Azure** production infrastructure.

---

## Infrastructure

| Attribute | Value |
|-----------|-------|
| **Cloud Provider** | Microsoft Azure |
| **Region** | France Central (Paris) |
| **Compute** | Azure Container Apps |
| **Registry** | Azure Container Registry |
| **CDN** | Cloudflare |
| **Latency** | Sub-40ms global |
| **Uptime SLA** | 99.9% |
| **Partner Program** | Microsoft AI Cloud Partner |

---

## Endpoints

| Service | URL | Status |
|---------|-----|--------|
| **MCP Server** | https://mcp.10060.ai | LIVE |
| **Signal Reference** | https://7signalstack.ai | LIVE |
| **DPU Rail** | https://aio-tfx-rail.ai | LIVE |
| **Resolver** | https://resolver.aio-resolver.com | LIVE |
| **Protocol Spec** | https://allooloo.github.io/acm-68000 | LIVE |

---

## Why Azure?

- **Enterprise-grade reliability** - 99.9% SLA
- - **Global edge network** - Sub-40ms response times
  - - **Container-native** - Azure Container Apps for auto-scaling
    - - **Microsoft AI ecosystem** - Native integration path for Copilot, Azure OpenAI
      - - **Compliance-ready** - GDPR, SOC 2, ISO 27001
       
        - ---

        ## Live Regions

        | Region | Jurisdiction Coverage |
        |--------|----------------------|
        | **France Central (Paris)** | EU, UK, CH |
        | *NYC (planned)* | US, CA, MX, BR |
        | *Singapore (planned)* | SG, JP, KR, AU, IN |

        ---

        ## Container Apps

        All services run as stateless containers on Azure Container Apps:

        - `acm-mcp-server` - MCP protocol server
        - - `aio-tfx-rail-ai` - DPU rail endpoint
          - - `sevensignalstack-ai` - Signal reference
            - - `rco-resolver-v2-1` - Core resolver
             
              - ---

              ## Microsoft AI Cloud Partner Program

              Allooloo Technologies Corp. is a **Microsoft AI Cloud Partner**, enabling:

              - Direct integration with Azure OpenAI Service
              - - Copilot extensibility pathway
                - - Enterprise support escalation
                 
                  - ---

                  **Allooloo Technologies Corp.**
                  Vancouver - Paris - Barcelona
                  https://allooloo.ai
