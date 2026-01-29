import os
import json
from typing import Dict, Any, AsyncGenerator
from google import genai
from google.genai import types
from app.data import PHONES
from app.firecrawl import FireCrawlClient

class ChatEngine:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        self.client = genai.Client(api_key=self.api_key)
        self.phones_data = json.dumps(PHONES, indent=2)
        self.phone_map = {p['id']: p for p in PHONES}
        self.firecrawl = FireCrawlClient()
        
    def _is_greeting(self, query: str) -> bool:
        greetings = ["hello", "hi", "hey", "good morning", "good evening", "how are you"]
        return query.lower().strip() in greetings
    
    def _get_system_prompt(self, search_context: str = "") -> str:
        return f"""You are TechScout AI, an expert mobile phone shopping assistant.

## Your Capabilities:
- Help users discover, compare, and learn about mobile phones
- Use LIVE WEB DATA when available for latest prices and specs
- Provide structured comparisons using markdown tables

## INVENTORY DATABASE:
{self.phones_data}

{search_context}

## OUTPUT FORMAT:
Always respond in clean MARKDOWN format. Use:
- **Tables** for comparisons (use proper markdown table syntax)
- **Bold** for important specs and prices
- **Bullet points** for feature lists
- **Headers** (##, ###) to organize information

## COMPARISON FORMAT EXAMPLE:
When comparing phones, ALWAYS use this table format:

| Feature | Phone A | Phone B |
|---------|---------|---------|
| Price | ₹XX,XXX | ₹XX,XXX |
| Display | 6.7" AMOLED | 6.5" LCD |
| Processor | Snapdragon 8 Gen 2 | Dimensity 9200 |
| Camera | 50MP + 12MP | 64MP + 8MP |
| Battery | 5000mAh | 4500mAh |

## RULES:
1. Be helpful, concise, and accurate
2. Use data from INVENTORY first, supplement with WEB DATA
3. For comparisons, ALWAYS use markdown tables
4. Include prices in INR (₹)
5. If asked about phones not in inventory, use web search data
6. Never hallucinate specs - only use provided data
"""

    async def process_query_stream(self, query: str) -> AsyncGenerator[str, None]:
        """
        Process the user query using Gemini with streaming.
        Yields text chunks as they arrive.
        """
        
        # 1. Perform Web Search for live context (non-greeting queries)
        search_context = ""
        if len(query) > 5 and not self._is_greeting(query):
            print(f"[TechScout] Searching web for: {query}")
            search_results = self.firecrawl.search(query + " mobile phone specs price india 2024", limit=3)
            if search_results:
                formatted_results = []
                for r in search_results[:3]:
                    title = r.get('title', 'No title')
                    url = r.get('url', '')
                    content = r.get('markdown', r.get('description', ''))[:400]
                    formatted_results.append(f"**{title}**\nURL: {url}\n{content}")
                
                search_context = f"""
## LIVE WEB SEARCH RESULTS:
{chr(10).join(formatted_results)}
"""
        
        system_prompt = self._get_system_prompt(search_context)
        
        try:
            # Use streaming with Gemini
            response = self.client.models.generate_content_stream(
                model="gemini-2.0-flash",
                contents=query,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    temperature=0.4
                )
            )
            
            # Stream the response chunks
            for chunk in response:
                if chunk.text:
                    yield chunk.text
                    
        except Exception as e:
            error_msg = str(e)
            print(f"[TechScout] LLM Error: {error_msg}")
            
            # Fallback error message
            yield f"I apologize, but I'm having trouble processing your request. Please try again in a moment."
    
    def process_query(self, query: str) -> Dict[str, Any]:
        """
        Synchronous version for backward compatibility.
        Returns complete response.
        """
        search_context = ""
        if len(query) > 5 and not self._is_greeting(query):
            search_results = self.firecrawl.search(query + " mobile phone specs price india 2024", limit=3)
            if search_results:
                formatted_results = []
                for r in search_results[:3]:
                    title = r.get('title', 'No title')
                    content = r.get('markdown', r.get('description', ''))[:400]
                    formatted_results.append(f"**{title}**\n{content}")
                search_context = f"\n## LIVE WEB DATA:\n{chr(10).join(formatted_results)}\n"
        
        system_prompt = self._get_system_prompt(search_context)
        
        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=query,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    temperature=0.4
                )
            )
            
            return {
                "type": "text",
                "content": response.text,
                "data": None
            }
            
        except Exception as e:
            print(f"[TechScout] Error: {e}")
            return {
                "type": "text",
                "content": "I'm having trouble right now. Please try again.",
                "data": None
            }
