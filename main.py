from crewai import Agent, Task, Crew,LLM
from pydantic import Field
from crewai_tools import BaseTool
import os
from langchain_community.tools import TavilySearchResults


# Define LLM model
Ollama_LLM = LLM(model="ollama/llama3:8b",
    base_url="http://localhost:11434")

os.environ["TAVILY_API_KEY"] = 'tvly-xxxx' 


#tool
Tavily_tool = TavilySearchResults(
    max_results=2,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=True,
    # include_domains=[...],
    # exclude_domains=[...],
    # name="...",            # overwrite default tool name
    # description="...",     # overwrite default tool description
    # args_schema=...,       # overwrite default args_schema: BaseModel
)
class TavilyTool(BaseTool):
    name: str = "Search For Information in Internet"
    description: str = "Useful for search-based queries. Use this to find current information about research in the internet."
    search: TavilySearchResults = Field(default_factory=TavilySearchResults)
    def _run(self, query: str) -> str:
        """Execute the search query and return results"""
        try:
            return self.search.run(query)
        except Exception as e:
            return f"Error performing search: {str(e)}"
# Create agents
legal_researcher = Agent(
    role='Legal Research Analyst',
    goal='Research and analyze laws and regulations in {country} regarding {query}',
    backstory='Experienced legal researcher specializing in {country} law with expertise in legislative analysis',
    tools=[TavilyTool()],
    verbose=True,
    llm=Ollama_LLM
)

legal_writer = Agent(
    role='Legal Content Writer',
    goal='Create comprehensive legal analysis on {query} in {country}',
    backstory='Expert legal writer specializing in translating complex legal concepts into clear documentation',
    verbose=True,
    llm=Ollama_LLM
)

legal_reviewer = Agent(
    role='Legal Editor',
    goal='Review and verify legal content accuracy for {query} in {country}',
    backstory='Senior legal editor with extensive experience in regulatory compliance and legal documentation',
    verbose=True,
    llm=Ollama_LLM
)

# Define tasks
research = Task(
    description='Research current laws, regulations, and legal precedents in {country} regarding {query}',
    expected_output='Detailed report on legal framework and regulatory requirements',
    agent=legal_researcher
)

write = Task(
    description='Create comprehensive legal analysis document covering regulations and compliance requirements',
    expected_output='In-depth legal analysis document with citations to relevant laws',
    agent=legal_writer
)

edit = Task(
    description='Review and verify legal accuracy, ensure proper citations, and validate compliance information',
    expected_output='Finalized legal analysis document ready for review',
    agent=legal_reviewer,
    output_file=r'Legal Research\md_files\legal_analysis.md'
)

# Create the crew
crew = Crew(
    agents=[legal_researcher, legal_writer, legal_reviewer],
    tasks=[research, write, edit],
    verbose=True,
    planning=True
)

# Execute tasks with legal query
crew.kickoff(
    inputs={
        "country": "United States",  # Specify target country
        "query": "Data Privacy Regulations"  # Specify legal topic
    }
)
