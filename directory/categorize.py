def classify_tool(name, url):
    name_lower = name.lower()
    url_lower = url.lower()

    # Define simple keyword-category mapping
    categories = {
        "Conversational AI": ["chat", "talk", "gpt", "bot", "dialog", "conversation"],
        "Image Generation": ["image", "photo", "art", "draw", "picture", "illustration"],
        "Video Generation": ["video", "animation", "scene", "film", "clip"],
        "Voice AI": ["voice", "speech", "audio", "sound", "listen"],
        "Writing AI": ["write", "text", "content", "story", "copy", "generate", "blog"],
        "Code/Developer AI": ["code", "developer", "program", "script", "debug", "automation"],
        "Search AI": ["search", "find", "discover", "recommend", "explore"],
        "Analytics/Data AI": ["data", "insight", "analyze", "predict", "forecast", "metrics"]
    }

    for category, keywords in categories.items():
        if any(keyword in name_lower or keyword in url_lower for keyword in keywords):
            return category
    
    return "Other"