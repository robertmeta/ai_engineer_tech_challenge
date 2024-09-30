Stack
=====

Our technology stack comprises the following components:

- Linode CLI: Utilized for creating easy, hand-rolled deployment scripts,
  simplifying server management and deployment processes.
- Make: A reliable build automation tool that, despite its age, remains
  functional and effective for our needs.
- Python 3.10+: Chosen for its advanced asynchronous capabilities and new
  control flow features, enhancing performance and code readability.
- Entr: Employed for monitoring file changes and triggering rebuilds,
  streamlining the development workflow.
- Docker: Used for containerization, ensuring consistent environments across
  development, testing, and production.
- D2: A tool for generating diagrams and visualizations, aiding in documentation
  and planning.
- Ollama (with ROPE data structure fix): Incorporates the ROPE data structure
  fix to improve performance in handling large text data.
- Llama 3.2 3B: A brand-new language model that is exceptionally fast, supports
  a 128k context window, and is perfect for our summarization and citation use
  case.
- HTMX: A modern UI framework that facilitates the creation of dynamic web pages
  without the overhead of heavy JavaScript frameworks.
- Jinja2: A very nice templating system for python.

Future Considerations:

- Caching: Would need to use a caching system for the fetched pages to build up
  our own index of files. KeyDB instead of Redis due to recent licensing
  changes.
- Docker Compose: Planning to adopt Docker Compose for managing more complex
  configurations in future developments, allowing for easier multi-container
  setups.

By leveraging this stack, we aim to build a robust, scalable, and efficient
application that meets our performance requirements while maintaining simplicity
in development and deployment processes.
