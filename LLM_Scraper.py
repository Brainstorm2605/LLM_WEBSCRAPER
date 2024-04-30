from scrapegraphai.graphs import SmartScraperGraph
import streamlit as ui
ui.title("WEB SCRAPER")
graph_config = {
    "llm": {
        "model": "ollama/llama3",
        "temperature": 0,
        "format": "json",  # Ollama needs the format to be specified explicitly
        "base_url": "http://localhost:11434",  # set Ollama URL
    },
    "embeddings": {
        "model": "ollama/llama3",
        "base_url": "http://localhost:11434",  
    }
}
link = ui.text_input("Webpage link")
prompt = ui.text_input("What you want to do")
button = ui.button("Submit")
if button:
    smart_scraper_graph = SmartScraperGraph(
        prompt=prompt,
        # also accepts a string with the already downloaded HTML code
        source=link,
        config=graph_config
    )

    result = smart_scraper_graph.run()
    ui.write(result)
