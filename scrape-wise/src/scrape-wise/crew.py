from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import SeleniumScrapingTool, SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool, PDFSearchTool

# Définition des outils que tu veux utiliser
selenium_tool = selenium_tool = SeleniumScrapingTool(
    website_url='https://example.com',
    css_element='.main-content',
    wait_time=5
)
web_search_tool = WebsiteSearchTool(
    config=dict(
        llm=dict(
            provider="ollama",  # or google, openai, anthropic, llama2
            config=dict(
                model="llama2"
            )
        ),
        embedder=dict(
            provider="google",  # or openai, ollama
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document"
            )
        )
    )
)

scrape_tool = ScrapeWebsiteTool()
pdf_tool = PDFSearchTool()

@CrewBase
class InsightMeshCrew:
    """Crew pour orchestrer l'analyse web et documentaire"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def scraper_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['ScraperAgent'],
            tools=[scrape_tool]
        )

    @agent
    def search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['SearchAgent'],
            tools=[web_search_tool]
        )

    @agent
    def rag_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['RAGAgent'],
            tools=[pdf_tool]
        )

    @agent
    def critic_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['CriticAgent']
        )

    @agent
    def report_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['ReportAgent']
        )

    @agent
    def coordinator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['CoordinatorAgent']
        )

    @task
    def web_scraping_task(self) -> Task:
        return Task(config=self.tasks_config['web_scraping_task'], agent=self.scraper_agent())

    @task
    def complementary_search_task(self) -> Task:
        return Task(config=self.tasks_config['complementary_search_task'], agent=self.search_agent())

    @task
    def pdf_analysis_task(self) -> Task:
        return Task(config=self.tasks_config['pdf_analysis_task'], agent=self.rag_agent())

    @task
    def data_validation_task(self) -> Task:
        return Task(config=self.tasks_config['data_validation_task'], agent=self.critic_agent())

    @task
    def report_generation_task(self) -> Task:
        return Task(config=self.tasks_config['report_generation_task'], agent=self.report_agent())

    @task
    def coordination_task(self) -> Task:
        return Task(config=self.tasks_config['coordination_task'], agent=self.coordinator_agent())

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
