"""
ACM-68000 MCP Server
Official MCP server for the ACM-68000 deterministic signal protocol.

Registry: io.github.allooloo/acm-68000-mcp
Endpoint: https://mcp.10060.ai
Operator: Allooloo Technologies Corp.

MIT License
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import httpx

app = FastAPI(
    title="ACM-68000 MCP Server",
    description="Deterministic signal protocol for agentic commerce. First CPG/FMCG product resolver on MCP.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ACM-68000 Signal Definitions
ACM_SIGNALS = {
    "ACM-000": {"state": "NOT_APPLICABLE", "meaning": "Signal does not govern this SKU or context"},
    "ACM-200": {"state": "ALLOW", "meaning": "Agent may execute the commercial action"},
    "ACM-300": {"state": "CONDITIONAL", "meaning": "Action requires additional conditions"},
    "ACM-403": {"state": "RESTRICT", "meaning": "Action blocked under current conditions"},
    "ACM-404": {"state": "NOT_FOUND", "meaning": "Object not registered in any signal cluster"},
    "ACM-451": {"state": "ESCALATE", "meaning": "Human-in-the-loop required"},
    "ACM-500": {"state": "SYSTEM_ERROR", "meaning": "Infrastructure failure — retry or fallback"}
}

DPU_RAIL_BASE = "https://aio-tfx-rail.ai/dpu"

# ============================================================
# Health & Discovery
# ============================================================

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "ok", "protocol": "MCP", "signal_protocol": "ACM-68000"}

@app.get("/.well-known/mcp.json")
async def mcp_manifest():
    """MCP server manifest for discovery"""
    return {
        "name": "acm-68000-mcp",
        "version": "1.0.0",
        "description": "ACM-68000 DPU resolver. First CPG product eligibility checker on MCP.",
        "protocol": "ACM-68000",
        "operator": "Allooloo Technologies Corp.",
        "tools": [
            {"name": "resolve_gtin", "description": "Resolve GTIN to ACM signal"},
            {"name": "get_dpu", "description": "Get full DPU object for GTIN"},
            {"name": "list_signals", "description": "List all ACM-68000 signals"},
            {"name": "check_eligibility", "description": "Check GTIN eligibility in jurisdiction"},
            {"name": "list_products", "description": "List all products on AIO-TFX Rail"}
        ]
    }

# ============================================================
# MCP Tools
# ============================================================

@app.get("/tools/resolve_gtin")
async def resolve_gtin(gtin: str):
    """
    Quick GTIN → ACM signal lookup.
    Returns the signal and state for a given GTIN barcode.
    """
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{DPU_RAIL_BASE}/{gtin}.json")
            if response.status_code == 200:
                dpu = response.json()
                return {
                    "gtin": gtin,
                    "signal": dpu.get("signal", "ACM-404"),
                    "state": dpu.get("state", "NOT_FOUND"),
                    "name": dpu.get("name", "Unknown")
                }
            else:
                return {
                    "gtin": gtin,
                    "signal": "ACM-404",
                    "state": "NOT_FOUND",
                    "error": "GTIN not registered in DPU rail"
                }
    except Exception as e:
        return {
            "gtin": gtin,
            "signal": "ACM-500",
            "state": "SYSTEM_ERROR",
            "error": str(e)
        }

@app.get("/tools/get_dpu")
async def get_dpu(gtin: str):
    """
    Get full DPU v1.1 object for a GTIN.
    Includes jurisdiction, compliance, brand, and signal data.
    """
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{DPU_RAIL_BASE}/{gtin}.json")
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=404, detail=f"DPU not found for GTIN {gtin}")
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch DPU: {str(e)}")

@app.get("/tools/list_signals")
async def list_signals():
    """
    List all 7 ACM-68000 signal definitions.
    Reference: https://7signalstack.ai
    """
    return {
        "protocol": "ACM-68000",
        "version": "1.2",
        "signals": ACM_SIGNALS,
        "reference": "https://7signalstack.ai/signals.json"
    }

@app.get("/tools/check_eligibility")
async def check_eligibility(gtin: str, jurisdiction: str):
    """
    Check if a GTIN is eligible for sale in a specific jurisdiction.
    Returns eligibility status with reason.
    """
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{DPU_RAIL_BASE}/{gtin}.json")
            if response.status_code == 200:
                dpu = response.json()
                jurisdictions = dpu.get("jurisdiction", [])
                jurisdiction_upper = jurisdiction.upper()
                
                if jurisdiction_upper in jurisdictions:
                    return {
                        "gtin": gtin,
                        "jurisdiction": jurisdiction_upper,
                        "eligible": True,
                        "signal": "ACM-200",
                        "state": "ALLOW",
                        "reason": f"{jurisdiction_upper} is in authorized jurisdiction list"
                    }
                else:
                    return {
                        "gtin": gtin,
                        "jurisdiction": jurisdiction_upper,
                        "eligible": False,
                        "signal": "ACM-403",
                        "state": "RESTRICT",
                        "reason": f"{jurisdiction_upper} not in authorized jurisdictions: {jurisdictions}"
                    }
            else:
                return {
                    "gtin": gtin,
                    "jurisdiction": jurisdiction.upper(),
                    "eligible": False,
                    "signal": "ACM-404",
                    "state": "NOT_FOUND",
                    "reason": "GTIN not registered"
                }
    except Exception as e:
        return {
            "gtin": gtin,
            "jurisdiction": jurisdiction.upper(),
            "eligible": False,
            "signal": "ACM-500",
            "state": "SYSTEM_ERROR",
            "reason": str(e)
        }

@app.get("/tools/list_products")
async def list_products():
    """
    List all products currently registered on the AIO-TFX Rail.
    """
    products = [
        {
            "gtin": "00990832300006",
            "name": "TreeFree Core econoLiite Core® Disposable Baby Diapers 240 Each",
            "format": "Open (Tape)",
            "brand": "GreenCore Solutions Corp.",
            "signal": "ACM-200",
            "dpu_url": f"{DPU_RAIL_BASE}/00990832300006.json"
        },
        {
            "gtin": "00990832300013",
            "name": "TreeFree Core Disposable Baby Diapers 240 Each",
            "format": "Pant (Pull-up)",
            "brand": "GreenCore Solutions Corp.",
            "signal": "ACM-200",
            "dpu_url": f"{DPU_RAIL_BASE}/00990832300013.json"
        }
    ]
    return {
        "rail": "AIO-TFX-Rail",
        "rail_url": "https://aio-tfx-rail.ai",
        "product_count": len(products),
        "products": products
    }

# ============================================================
# Root
# ============================================================

@app.get("/")
async def root():
    """Root endpoint with server info"""
    return {
        "server": "acm-68000-mcp",
        "version": "1.0.0",
        "protocol": "ACM-68000",
        "operator": "Allooloo Technologies Corp.",
        "registry": "io.github.allooloo/acm-68000-mcp",
        "endpoints": {
            "health": "/health",
            "manifest": "/.well-known/mcp.json",
            "tools": {
                "resolve_gtin": "/tools/resolve_gtin?gtin={gtin}",
                "get_dpu": "/tools/get_dpu?gtin={gtin}",
                "list_signals": "/tools/list_signals",
                "check_eligibility": "/tools/check_eligibility?gtin={gtin}&jurisdiction={jurisdiction}",
                "list_products": "/tools/list_products"
            }
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
