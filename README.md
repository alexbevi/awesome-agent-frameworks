# Awesome Agent Frameworks [![Awesome Lists](https://srv-cdn.himpfen.io/badges/awesome-lists/awesomelists-flat.svg)](https://github.com/brandonhimpfen/awesome-lists)

A curated list of open source frameworks and tools for building agents, running agent systems, connecting tools, managing memory and retrieval, and observing or evaluating agent behavior.

This list is generated from a private research inventory and organized by category.

## Contents

- [Agent SDK / framework](#agent-sdk-framework)
- [Agent graph / runtime](#agent-graph-runtime)
- [RAG / knowledge system](#rag-knowledge-system)
- [Memory / context system](#memory-context-system)
- [Low-code builder / agent app](#low-code-builder-agent-app)
- [Tool / protocol / connector layer](#tool-protocol-connector-layer)
- [Developer / computer-use agent](#developer-computer-use-agent)
- [Data / ingestion / MLOps substrate](#data-ingestion-mlops-substrate)
- [Observability / evals](#observability-evals)
- [Model serving / gateway](#model-serving-gateway)
- [Database / infrastructure product](#database-infrastructure-product)
- [Protocol / standard only](#protocol-standard-only)
- [Related Awesome Lists](#related-awesome-lists)
- [Contribute](#contribute)
- [License](#license)

<a id="agent-sdk-framework"></a>
## Agent SDK / framework

Code-first APIs for agents, tools, prompts, models, and state.

- [AG2](https://ag2.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/ag2ai/ag2?style=social) - Community continuation of Microsoft's AutoGen multi-agent framework.
- [Agentica](https://github.com/wrtnlabs/agentica) ![GitHub Repo stars](https://img.shields.io/github/stars/wrtnlabs/agentica?style=social) - Agentica uses TypeScript compiler analysis to automatically generate type-safe function schemas for LLM tool calling, eliminating manual schema definition.
- [AgentScope](https://modelscope.github.io/agentscope/) ![GitHub Repo stars](https://img.shields.io/github/stars/agentscope-ai/agentscope?style=social) - Full-featured multi-agent framework from Alibaba DAMO Academy.
- [AutoGen](https://microsoft.github.io/autogen) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/autogen?style=social) - Microsoft's foundational multi-agent conversation framework.
- [BotSharp](https://botsharp.readthedocs.io) ![GitHub Repo stars](https://img.shields.io/github/stars/SciSharp/BotSharp?style=social) - BotSharp - AI multi-agent framework in .NET.
- [CAMEL](https://www.camel-ai.org) ![GitHub Repo stars](https://img.shields.io/github/stars/camel-ai/camel?style=social) - Multi-agent research framework studying collaborative AI systems at scale.
- [Context7](https://context7.com) ![GitHub Repo stars](https://img.shields.io/github/stars/upstash/context7?style=social) - Context7 is an MCP server that fetches live, up-to-date documentation for libraries and injects it directly into LLM/AI coding agent contexts.
- [CrewAI](https://crewai.com) ![GitHub Repo stars](https://img.shields.io/github/stars/crewAIInc/crewAI?style=social) - Promoted to Tier 2; O plane added for observability/ops surface.
- [GenAIScript](https://microsoft.github.io/genaiscript/) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/genaiscript?style=social) - Microsoft's automatable GenAI scripting environment.
- [Google ADK Go](https://google.github.io/adk-go/) ![GitHub Repo stars](https://img.shields.io/github/stars/google/adk-go?style=social) - Google ADK Go is the Go-language member of the Google Agent Development Kit family, extending the same agent abstractions to Go developers.
- [Google ADK (Java)](https://google.github.io/adk-java) ![GitHub Repo stars](https://img.shields.io/github/stars/google/adk-java?style=social) - Provides code-first agent building for Java developers with support for Gemini models, tool calling, multi-agent orchestration, and memory/session persistence.
- [Google ADK (JavaScript)](https://google.github.io/adk-js) ![GitHub Repo stars](https://img.shields.io/github/stars/google/adk-js?style=social) - Google's Agent Development Kit for JavaScript/TypeScript - the official JS implementation of ADK.
- [Google Agent Development Kit (ADK)](https://google.github.io/adk-python) ![GitHub Repo stars](https://img.shields.io/github/stars/google/adk-python?style=social) - Google's open-source agent development framework, tightly integrated with Gemini models and Google Cloud infrastructure.
- [Gorilla](https://gorilla.cs.berkeley.edu) ![GitHub Repo stars](https://img.shields.io/github/stars/ShishirPatil/gorilla?style=social) - LLM function call training, evaluation, and inference framework from UC Berkeley.
- [Guidance](https://github.com/guidance-ai/guidance) ![GitHub Repo stars](https://img.shields.io/github/stars/guidance-ai/guidance?style=social) - Guidance is a domain-specific language for controlling large language models - constrained decoding, guided generation, structured output, and tool invocation.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) ![GitHub Repo stars](https://img.shields.io/github/stars/NousResearch/hermes-agent?style=social) - Opinionated self-improving agent kit from Nous Research with 40+ built-in tools, multi-platform execution backends, and learning loop.
- [llama-cpp-agent](https://github.com/Maximilian-Winter/llama-cpp-agent) ![GitHub Repo stars](https://img.shields.io/github/stars/Maximilian-Winter/llama-cpp-agent?style=social) - Llama-cpp-agent - Python framework designed for easy interaction with Large Language Models running on llama.cpp.
- [Mastra](https://mastra.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/mastra-ai/mastra?style=social) - TypeScript-first AI application framework from the team behind Gatsby.
- [Mirascope](https://github.com/Mirascope/mirascope) ![GitHub Repo stars](https://img.shields.io/github/stars/Mirascope/mirascope?style=social) - Minimalist Python anti-framework for LLM interactions that favors composable primitives over heavy abstractions.
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) ![GitHub Repo stars](https://img.shields.io/github/stars/openai/openai-agents-python?style=social) - OpenAI's official production multi-agent orchestration framework and successor to OpenAI Swarm.
- [page-agent](https://github.com/alibaba/page-agent) ![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/page-agent?style=social) - TypeScript library from Alibaba for natural-language control of web interfaces.
- [Pydantic AI](https://ai.pydantic.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=social) - Production-grade Python agent framework from the Pydantic team leveraging type-safe structured outputs.
- [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/semantic-kernel?style=social) - Microsoft-backed open-source SDK for building AI agents and integrating LLMs into C#/.NET, Python, and Java codebases.
- [smolagents](https://huggingface.co/docs/smolagents) ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/smolagents?style=social) - Hugging Face's minimal code-first agent framework that executes Python tool calls.
- [Spring AI](https://spring.io/projects/spring-ai) ![GitHub Repo stars](https://img.shields.io/github/stars/spring-projects/spring-ai?style=social) - The official Spring Framework project for AI engineering in Java/JVM.
- [Strands Agents](https://strandsagents.com) ![GitHub Repo stars](https://img.shields.io/github/stars/strands-agents/harness-sdk?style=social) - Supports Amazon Bedrock, OpenAI, Anthropic, Ollama, and LiteLLM as model providers.
- [SuperAGI](https://superagi.com) ![GitHub Repo stars](https://img.shields.io/github/stars/TransformerOptimus/SuperAGI?style=social) - Open-source autonomous agent platform with tool marketplace and vector memory.
- [Vercel AI SDK](https://ai-sdk.dev/docs) ![GitHub Repo stars](https://img.shields.io/github/stars/vercel/ai?style=social) - The Vercel AI SDK is a widely-adopted TypeScript toolkit for building AI-powered Next.js and Node.js applications.

<a id="agent-graph-runtime"></a>
## Agent graph / runtime

Runtime for graph execution, checkpoints, resumability, HITL, or durable agent state.

- [Adala](https://humansignal.github.io/Adala/) ![GitHub Repo stars](https://img.shields.io/github/stars/HumanSignal/Adala?style=social) - Adala (Autonomous DAta Labeling Agent) is a framework for building autonomous data labeling and processing pipelines using LLMs as agents.
- [AgentFS](https://www.agentfs.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/tursodatabase/agentfs?style=social) - SDKs ship for TypeScript, Python, and Rust; a CLI mounts AgentFS via FUSE (Linux) or NFS (macOS).
- [agentUniverse](https://github.com/agentuniverse-ai/agentUniverse) ![GitHub Repo stars](https://img.shields.io/github/stars/agentuniverse-ai/agentUniverse?style=social) - AgentUniverse is a Python LLM multi-agent framework for building collaborative agent applications.
- [Agno](https://agno.com) ![GitHub Repo stars](https://img.shields.io/github/stars/agno-agi/agno?style=social) - Agno is a runtime or orchestration layer for agent applications.
- [AIOS](https://github.com/agiresearch/AIOS) ![GitHub Repo stars](https://img.shields.io/github/stars/agiresearch/AIOS?style=social) - AIOS - AI Agent Operating System.
- [Astron Agent](https://github.com/iflytek/astron-agent) ![GitHub Repo stars](https://img.shields.io/github/stars/iflytek/astron-agent?style=social) - Astron Agent is iFlyTek's enterprise agentic platform, a major player in the Chinese enterprise AI market.
- [Auto Deep Researcher 24x7](https://arxiv.org/abs/2604.05854) ![GitHub Repo stars](https://img.shields.io/github/stars/Xiangyue-Zhang/auto-deep-researcher-24x7?style=social) - Auto Deep Researcher 24x7 is an autonomous AI agent that runs deep learning experiments continuously (24/7) using a Leader-Worker architecture with constant-size memory.
- [AutoAgents](https://github.com/liquidos-ai/AutoAgents) ![GitHub Repo stars](https://img.shields.io/github/stars/liquidos-ai/AutoAgents?style=social) - AutoAgents is a Rust multi-agent framework from liquidos-ai for building, deploying, and coordinating multiple intelligent agents.
- [AutoGPT](https://agpt.co) ![GitHub Repo stars](https://img.shields.io/github/stars/Significant-Gravitas/AutoGPT?style=social) - The original autonomous agent harness.
- [AX (Agent Executor)](https://agentexecutor.io) ![GitHub Repo stars](https://img.shields.io/github/stars/google/ax?style=social) - AX (Agent eXecutor) is Google's open source distributed agent runtime, written in Go and licensed Apache-2.0.
- [BabyAGI](https://github.com/yoheinakajima/babyagi) ![GitHub Repo stars](https://img.shields.io/github/stars/yoheinakajima/babyagi?style=social) - BabyAGI is a runtime or orchestration layer for agent applications.
- [Back4app](https://www.back4app.com) ![GitHub Repo stars](https://img.shields.io/github/stars/parse-community/parse-server?style=social) - Back4app is a managed backend-as-a-service (BaaS) platform built on top of the open-source Parse Platform (parse-community/parse-server).
- [Bindu](https://docs.getbindu.com) ![GitHub Repo stars](https://img.shields.io/github/stars/GetBindu/Bindu?style=social) - Runtime layer that turns any AI agent into an interoperable, observable, composable microservice.
- [BrowserOS](https://browseros.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/browseros-ai/BrowserOS?style=social) - BrowserOS is an emerging agentic browser platform combining Chromium with AI agent capabilities.
- [Burr](https://burr.dagworks.io) ![GitHub Repo stars](https://img.shields.io/github/stars/apache/burr?style=social) - Apache-incubated Python framework for building decision-making applications (chatbots, agents, simulations) with first-class persistence and tracing.
- [Bytebot](https://bytebot.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/bytebot-ai/bytebot?style=social) - Computer-use AI agent platform enabling browser automation and desktop interaction.
- [Chidori](https://docs.thousandbirds.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/ThousandBirdsInc/chidori?style=social) - Unlike most Python/TypeScript agent frameworks, Chidori emphasizes reactive programming, time-travel debugging, and durable orchestration as first-class runtime primitives.
- [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk) ![GitHub Repo stars](https://img.shields.io/github/stars/anthropics/claude-agent-sdk-python?style=social) - Anthropic's official SDK for building production AI agents with Claude Code capabilities.
- [Claude Task Master](https://task-master.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/eyaltoledano/claude-task-master?style=social) - Claude Task Master is a runtime or orchestration layer for agent applications.
- [Composio Agent Orchestrator](https://github.com/ComposioHQ/agent-orchestrator) ![GitHub Repo stars](https://img.shields.io/github/stars/ComposioHQ/agent-orchestrator?style=social) - Composio Agent Orchestrator - agentic orchestrator for parallel coding agents.
- [Conductor](https://conductor-oss.org) ![GitHub Repo stars](https://img.shields.io/github/stars/conductor-oss/conductor?style=social) - Open-source workflow orchestration engine originally built at Netflix.
- [ControlFlow](https://github.com/prefect-archive/ControlFlow) ![GitHub Repo stars](https://img.shields.io/github/stars/prefect-archive/ControlFlow?style=social) - Workflow state rides on Prefect's own runtime.
- [Convex](https://www.convex.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/get-convex/convex-backend?style=social) - Convex is the open-source reactive database for app developers, now positioned as the backend building blocks for your agents.
- [CUA (Computer-Use Agent)](https://trycua.com) ![GitHub Repo stars](https://img.shields.io/github/stars/trycua/cua?style=social) - Open-source Computer-Use Agent infrastructure - sandboxes, SDKs, and benchmarks for agents that control macOS/Windows desktops.
- [CubeSandbox](https://cubesandbox.com) ![GitHub Repo stars](https://img.shields.io/github/stars/TencentCloud/CubeSandbox?style=social) - CubeSandbox is a high-performance, instant, concurrent, secure, and lightweight sandbox service for AI agents built by Tencent Cloud on RustVMM and KVM.
- [Dapr](https://dapr.io) ![GitHub Repo stars](https://img.shields.io/github/stars/dapr/dapr?style=social) - CNCF-graduated, vendor-neutral distributed application runtime providing building blocks for microservices and AI agents.
- [Dapr Agents](https://github.com/dapr/dapr-agents) ![GitHub Repo stars](https://img.shields.io/github/stars/dapr/dapr-agents?style=social) - Agent framework built on Dapr's durable workflow and actor model.
- [dimos](https://github.com/dimensionalOS/dimos) ![GitHub Repo stars](https://img.shields.io/github/stars/dimensionalOS/dimos?style=social) - Agentic operating system for physical hardware (humanoids, drones) supporting multi-agent coordination.
- [Dora](https://github.com/dora-rs/dora) ![GitHub Repo stars](https://img.shields.io/github/stars/dora-rs/dora?style=social) - Dora (Dataflow-Oriented Robotic Architecture) is middleware for building AI-based robotic applications.
- [E2B](https://e2b.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/e2b-dev/E2B?style=social) - Cloud sandbox infrastructure for AI agents - provides secure isolated execution environments for AI-generated code.
- [Eino](https://github.com/cloudwego/eino) ![GitHub Repo stars](https://img.shields.io/github/stars/cloudwego/eino?style=social) - Eino is ByteDance's production Go-based LLM application framework with composable retrieval, memory, and orchestration abstractions.
- [Eve](https://vercel.com/eve) ![GitHub Repo stars](https://img.shields.io/github/stars/vercel/eve?style=social) - Eve (The Framework for Building Agents) is Vercel's filesystem-first framework for durable AI agents, in public beta as of June 2026.
- [EvoAgentX](https://github.com/EvoAgentX/EvoAgentX) ![GitHub Repo stars](https://img.shields.io/github/stars/EvoAgentX/EvoAgentX?style=social) - Self-evolving multi-agent ecosystem that auto-generates and refines agent pipelines.
- [Flock](https://github.com/Onelevenvy/flock) ![GitHub Repo stars](https://img.shields.io/github/stars/Onelevenvy/flock?style=social) - Flock is a workflow-based low-code platform for rapidly building chatbots, RAG pipelines, and multi-agent teams.
- [Forge](https://github.com/antoinezambelli/forge) ![GitHub Repo stars](https://img.shields.io/github/stars/antoinezambelli/forge?style=social) - Forge is a runtime or orchestration layer for agent applications.
- [Gastown](https://gastownhall.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/gastownhall/gastown?style=social) - Each agent has its own context window and state; Gastown manages routing, scheduling, and inter-agent communication.
- [GenericAgent](https://github.com/lsdefine/GenericAgent) ![GitHub Repo stars](https://img.shields.io/github/stars/lsdefine/GenericAgent?style=social) - GenericAgent is a minimal (~3K lines), self-evolving autonomous agent framework.
- [GenSX](https://gensx.com) ![GitHub Repo stars](https://img.shields.io/github/stars/gensx-inc/gensx?style=social) - GenSX is a TypeScript framework for building agents and workflows using React-like component composition.
- [Google Antigravity SDK](https://antigravity.google/product/antigravity-sdk) ![GitHub Repo stars](https://img.shields.io/github/stars/google-antigravity/antigravity-sdk-python?style=social) - Google Antigravity SDK is an official Python SDK for building Antigravity/Gemini-powered agents.
- [Hatchet](https://hatchet.run) ![GitHub Repo stars](https://img.shields.io/github/stars/hatchet-dev/hatchet?style=social) - Hatchet - Orchestration engine for background tasks, AI agents, and durable workflows.
- [Helix](https://helix.ml) ![GitHub Repo stars](https://img.shields.io/github/stars/helixml/helix?style=social) - Private agent fleet runtime that provisions GPU-accelerated compute for each agent, supporting Claude, Codex, Gemini, and open models on a self-hosted AI stack.
- [HelixDB](https://www.helix-db.com) ![GitHub Repo stars](https://img.shields.io/github/stars/HelixDB/helix-db?style=social) - HelixDB is an open-source (Apache 2.0) OLTP graph-vector database built from scratch in Rust, positioned as a graph-vector database for knowledge graphs and AI memory.
- [holaOS](https://holaos.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/holaboss-ai/holaOS?style=social) - Open agent computer desktop harness (Electron, TypeScript) for any digital work - bundles an agent runtime with memory, MCP tool integration, and proactive workflows.
- [InsForge](https://insforge.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/InsForge/InsForge?style=social) - Open-source backend platform for agentic coding.
- [JoyAgent-JDGenie](https://github.com/jd-opensource/joyagent-jdgenie) ![GitHub Repo stars](https://img.shields.io/github/stars/jd-opensource/joyagent-jdgenie?style=social) - Production-grade universal multi-agent framework from JD.com.
- [KaibanJS](https://www.kaibanjs.com/) ![GitHub Repo stars](https://img.shields.io/github/stars/kaiban-ai/KaibanJS?style=social) - JavaScript-native multi-agent framework that applies Kanban-style workflow management to AI agent orchestration.
- [Kitaru](https://kitaru.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/zenml-io/kitaru?style=social) - Kitaru is a self-hosted, framework-agnostic runtime for production AI agents.
- [LangGraph](https://langchain-ai.github.io/langgraph) ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=social) - Durable execution runtime from the LangChain team; the primary way LangChain users build stateful, multi-step agents.
- [Letta](https://letta.com) ![GitHub Repo stars](https://img.shields.io/github/stars/letta-ai/letta?style=social) - Stateful agent execution runtime (formerly MemGPT) with persistent, editable memory architecture.
- [Magentic](https://magentic.dev/) ![GitHub Repo stars](https://img.shields.io/github/stars/jackmpcollins/magentic?style=social) - Community Python library that uses decorators to seamlessly integrate LLMs as regular Python functions - including structured outputs, tool calls, and async support.
- [Marvin](https://askmarvin.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/PrefectHQ/marvin?style=social) - Marvin is a runtime or orchestration layer for agent applications.
- [Memobase](https://memobase.io) ![GitHub Repo stars](https://img.shields.io/github/stars/memodb-io/memobase?style=social) - Memobase is a user-profile-based long-term memory layer for LLM chatbots - virtual companions, education, personalized assistants.
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) ![GitHub Repo stars](https://img.shields.io/github/stars/FoundationAgents/MetaGPT?style=social) - Opinionated multi-agent software engineering harness with pre-built roles (ProductManager/Engineer/Architect).
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/agent-framework?style=social) - Successor to AutoGen (microsoft/autogen, now deprecated - see migration guide).
- [Microsoft Promptflow](https://microsoft.github.io/promptflow) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/promptflow?style=social) - Microsoft's LLM app development toolkit for building, evaluating, and deploying prompt flows.
- [MLflow](https://mlflow.org) ![GitHub Repo stars](https://img.shields.io/github/stars/mlflow/mlflow?style=social) - MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models.
- [NanoClaw](https://nanoclaw.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/qwibitai/nanoclaw?style=social) - NanoClaw is a lightweight containerized AI assistant runtime that runs agents in isolated Linux containers for security.
- [NVIDIA OpenShell](https://docs.nvidia.com/openshell/latest/) ![GitHub Repo stars](https://img.shields.io/github/stars/NVIDIA/OpenShell?style=social) - Sandboxed execution runtime for autonomous AI agents from NVIDIA.
- [Omnigent](https://omnigent.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/omnigent-ai/omnigent?style=social) - Open-source meta-harness for orchestrating multiple AI coding agents (Claude Code, Codex, Cursor, OpenCode, Hermes, Gemini, custom).
- [Open Agents](https://open-agents.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/vercel-labs/open-agents?style=social) - Open source template/harness for building cloud agents from Vercel Labs.
- [Open-AutoGLM](https://autoglm.z.ai/blog) ![GitHub Repo stars](https://img.shields.io/github/stars/zai-org/Open-AutoGLM?style=social) - Open-AutoGLM is a runtime or orchestration layer for agent applications.
- [Open Multi-Agent](https://github.com/open-multi-agent/open-multi-agent) ![GitHub Repo stars](https://img.shields.io/github/stars/open-multi-agent/open-multi-agent?style=social) - TypeScript-native multi-agent orchestration framework.
- [OpenAgent](https://www.openagentai.org/) ![GitHub Repo stars](https://img.shields.io/github/stars/the-open-agent/openagent?style=social) - OpenAgent is an open-source, self-hostable personal AI assistant platform that ships as a single Go binary with no installation dependencies.
- [OpenFang](https://www.openfang.sh/) ![GitHub Repo stars](https://img.shields.io/github/stars/RightNow-AI/openfang?style=social) - OpenFang is an open-source Agent Operating System built in Rust (~137K LOC, 14 crates, single binary).
- [OpenViking](https://github.com/volcengine/OpenViking) ![GitHub Repo stars](https://img.shields.io/github/stars/volcengine/OpenViking?style=social) - Open-source context database from ByteDance's Volcengine implementing a three-tier (L0/L1/L2) hierarchical memory system for AI agents.
- [Ouroboros](https://github.com/Q00/ouroboros) ![GitHub Repo stars](https://img.shields.io/github/stars/Q00/ouroboros?style=social) - TypeScript/Python project that lets developers define agent behavior via structured specifications rather than freeform prompts - integrates with claude-code, codex-cli, and MCP.
- [OWL (CAMEL-AI)](https://github.com/camel-ai/owl) ![GitHub Repo stars](https://img.shields.io/github/stars/camel-ai/owl?style=social) - Opinionated, batteries-included multi-agent application from CAMEL-AI for real-world task automation.
- [PocketFlow](https://github.com/The-Pocket/PocketFlow) ![GitHub Repo stars](https://img.shields.io/github/stars/The-Pocket/PocketFlow?style=social) - Minimal 100-line Python LLM framework using nested directed graphs for multi-step agent tasks.
- [Pulumi](https://pulumi.com) ![GitHub Repo stars](https://img.shields.io/github/stars/pulumi/pulumi?style=social) - Pulumi is an infrastructure-as-code platform that sits outside the AI framework taxonomy.
- [Ragent](https://nageoffer.com/ragent) ![GitHub Repo stars](https://img.shields.io/github/stars/nageoffer/ragent?style=social) - Enterprise-grade Agentic RAG platform built with Spring Boot 3 and Java 17.
- [RD-Agent](https://rdagent.azurewebsites.net/) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/RD-Agent?style=social) - At it has significant reach.
- [Ruflo](https://flo.ruv.io/) ![GitHub Repo stars](https://img.shields.io/github/stars/ruvnet/ruflo?style=social) - Agent orchestration platform for Claude.
- [RushDB](https://rushdb.com) ![GitHub Repo stars](https://img.shields.io/github/stars/rush-db/rushdb?style=social) - RushDB is a runtime or orchestration layer for agent applications.
- [Skyvern](https://skyvern.com) ![GitHub Repo stars](https://img.shields.io/github/stars/Skyvern-AI/skyvern?style=social) - Skyvern automates browser-based workflows using AI vision and LLMs instead of brittle CSS selectors.
- [Solace Agent Mesh](https://solacelabs.github.io/solace-agent-mesh/) ![GitHub Repo stars](https://img.shields.io/github/stars/SolaceLabs/solace-agent-mesh?style=social) - Uses Solace's messaging/event-streaming infrastructure to connect AI agents with real-world data sources, enabling complex multi-step workflows via pub/sub patterns.
- [superdesign](https://superdesign.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/superdesigndev/superdesign?style=social) - AI product design agent - an opinionated harness for running design and coding tasks end-to-end via LLM agents.
- [Taipy](https://taipy.io) ![GitHub Repo stars](https://img.shields.io/github/stars/avaiga/taipy?style=social) - Avaiga (Orsay, France, founded 2020).
- [Temporal](https://temporal.io) ![GitHub Repo stars](https://img.shields.io/github/stars/temporalio/temporal?style=social) - Temporal is a durable workflow execution engine increasingly used as the persistence substrate for long-running AI agents and pipelines.
- [TensorZero](https://www.tensorzero.com) ![GitHub Repo stars](https://img.shields.io/github/stars/tensorzero/tensorzero?style=social) - LLM gateway and optimization runtime built in Rust.
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) ![GitHub Repo stars](https://img.shields.io/github/stars/TauricResearch/TradingAgents?style=social) - Multi-agent LLM framework for financial trading built on LangGraph.
- [Trigger.dev](https://trigger.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/triggerdotdev/trigger.dev?style=social) - Trigger.dev is a leading TypeScript-first durable execution platform for background jobs and AI workflows.
- [Upsonic](https://github.com/Upsonic/Upsonic) ![GitHub Repo stars](https://img.shields.io/github/stars/Upsonic/Upsonic?style=social) - Python agent framework purpose-built for enterprise/fintech use cases with a client-server architecture.
- [Vibe Kanban](https://bloop.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/BloopAI/vibe-kanban?style=social) - Vibe Kanban is an opinionated task orchestration harness for AI coding agents - notably Claude Code, Codex, and similar systems.
- [VoltAgent](https://github.com/VoltAgent/voltagent) ![GitHub Repo stars](https://img.shields.io/github/stars/VoltAgent/voltagent?style=social) - TypeScript-first AI agent engineering platform with observability-first design and visual debugging console.
- [Zep](https://getzep.com) ![GitHub Repo stars](https://img.shields.io/github/stars/getzep/zep?style=social) - Zep is a purpose-built long-term memory runtime for AI agents with a knowledge-graph-backed memory architecture.
- [ZeroClaw](https://zeroclawlabs.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/zeroclaw-labs/zeroclaw?style=social) - ZeroClaw is a fast, small, fully autonomous AI personal assistant infrastructure written in Rust.
- [Zerolang](https://zerolang.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/vercel-labs/zerolang?style=social) - Zerolang (the programming language for agents) is an experimental Vercel Labs project: a graph-native language where the semantic graph (zero.graph) is the program database.

<a id="rag-knowledge-system"></a>
## RAG / knowledge system

Product or framework centered on ingestion, indexing, retrieval, and search.

- [Augment Code](https://augmentcode.com) ![GitHub Repo stars](https://img.shields.io/github/stars/AugmentCode/augment-swebench-agent?style=social) - The platform maintains long-term developer memory and preferences across sessions.
- [BeeAI Framework](https://framework.beeai.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/i-am-bee/beeai-framework?style=social) - BeeAI Framework is an open-source (Apache 2.0) framework for building production-ready multi-agent systems, with first-class parity across Python and TypeScript.
- [Boxcars](https://github.com/BoxcarsAI/boxcars) ![GitHub Repo stars](https://img.shields.io/github/stars/BoxcarsAI/boxcars?style=social) - Ruby AI framework focused on composable boxcars (chains/tools) with LLM backends.
- [Cognee](https://cognee.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/topoteretes/cognee?style=social) - Knowledge engine for AI agent memory using knowledge graphs -, active weekly development (trending Apr 2026).
- [Cognita](https://cognita.truefoundry.com) ![GitHub Repo stars](https://img.shields.io/github/stars/truefoundry/cognita?style=social) - Open-source modular RAG framework with a web UI.
- [ContextGem](https://contextgem.dev/) ![GitHub Repo stars](https://img.shields.io/github/stars/shcherbak-ai/contextgem?style=social) - Positioned alongside Unstructured, MegaParse, and PageIndex in the document-processing/extraction layer.
- [CowAgent](https://cowagent.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/zhayujie/CowAgent?style=social) - Open-source super AI assistant and agent harness with task planning, three-tier memory architecture (context daily core), personal knowledge base, and skill marketplace.
- [DocArray](https://docarray.jina.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/docarray/docarray?style=social) - Multimodal data representation library for AI pipelines with pluggable document store backends.
- [DSPy](https://dspy.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/stanfordnlp/dspy?style=social) - DSPy supports retrieval, knowledge, or grounding workflows for agent applications.
- [Eliza](https://elizaos.github.io/eliza/) ![GitHub Repo stars](https://img.shields.io/github/stars/elizaos/eliza?style=social) - Multi-agent simulation framework for autonomous AI agents, originally popularized by ai16z.
- [Embabel](https://github.com/embabel/embabel-agent) ![GitHub Repo stars](https://img.shields.io/github/stars/embabel/embabel-agent?style=social) - Embabel - Agent framework for the JVM.
- [Firebase Genkit](https://firebase.google.com/docs/genkit) ![GitHub Repo stars](https://img.shields.io/github/stars/genkit-ai/genkit?style=social) - Genkit is Google's production-backed open-source AI app framework for JS/Go/Python.
- [GraphRAG](https://microsoft.github.io/graphrag/) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/graphrag?style=social) - Builds a knowledge graph from source documents using LLMs, enabling global and local search queries that traverse entity relationships.
- [Griptape](https://www.griptape.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/griptape-ai/griptape?style=social) - Modular Python agent framework with strict separation of concerns.
- [Haystack](https://haystack.deepset.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/deepset-ai/haystack?style=social) - Production-grade NLP/RAG framework from deepset.
- [HolmesGPT](https://holmesgpt.com) ![GitHub Repo stars](https://img.shields.io/github/stars/HolmesGPT/holmesgpt?style=social) - HolmesGPT automatically investigates alerts by querying observability data (Prometheus, Grafana, Datadog, etc.) and generates root cause analysis.
- [Jina AI](https://jina.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/jina-ai/serve?style=social) - Neural search and embedding framework by Jina AI.
- [k8sGPT](https://k8sgpt.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/k8sgpt-ai/k8sgpt?style=social) - CNCF Sandbox project. k8sGPT scans Kubernetes clusters, surfaces problems in plain English, and uses LLMs to suggest fixes.
- [LangChain](https://python.langchain.com) ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=social) - The dominant LLM application framework.
- [LangChain Elixir](https://github.com/brainlid/langchain) ![GitHub Repo stars](https://img.shields.io/github/stars/brainlid/langchain?style=social) - LangChain Elixir - Elixir implementation of a LangChain-style framework that lets Elixir projects integrate with and leverage LLMs.
- [LangChain Go](https://github.com/tmc/langchaingo) ![GitHub Repo stars](https://img.shields.io/github/stars/tmc/langchaingo?style=social) - Community-maintained Go port of LangChain, implementing the core abstractions - chains, agents, tools, vector stores, memory - in idiomatic Go.
- [LangChain.js](https://js.langchain.com) ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langchainjs?style=social) - The official TypeScript/JavaScript port of LangChain.
- [Langchain.rb](https://github.com/patterns-ai-core/langchainrb) ![GitHub Repo stars](https://img.shields.io/github/stars/patterns-ai-core/langchainrb?style=social) - Ruby port of LangChain with vectorstore, memory, and tool abstractions.
- [LangChain4j](https://docs.langchain4j.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/langchain4j/langchain4j?style=social) - The leading Java/Kotlin LLM integration library.
- [Langroid](https://langroid.github.io/langroid/) ![GitHub Repo stars](https://img.shields.io/github/stars/langroid/langroid?style=social) - Multi-agent LLM framework with a task-delegation architecture.
- [Laravel AI](https://laravel.com/docs/ai) ![GitHub Repo stars](https://img.shields.io/github/stars/laravel/ai?style=social) - The Laravel AI SDK provides a unified, expressive API for interacting with AI providers (OpenAI, Anthropic, Gemini).
- [LightRAG](https://github.com/HKUDS/LightRAG) ![GitHub Repo stars](https://img.shields.io/github/stars/HKUDS/LightRAG?style=social) - LightRAG is a graph-based RAG framework combining knowledge graphs with vector retrieval.
- [LlamaIndex](https://www.llamaindex.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/run-llama/llama_index?style=social) - Major RAG and data framework; strong in enterprise knowledge retrieval use cases.
- [LLPhant](https://github.com/LLPhant/LLPhant) ![GitHub Repo stars](https://img.shields.io/github/stars/LLPhant/LLPhant?style=social) - PHP-native generative AI framework with LangChain-inspired abstractions for RAG, memory, and tool use.
- [Local Deep Research](https://github.com/LearningCircuit/local-deep-research) ![GitHub Repo stars](https://img.shields.io/github/stars/LearningCircuit/local-deep-research?style=social) - LLM-powered deep research tool achieving ~95% on SimpleQA benchmarks.
- [Local Deep Researcher](https://github.com/langchain-ai/local-deep-researcher) ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/local-deep-researcher?style=social) - Local Deep Researcher is a fully local web research and report-writing assistant built on LangGraph.
- [LocalGPT](https://github.com/PromtEngineer/localGPT) ![GitHub Repo stars](https://img.shields.io/github/stars/PromtEngineer/localGPT?style=social) - Local RAG application for private document Q&A.
- [MiroThinker](https://github.com/MiroMindAI/MiroThinker) ![GitHub Repo stars](https://img.shields.io/github/stars/MiroMindAI/MiroThinker?style=social) - Opinionated deep research agent harness achieving top benchmark scores.
- [Nexa SDK](https://nexa.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/nexaai/nexa-sdk?style=social) - Nexa AI (San Jose, founded 2023, $16.5M raised) provides an SDK for running models locally on CPU/GPU/Apple Silicon without cloud dependency.
- [Open Notebook](https://www.open-notebook.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/lfnovo/open-notebook?style=social) - Open Notebook is an open-source NotebookLM-style research and note-taking harness.
- [PageIndex](https://pageindex.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/VectifyAI/PageIndex?style=social) - Repo created April 2025 and grew to in under a year.
- [PentAGI](https://pentagi.com) ![GitHub Repo stars](https://img.shields.io/github/stars/vxcontrol/pentagi?style=social) - PentAGI is a fully autonomous AI agent system for penetration testing, capable of performing complex security assessments end-to-end.
- [PrivateGPT](https://privategpt.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/zylon-ai/private-gpt?style=social) - The pluggable backend architecture means an integration is technically feasible.
- [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) ![GitHub Repo stars](https://img.shields.io/github/stars/QwenLM/Qwen-Agent?style=social) - Qwen-Agent is Alibaba's official agent framework built on the Qwen model family, supporting function calling, MCP, RAG, and code interpretation.
- [RAG-Anything](https://github.com/HKUDS/RAG-Anything) ![GitHub Repo stars](https://img.shields.io/github/stars/HKUDS/RAG-Anything?style=social) - Handles diverse content types including text, images, tables, equations, and charts through a unified retrieval interface.
- [Rasa](https://rasa.com) ![GitHub Repo stars](https://img.shields.io/github/stars/RasaHQ/rasa?style=social) - Rasa is a mature open-source conversational AI harness with pluggable tracker stores and NLU backends.
- [Rig](https://rig.rs) ![GitHub Repo stars](https://img.shields.io/github/stars/0xPlaygrounds/rig?style=social) - Rig - Rust framework for building modular and scalable LLM applications.
- [ScrapeGraphAI](https://scrapegraphai.com) ![GitHub Repo stars](https://img.shields.io/github/stars/scrapegraphai/scrapegraph-ai?style=social) - AI-powered web scraping pipeline framework using LLMs to extract structured data.
- [TaskingAI](https://www.tasking.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/TaskingAI/TaskingAI?style=social) - TaskingAI - The open source platform for AI-native application development.
- [txtai](https://neuml.github.io/txtai/) ![GitHub Repo stars](https://img.shields.io/github/stars/neuml/txtai?style=social) - All-in-one embeddings database, LLM orchestration, and semantic search framework.
- [TypedAI](https://github.com/TrafficGuard/typedai) ![GitHub Repo stars](https://img.shields.io/github/stars/TrafficGuard/typedai?style=social) - TypedAI - TypeScript AI platform with AI chat, autonomous agents, software developer agents, chatbots and more.
- [Vanna AI](https://vanna.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/vanna-ai/vanna?style=social) - Text-to-SQL framework using RAG (Retrieval-Augmented Generation).
- [WeKnora](https://weknora.weixin.qq.com) ![GitHub Repo stars](https://img.shields.io/github/stars/Tencent/WeKnora?style=social) - LLM-powered framework for deep document understanding, semantic retrieval, and context-aware answers using the RAG paradigm.
- [WrenAI](https://getwren.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/Canner/WrenAI?style=social) - WrenAI lets users query any database in natural language and generate charts/dashboards.

<a id="memory-context-system"></a>
## Memory / context system

Long-term memory, profile state, context graph, or recall layer.

- [A-MEM](https://github.com/agiresearch/A-mem) ![GitHub Repo stars](https://img.shields.io/github/stars/agiresearch/A-mem?style=social) - Two related repos exist: agiresearch/A-mem and WujiangXu/AgenticMemory.
- [Accomplish](https://accomplish.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/accomplish-ai/coworker?style=social) - AccomplishTM is an open-source AI coworker that lives on the desktop.
- [Agency Swarm](https://vrsen.github.io/agency-swarm) ![GitHub Repo stars](https://img.shields.io/github/stars/VRSEN/agency-swarm?style=social) - Open-source framework for building structured, reliable AI agent networks where each agent has clearly defined roles and communication channels.
- [Agent S](https://github.com/simular-ai/Agent-S) ![GitHub Repo stars](https://img.shields.io/github/stars/simular-ai/Agent-S?style=social) - Open GUI automation agent framework from Simular AI.
- [Agent Zero](https://github.com/agent0ai/agent-zero) ![GitHub Repo stars](https://img.shields.io/github/stars/agent0ai/agent-zero?style=social) - Designed as a personal AI assistant that orchestrates other agents, uses tools, executes code, and builds dynamic memory.
- [AgentDock](https://github.com/AgentDock/AgentDock) ![GitHub Repo stars](https://img.shields.io/github/stars/AgentDock/AgentDock?style=social) - AgentDock is a general-purpose Build Anything with AI Agents framework.
- [AgentGPT](https://agentgpt.reworkd.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/reworkd/AgentGPT?style=social) - Web-based autonomous AI agent platform.
- [Agentic Context Engine](https://kayba.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/kayba-ai/agentic-context-engine?style=social) - Company-led (Kayba) with a hosted commercial offering adjacent to the OSS core.
- [Agentic Stack](https://github.com/codejunkie99/agentic-stack) ![GitHub Repo stars](https://img.shields.io/github/stars/codejunkie99/agentic-stack?style=social) - Includes a local data layer for monitoring harness activity, cron runs, token/cost estimates, and dashboard exports.
- [Agently](https://agently.tech) ![GitHub Repo stars](https://img.shields.io/github/stars/AgentEra/Agently?style=social) - Structured data chaining, multi-LLM support.
- [AgentScope Java](https://java.agentscope.io/) ![GitHub Repo stars](https://img.shields.io/github/stars/agentscope-ai/agentscope-java?style=social) - Java port of Alibaba's AgentScope framework for building LLM applications using an agent-oriented programming model.
- [Aperant](https://aperant.com) ![GitHub Repo stars](https://img.shields.io/github/stars/AndyMik90/Aperant?style=social) - Aperant (formerly Auto Claude) is an autonomous multi-agent coding framework with Kanban-based task planning and validation.
- [Archon](https://github.com/coleam00/Archon) ![GitHub Repo stars](https://img.shields.io/github/stars/coleam00/Archon?style=social) - Archon is an AI agent that builds other AI agents by generating and iterating on complete agent codebases.
- [Atomic Agents](https://github.com/BrainBlend-AI/atomic-agents) ![GitHub Repo stars](https://img.shields.io/github/stars/BrainBlend-AI/atomic-agents?style=social) - Lightweight modular agent framework built on Pydantic.
- [Beads](https://github.com/gastownhall/beads) ![GitHub Repo stars](https://img.shields.io/github/stars/gastownhall/beads?style=social) - Beads is a Go-based memory upgrade layer for coding agents.
- [ByteRover](https://docs.byterover.dev/) ![GitHub Repo stars](https://img.shields.io/github/stars/campfirein/byterover-cli?style=social) - ByteRover CLI (brv) - portable memory layer for autonomous coding agents (formerly Cipher).
- [Cheshire Cat AI](https://cheshirecat.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/cheshire-cat-ai/core?style=social) - Cheshire Cat provides a production-ready, plugin-based AI agent server with memory, tool use, and RAG over personal/organizational documents.
- [CopilotKit](https://www.copilotkit.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/CopilotKit/CopilotKit?style=social) - Frontend SDK for building agent-native UI in React.
- [Craft Agents](https://agents.craft.do) ![GitHub Repo stars](https://img.shields.io/github/stars/lukilabs/craft-agents-oss?style=social) - Opinionated desktop agent harness built by Craft (craft.do), the document editor company.
- [Crush](https://github.com/charmbracelet/crush) ![GitHub Repo stars](https://img.shields.io/github/stars/charmbracelet/crush?style=social) - Crush - Glamourous agentic coding for all.
- [DB-GPT](https://docs.dbgpt.site) ![GitHub Repo stars](https://img.shields.io/github/stars/eosphoros-ai/DB-GPT?style=social) - Open-source agentic AI data assistant targeting AI + Data product builders.
- [Dexter](https://github.com/virattt/dexter) ![GitHub Repo stars](https://img.shields.io/github/stars/virattt/dexter?style=social) - Autonomous agent for deep financial research.
- [Dust](https://dust.tt) ![GitHub Repo stars](https://img.shields.io/github/stars/dust-tt/dust?style=social) - Hosted multi-agent platform for enterprises to build custom AI agents that automate internal workflows.
- [Emdash](https://emdash.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/generalaction/emdash?style=social) - Open-source agentic development environment for running multiple coding agents in parallel.
- [Engram](https://github.com/Gentleman-Programming/engram) ![GitHub Repo stars](https://img.shields.io/github/stars/Gentleman-Programming/engram?style=social) - Engram - persistent memory system for AI coding agents, agent-agnostic.
- [EverOS](https://evermind.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/EverMind-AI/EverOS?style=social) - EverOS - memory-layer framework for building, evaluating, and integrating long-term memory for self-evolving agents.
- [FinRobot](https://finrobot.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/AI4Finance-Foundation/FinRobot?style=social) - FinRobot is an open-source AI agent platform for financial analysis using LLMs, developed by the AI4Finance Foundation (an open-source community organization).
- [GBrain](https://github.com/garrytan/gbrain) ![GitHub Repo stars](https://img.shields.io/github/stars/garrytan/gbrain?style=social) - Self-wiring knowledge graph and brain for AI agents.
- [GPT-Researcher](https://gptr.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/assafelovic/gpt-researcher?style=social) - GPT-Researcher is a batteries-included autonomous research agent that retrieves, synthesizes, and persists research outputs.
- [Graphiti](https://github.com/getzep/graphiti) ![GitHub Repo stars](https://img.shields.io/github/stars/getzep/graphiti?style=social) - Real-time knowledge graph framework for AI agents by Zep.
- [Hive](https://adenhq.com) ![GitHub Repo stars](https://img.shields.io/github/stars/aden-hive/hive?style=social) - Explicitly self-describes as a Multi-Agent Harness for Production AI.
- [Honcho](https://honcho.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/plastic-labs/honcho?style=social) - Honcho provides memory or context management for agent applications.
- [IntentKit](https://github.com/crestalnetwork/intentkit) ![GitHub Repo stars](https://img.shields.io/github/stars/crestalnetwork/intentkit?style=social) - Agent framework for building specialized skill-based AI agents.
- [JARVIS (HuggingGPT)](https://github.com/microsoft/JARVIS) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/JARVIS?style=social) - Microsoft Research prototype (HuggingGPT) - LLM as controller, routes tasks to specialized Hugging Face models.
- [Khoj](https://khoj.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/khoj-ai/khoj?style=social) - Supports RAG over personal notes (Obsidian, Notion, email, etc.), persistent agent memory, and web search.
- [Lagent](https://lagent.readthedocs.io) ![GitHub Repo stars](https://img.shields.io/github/stars/InternLM/lagent?style=social) - Lagent provides clean abstractions for agent workflows including tool calling, memory, and multi-agent coordination.
- [LangMem](https://langchain-ai.github.io/langmem/) ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langmem?style=social) - Memory tools (create_manage_memory_tool, create_search_memory_tool) are designed to be added to any LangGraph agent via create_react_agent.
- [LaVague](https://lavague.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/lavague-ai/LaVague?style=social) - LaVague enables building web automation agents using natural language instructions and vision models.
- [LiveKit Agents](https://docs.livekit.io/agents/) ![GitHub Repo stars](https://img.shields.io/github/stars/livekit/agents?style=social) - Framework for building real-time voice AI agents on WebRTC infrastructure (LiveKit).
- [mem0](https://mem0.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/mem0ai/mem0?style=social) - Dedicated memory layer for AI applications; adds persistent, personalized memory across conversations and agents.
- [memary](https://github.com/kingjulio8238/memary) ![GitHub Repo stars](https://img.shields.io/github/stars/kingjulio8238/memary?style=social) - Memary is an open-source memory layer for autonomous agents, providing episodic, semantic, and profile memory capabilities.
- [MemMachine](https://memmachine.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/MemMachine/MemMachine?style=social) - MemMachine - universal memory layer for AI agents, providing scalable, extensible, and interoperable memory storage and retrieval.
- [Memoir](https://www.memoir-ai.dev/) ![GitHub Repo stars](https://img.shields.io/github/stars/zhangfengcdt/memoir?style=social) - Alpha-stage semantic memory framework for AI agents with a Git-like versioning model (branch / commit / merge / rollback on memory stores).
- [Memori](https://memorilabs.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/MemoriLabs/Memori?style=social) - Persistent memory framework for LLM applications and AI agents (Memori Labs, New York, founded 2024, $3.7M raised).
- [MemoryOS](https://baijia.online/memoryos/) ![GitHub Repo stars](https://img.shields.io/github/stars/BAI-LAB/MemoryOS?style=social) - Architecture borrows from OS memory management: hierarchical short-term / mid-term / long-term persona memory with four core modules - Storage, Updating, Retrieval, Generation.
- [MemOS](https://memos.openmem.net) ![GitHub Repo stars](https://img.shields.io/github/stars/MemTensor/MemOS?style=social) - MemOS (Memory Operating System) is a framework for persistent skill and context memory in LLM and agent systems.
- [MemPalace](https://github.com/MemPalace/mempalace) ![GitHub Repo stars](https://img.shields.io/github/stars/MemPalace/mempalace?style=social) - MemPalace - The best-benchmarked open-source AI memory system.
- [Memsearch](https://zilliztech.github.io/memsearch/) ![GitHub Repo stars](https://img.shields.io/github/stars/zilliztech/memsearch?style=social) - , created Feb 2026 - rapid early growth.
- [memU](https://memu.pro) ![GitHub Repo stars](https://img.shields.io/github/stars/NevaMind-AI/memU?style=social) - MemU is a memory framework for 24/7 proactive agents built by NevaMind AI, positioned as the OpenClaw alternative.
- [Memvid](https://www.memvid.com) ![GitHub Repo stars](https://img.shields.io/github/stars/memvid/memvid?style=social) - Memory layer for AI agents that replaces complex RAG pipelines with a serverless, single-file memory layer designed for instant retrieval and long-term memory.
- [ML Intern](https://github.com/huggingface/ml-intern) ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/ml-intern?style=social) - ML Intern - an open-source ML engineer agent from Hugging Face that reads papers, trains models, and ships ML models.
- [OGX (formerly Llama Stack)](https://ogx-ai.github.io/) ![GitHub Repo stars](https://img.shields.io/github/stars/ogx-ai/ogx?style=social) - OGX is the rebrand of Meta's Llama Stack - announced 2026-04-30 with the blog post From Llama Stack to OGX.
- [Open Interpreter](https://openinterpreter.com) ![GitHub Repo stars](https://img.shields.io/github/stars/openinterpreter/openinterpreter?style=social) - Open Interpreter is one of the largest open-source AI agent harnesses, widely used for local code execution and computer control.
- [OpenAgents](https://github.com/xlang-ai/OpenAgents) ![GitHub Repo stars](https://img.shields.io/github/stars/xlang-ai/OpenAgents?style=social) - XLANG Lab (COLM 2024 paper).
- [OpenAI Swarm](https://github.com/openai/swarm) ![GitHub Repo stars](https://img.shields.io/github/stars/openai/swarm?style=social) - Swarm is OpenAI's lightweight experimental multi-agent orchestration framework with minimal built-in persistence.
- [OpenClaw](https://openclaw.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/openclaw/openclaw?style=social) - Openclaw/openclaw is a consumer-grade AI personal assistant app that connects to messaging platforms (WhatsApp, Telegram, Slack, iMessage) via a local Gateway.
- [Osaurus](https://osaurus.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/osaurus-ai/osaurus?style=social) - Because it targets on-device macOS usage, the memory/session layer is local by default.
- [Parlant](https://www.parlant.io) ![GitHub Repo stars](https://img.shields.io/github/stars/emcie-co/parlant?style=social) - Developers define declarative guidelines that shape agent behavior without prompt engineering.
- [Pipecat](https://www.pipecat.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/pipecat-ai/pipecat?style=social) - Open-source framework for building voice and multimodal conversational AI agents.
- [PraisonAI](https://docs.praison.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/MervinPraison/PraisonAI?style=social) - Self-reflection and self-reasoning multi-agent AI framework built on CrewAI and AutoGen, combining them with a YAML-based configuration layer.
- [RedPlanetHQ Core](https://getcore.me) ![GitHub Repo stars](https://img.shields.io/github/stars/RedPlanetHQ/core?style=social) - AI butler agent harness (TypeScript/Remix stack, Node.js) that orchestrates personal productivity workflows.
- [Rivet](https://rivet.ironcladapp.com) ![GitHub Repo stars](https://img.shields.io/github/stars/Ironclad/rivet?style=social) - Rivet provides a node-based graph editor for building AI agent workflows, with both a visual interface and a programmatic TypeScript SDK.
- [Rowboat](https://rowboatlabs.com) ![GitHub Repo stars](https://img.shields.io/github/stars/rowboatlabs/rowboat?style=social) - Open-source AI coworker with persistent memory and MCP (Model Context Protocol) tool support.
- [Screenpipe](https://screenpi.pe) ![GitHub Repo stars](https://img.shields.io/github/stars/screenpipe/screenpipe?style=social) - Founded 2024 (US, San Francisco).
- [Second Me](https://home.second.me/) ![GitHub Repo stars](https://img.shields.io/github/stars/mindverse/Second-Me?style=social) - Second Me is a personal AI training and memory framework that lets users train a local AI model on their own data to create a persistent personal AI self.
- [Stakpak Agent](https://github.com/stakpak/agent) ![GitHub Repo stars](https://img.shields.io/github/stars/stakpak/agent?style=social) - Stakpak Agent - open source agent that lives on your machines 24/7 and keeps your apps running (Ship your code, on autopilot).
- [STORM](https://github.com/stanford-oval/storm) ![GitHub Repo stars](https://img.shields.io/github/stars/stanford-oval/storm?style=social) - Generates Wikipedia-style articles from internet research by conducting multi-perspective conversations and synthesizing results.
- [Suna](https://suna.so) ![GitHub Repo stars](https://img.shields.io/github/stars/kortix-ai/suna?style=social) - Open-source generalist AI agent harness with browser automation, file system, shell, and web action capabilities.
- [SuperDuper](https://superduper.io) ![GitHub Repo stars](https://img.shields.io/github/stars/superduper-io/superduper?style=social) - Rebranded from SuperDuperDB to SuperDuper in late 2024; repo moved from superduperdb/superduperdb to superduper-io/superduper.
- [Supermemory](https://supermemory.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/supermemoryai/supermemory?style=social) - Memory and context engine for AI agents.
- [Swarms](https://swarms.world) ![GitHub Repo stars](https://img.shields.io/github/stars/kyegomez/swarms?style=social) - Designed for production deployment of large agent fleets.
- [Tambo](https://tambo.co) ![GitHub Repo stars](https://img.shields.io/github/stars/tambo-ai/tambo?style=social) - Tambo is a generative UI SDK for React that connects UI components to AI agents with streaming, state management, and MCP integration.
- [TaskWeaver](https://microsoft.github.io/TaskWeaver/) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/TaskWeaver?style=social) - Code-first agent framework for data analytics - from Microsoft Research.
- [TEN Framework](https://theten.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/TEN-framework/ten-framework?style=social) - TEN (The Extension Network) provides a real-time, low-latency multimodal agent runtime for voice, video, and text interactions.
- [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) ![GitHub Repo stars](https://img.shields.io/github/stars/TencentCloud/TencentDB-Agent-Memory?style=social) - TencentDB Agent Memory provides memory or context management for agent applications.
- [uAgents](https://fetch.ai/docs/guides/agents) ![GitHub Repo stars](https://img.shields.io/github/stars/fetchai/uAgents?style=social) - Agents persist state using a local storage backend.

<a id="low-code-builder-agent-app"></a>
## Low-code builder / agent app

Visual builder, packaged chat/RAG app, or batteries-included application surface.

- [Activepieces](https://www.activepieces.com) ![GitHub Repo stars](https://img.shields.io/github/stars/activepieces/activepieces?style=social) - AI-native with MCP toolkit support, 280+ pre-built integrations, a no-code visual builder, and a TypeScript extension framework for custom pieces.
- [AnythingLLM](https://anythingllm.com) ![GitHub Repo stars](https://img.shields.io/github/stars/Mintplex-Labs/anything-llm?style=social) - AnythingLLM is a batteries-included local RAG application with pluggable vector and document store backends.
- [AstrBot](https://astrbot.app) ![GitHub Repo stars](https://img.shields.io/github/stars/AstrBotDevs/AstrBot?style=social) - AI Agent assistant and development framework integrating multiple IM platforms (QQ, Discord, Telegram, WeChat).
- [BiSheng](https://bisheng.dataelem.com) ![GitHub Repo stars](https://img.shields.io/github/stars/dataelement/bisheng?style=social) - Enterprise LLM DevOps platform (Chinese-market) -, actively maintained.
- [Botpress](https://botpress.com) ![GitHub Repo stars](https://img.shields.io/github/stars/botpress/botpress?style=social) - Open-source platform to build and deploy GPT/LLM-powered agents, chatbots, and voice assistants.
- [Casibase](https://casibase.org) ![GitHub Repo stars](https://img.shields.io/github/stars/casibase/casibase?style=social) - Casibase is an open-source enterprise-level AI knowledge base and MCP/A2A management platform.
- [Chainlit](https://chainlit.io) ![GitHub Repo stars](https://img.shields.io/github/stars/Chainlit/chainlit?style=social) - Python framework for building conversational AI applications with a built-in chat UI.
- [ChatDev](https://chatdev.toscl.com) ![GitHub Repo stars](https://img.shields.io/github/stars/OpenBMB/ChatDev?style=social) - Multi-agent software development simulation framework from Tsinghua University / OpenBMB.
- [Coze Studio](https://www.coze.com) ![GitHub Repo stars](https://img.shields.io/github/stars/coze-dev/coze-studio?style=social) - Open-source AI agent and workflow development platform from ByteDance/Coze.
- [DeepChat](https://deepchat.thinkinai.xyz/) ![GitHub Repo stars](https://img.shields.io/github/stars/thinkinaixyz/deepchat?style=social) - DeepChat is an open-source AI agent platform desktop application (Electron/TypeScript) that unifies models, tools, and agents.
- [DeerFlow](https://github.com/bytedance/deer-flow) ![GitHub Repo stars](https://img.shields.io/github/stars/bytedance/deer-flow?style=social) - Open-source long-horizon SuperAgent harness by ByteDance.
- [Dify](https://dify.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/langgenius/dify?style=social) - The platform's architecture explicitly externalizes storage - users configure their own vector store, document store, and session/conversation persistence backends.
- [DocsGPT](https://docsgpt.cloud) ![GitHub Repo stars](https://img.shields.io/github/stars/arc53/DocsGPT?style=social) - DocsGPT is a self-hosted document Q&A and enterprise search platform with built-in agent builder and multi-model support.
- [FastGPT](https://fastgpt.in) ![GitHub Repo stars](https://img.shields.io/github/stars/labring/FastGPT?style=social) - Knowledge-base-powered LLM application platform built on RAG + workflow orchestration.
- [Flowise](https://flowiseai.com) ![GitHub Repo stars](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=social) - Drag-and-drop LLM app builder with broad connector ecosystem.
- [GoClaw](https://goclaw.sh) ![GitHub Repo stars](https://img.shields.io/github/stars/nextlevelbuilder/goclaw?style=social) - GoClaw is a Go-based multi-agent gateway and platform derived from OpenClaw patterns.
- [Langflow](https://www.langflow.org) ![GitHub Repo stars](https://img.shields.io/github/stars/langflow-ai/langflow?style=social) - Langflow is a low-code visual harness for building AI applications and multi-agent pipelines built on top of LangChain, with making it the largest-star repository in this batch.
- [LibreChat](https://librechat.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/danny-avila/LibreChat?style=social) - Open-source ChatGPT-like platform supporting 30+ LLM providers (OpenAI, Claude, Gemini, local models).
- [LobeChat](https://lobechat.com) ![GitHub Repo stars](https://img.shields.io/github/stars/lobehub/lobehub?style=social) - LobeChat is one of the highest-starred open-source LLM chat platforms with a built-in knowledge base and RAG pipeline.
- [MaxKB](https://maxkb.com) ![GitHub Repo stars](https://img.shields.io/github/stars/1Panel-dev/MaxKB?style=social) - MaxKB is the leading enterprise AI knowledge base platform in the Chinese developer ecosystem, with broad enterprise deployments and growing international adoption.
- [MLE-Agent](https://mle-agent-site.vercel.app/) ![GitHub Repo stars](https://img.shields.io/github/stars/MLSysOps/MLE-agent?style=social) - MLE-Agent is a Python CLI-based AI pairing agent for machine learning engineers.
- [n8n](https://n8n.io) ![GitHub Repo stars](https://img.shields.io/github/stars/n8n-io/n8n?style=social) - Open-source workflow automation platform (400+ integrations) with a first-class AI/agent node cluster built on LangChain.
- [NocoBase](https://www.nocobase.com) ![GitHub Repo stars](https://img.shields.io/github/stars/nocobase/nocobase?style=social) - NocoBase is an open-source AI + no-code platform for building business systems.
- [Onyx](https://www.onyx.app) ![GitHub Repo stars](https://img.shields.io/github/stars/onyx-dot-app/onyx?style=social) - Open-source enterprise search and AI assistant with RAG, document connectors, and chat (formerly Danswer).
- [Open WebUI](https://openwebui.com) ![GitHub Repo stars](https://img.shields.io/github/stars/open-webui/open-webui?style=social) - Extensible, self-hosted AI interface platform with - one of the largest open-source AI projects by adoption.
- [RAGFlow](https://ragflow.io) ![GitHub Repo stars](https://img.shields.io/github/stars/infiniflow/ragflow?style=social) - The system is architected around pluggable storage backends for both the vector index and the document/chunk store.
- [SillyTavern](https://sillytavern.app) ![GitHub Repo stars](https://img.shields.io/github/stars/SillyTavern/SillyTavern?style=social) - LLM frontend for power users.
- [Sim Studio](https://simstudio.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/simstudioai/sim?style=social) - Open-source AI agent workflow builder and simulation platform.
- [WiseFlow](https://github.com/TeamWiseFlow/wiseflow) ![GitHub Repo stars](https://img.shields.io/github/stars/TeamWiseFlow/wiseflow?style=social) - Multi-agent RPA and information extraction system.

<a id="tool-protocol-connector-layer"></a>
## Tool / protocol / connector layer

MCP, A2A, tool registry, auth broker, connector catalog, or action metadata layer.

- [A2A (Agent2Agent Protocol)](https://a2a-protocol.org) ![GitHub Repo stars](https://img.shields.io/github/stars/a2aproject/A2A?style=social) - Agent-to-Agent (A2A) is an open protocol for inter-agent communication and interoperability.
- [AG-UI Protocol](https://docs.ag-ui.com) ![GitHub Repo stars](https://img.shields.io/github/stars/ag-ui-protocol/ag-ui?style=social) - Open protocol and SDK for connecting AI agents to frontend applications.
- [Agentic](https://agentic.so) ![GitHub Repo stars](https://img.shields.io/github/stars/transitive-bullshit/agentic?style=social) - Agentic - Your API Paid MCP.
- [Appwrite](https://appwrite.io) ![GitHub Repo stars](https://img.shields.io/github/stars/appwrite/appwrite?style=social) - MariaDB is the alternative.
- [Arcade.dev](https://arcade.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/ArcadeAI/arcade-mcp?style=social) - Repo recently renamed from arcade-ai to arcade-mcp, reflecting a pivot toward the MCP ecosystem.
- [ByteChef](https://www.bytechef.io) ![GitHub Repo stars](https://img.shields.io/github/stars/bytechefhq/bytechef?style=social) - Open-source AI agent orchestration and workflow automation platform (alternative to Zapier/n8n/Workato).
- [Composio](https://github.com/ComposioHQ/composio) ![GitHub Repo stars](https://img.shields.io/github/stars/ComposioHQ/composio?style=social) - Composio provides 1000+ pre-built tool integrations and managed auth brokerage for AI agents.
- [crewAI Tools](https://docs.crewai.com/tools/database-data-tools/mongodbvectorsearchtool) ![GitHub Repo stars](https://img.shields.io/github/stars/crewAIInc/crewAI-tools?style=social) - CrewAI Tools is the official tool library for the CrewAI multi-agent harness.
- [FastAPI MCP](https://github.com/tadata-org/fastapi_mcp) ![GitHub Repo stars](https://img.shields.io/github/stars/tadata-org/fastapi_mcp?style=social) - Automatically exposes FastAPI routes as MCP (Model Context Protocol) tools, enabling any FastAPI-based service to be used as an agent tool with zero boilerplate.
- [FastMCP](https://gofastmcp.com) ![GitHub Repo stars](https://img.shields.io/github/stars/PrefectHQ/fastmcp?style=social) - Created by Jeremiah Lowin (Prefect founder), now maintained under PrefectHQ.
- [GenAI Toolbox](https://mcp-toolbox.dev/documentation/introduction/) ![GitHub Repo stars](https://img.shields.io/github/stars/googleapis/mcp-toolbox?style=social) - GenAI Toolbox is Google's official open-source MCP server for AI-database connectivity, providing a standardized way for AI agents to query and operate on enterprise databases.
- [GitHub MCP Server](https://github.com/github/github-mcp-server) ![GitHub Repo stars](https://img.shields.io/github/stars/github/github-mcp-server?style=social) - GitHub's official MCP Server with - enables LLM agents to interact with GitHub repositories, issues, PRs, code search, and actions via the Model Context Protocol.
- [Integuru](https://integuru.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/Integuru-AI/Integuru?style=social) - AI agent that builds permissionless integrations by reverse engineering platforms' internal APIs.
- [Kestra](https://kestra.io) ![GitHub Repo stars](https://img.shields.io/github/stars/kestra-io/kestra?style=social) - YAML-based workflow definitions with a rich UI.
- [mcp-agent](https://github.com/lastmile-ai/mcp-agent) ![GitHub Repo stars](https://img.shields.io/github/stars/lastmile-ai/mcp-agent?style=social) - Simple, composable framework for building agents using the Model Context Protocol (MCP).
- [MCP Context Forge](https://ibm.github.io/mcp-context-forge/) ![GitHub Repo stars](https://img.shields.io/github/stars/IBM/mcp-context-forge?style=social) - MCP Context Forge is an IBM-built AI gateway, registry, and proxy that sits in front of MCP, A2A, and REST/gRPC APIs.
- [MCP Framework](https://github.com/QuantGeekDev/mcp-framework) ![GitHub Repo stars](https://img.shields.io/github/stars/QuantGeekDev/mcp-framework?style=social) - Provides scaffolding, auto-discovery, and lifecycle management for building Model Context Protocol servers in TypeScript.
- [MCP-use](https://mcp-use.io) ![GitHub Repo stars](https://img.shields.io/github/stars/mcp-use/mcp-use?style=social) - MCP-use is a growing MCP framework providing a full-stack toolkit for building and connecting to MCP servers.
- [Mirage](https://www.strukto.ai/mirage) ![GitHub Repo stars](https://img.shields.io/github/stars/strukto-ai/mirage?style=social) - Python (mirage-ai) and TypeScript (@struktoai/mirage-) SDKs; FUSE-based mounts.
- [OpenSandbox](https://open-sandbox.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/opensandbox-group/OpenSandbox?style=social) - Secure, fast, and extensible sandbox runtime for AI agents built by Alibaba.
- [Smithery.ai](https://smithery.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/smithery-ai/cli?style=social) - MCP server registry and marketplace enabling discovery and installation of Model Context Protocol servers.
- [Spring AI Alibaba](https://java2ai.com) ![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/spring-ai-alibaba?style=social) - Production-ready agentic Java framework extending Spring AI with multi-agent orchestration, graph-based stateful workflows, HITL support, and a visual debugger.
- [Tilde](https://tilde.run) ![GitHub Repo stars](https://img.shields.io/github/stars/tilderun/tilde-python-sdk?style=social) - Transactional sandbox platform for safely running autonomous AI agents against production data.
- [Windmill](https://windmill.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/windmill-labs/windmill?style=social) - Open-source developer platform for building internal tools, automations, and data pipelines - a developer-first alternative to n8n and Zapier.

<a id="developer-computer-use-agent"></a>
## Developer / computer-use agent

Coding agent, browser/computer operator, IDE agent, CLI agent, or desktop task agent.

- [Aider](https://aider.chat) ![GitHub Repo stars](https://img.shields.io/github/stars/Aider-AI/aider?style=social) - AI pair programming tool for terminal-based code editing.
- [Browser Harness](https://browser-harness.com) ![GitHub Repo stars](https://img.shields.io/github/stars/browser-use/browser-harness?style=social) - Browser Harness helps agents operate developer tools, browsers, desktops, or local workflows.
- [browser-use](https://github.com/browser-use/browser-use) ![GitHub Repo stars](https://img.shields.io/github/stars/browser-use/browser-use?style=social) - High-adoption Python library enabling AI agents to control browsers via Playwright.
- [Chrome DevTools MCP](https://npmjs.org/package/chrome-devtools-mcp) ![GitHub Repo stars](https://img.shields.io/github/stars/ChromeDevTools/chrome-devtools-mcp?style=social) - Chrome DevTools MCP helps agents operate developer tools, browsers, desktops, or local workflows.
- [Cline](https://cline.bot) ![GitHub Repo stars](https://img.shields.io/github/stars/cline/cline?style=social) - Cline helps agents operate developer tools, browsers, desktops, or local workflows.
- [Continue](https://continue.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/continuedev/continue?style=social) - Open-source AI code assistant extension for VS Code and JetBrains with pluggable context providers and indexing backends.
- [Devika](https://github.com/stitionai/devika) ![GitHub Repo stars](https://img.shields.io/github/stars/stitionai/devika?style=social) - Open-source agentic AI software engineer that understands high-level human instructions, breaks them into steps, and executes code using web search and terminal tools.
- [Factory](https://factory.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/Factory-AI/factory?style=social) - Factory builds autonomous AI software engineering agents (Droids) that handle multi-step coding tasks across IDEs, CLI, GitHub Actions, Slack, and CI/CD pipelines.
- [FiftyOne](https://voxel51.com/fiftyone) ![GitHub Repo stars](https://img.shields.io/github/stars/voxel51/fiftyone?style=social) - FiftyOne is an ML dataset curation and model evaluation tool that stores rich sample metadata, embeddings, and evaluation results.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) ![GitHub Repo stars](https://img.shields.io/github/stars/google-gemini/gemini-cli?style=social) - Gemini CLI is Google's answer to Claude Code and Codex, providing an open-source AI agent in the terminal with MCP support and broad tool use.
- [Goose](https://github.com/aaif-goose/goose) ![GitHub Repo stars](https://img.shields.io/github/stars/aaif-goose/goose?style=social) - Goose is an extensible open-source AI coding agent from Block with plugin-based extensibility.
- [GPT Engineer](https://gptengineer.app) ![GitHub Repo stars](https://img.shields.io/github/stars/AntonOsika/gpt-engineer?style=social) - AI coding agent harness that generates full codebases from prompts.
- [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot) ![GitHub Repo stars](https://img.shields.io/github/stars/Pythagora-io/gpt-pilot?style=social) - AI developer agent that builds full applications step-by-step with human checkpoints.
- [gptme](https://gptme.org) ![GitHub Repo stars](https://img.shields.io/github/stars/gptme/gptme?style=social) - Terminal-based personal AI agent with local tool execution - code writing, terminal use, web browsing.
- [Kilo Code](https://kilocode.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/Kilo-Org/kilocode?style=social) - Kilo Code is an all-in-one agentic engineering platform - an opinionated coding agent harness that spans code generation, task orchestration, and agent execution.
- [mini-swe-agent](https://mini-swe-agent.com) ![GitHub Repo stars](https://img.shields.io/github/stars/SWE-agent/mini-swe-agent?style=social) - A radically simple (~100-line) coding agent sibling to SWE-agent, optimized for solving GitHub issues and command-line tasks with a minimal configuration surface.
- [Nanobrowser](https://nanobrowser.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/nanobrowser/nanobrowser?style=social) - Nanobrowser is an open-source Chrome extension for AI-powered browser automation.
- [open-swe](https://github.com/langchain-ai/open-swe) ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/open-swe?style=social) - Open-swe is an open-source asynchronous software engineering agent built on LangGraph.
- [OpenCode](https://opencode.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/opencode-ai/opencode?style=social) - OpenCode is a Charm-maintained coding agent (similar to Aider/Cline) that runs in the terminal, supports MCP tools, and uses Claude/GPT.
- [OpenHands](https://github.com/OpenHands/OpenHands) ![GitHub Repo stars](https://img.shields.io/github/stars/OpenHands/OpenHands?style=social) - Open-source software development agent platform formerly known as OpenDevin; ConversationStore has only FileConversationStore.
- [Plandex](https://plandex.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/plandex-ai/plandex?style=social) - Open-source AI coding agent designed for large, complex tasks.
- [Refact](https://refact.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/smallcloudai/refact?style=social) - Self-hosted AI coding agent with IDE plugin.
- [Serena](https://github.com/oraios/serena) ![GitHub Repo stars](https://img.shields.io/github/stars/oraios/serena?style=social) - MCP toolkit for coding agents with semantic code retrieval -, rapidly trending.
- [Stagehand](https://stagehand.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/browserbase/stagehand?style=social) - Stagehand helps agents operate developer tools, browsers, desktops, or local workflows.
- [Steel Browser](https://steel.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/steel-dev/steel-browser?style=social) - Steel Browser is an open-source Browser API for AI Agents & Apps - a batteries-included browser sandbox for automating the web.
- [SWE-agent](https://swe-agent.com) ![GitHub Repo stars](https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=social) - SWE-agent is the leading autonomous software engineering agent, widely used in research and production CI pipelines.
- [Tabby](https://tabbyml.com) ![GitHub Repo stars](https://img.shields.io/github/stars/TabbyML/tabby?style=social) - Self-hosted AI coding assistant and GitHub Copilot alternative.
- [Tavily](https://tavily.com) ![GitHub Repo stars](https://img.shields.io/github/stars/tavily-ai/tavily-python?style=social) - Tavily is a search-and-extract API purpose-built for AI agents, widely used as a web-search tool in LangChain and LangGraph pipelines.
- [trae-agent](https://www.trae.ai/) ![GitHub Repo stars](https://img.shields.io/github/stars/bytedance/trae-agent?style=social) - Trae-agent is a ByteDance-built LLM-based agent for general purpose software engineering tasks.
- [UFO](https://microsoft.github.io/UFO/) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/UFO?style=social) - UFO (UI-Focused Agent) is a Microsoft Research project that enables LLM agents to interact with Windows desktop applications via GUI automation.

<a id="data-ingestion-mlops-substrate"></a>
## Data / ingestion / MLOps substrate

ETL, workflow, feature, ML, or data pipeline substrate adjacent to AI apps.

- [Agentset](https://github.com/agentset-ai/agentset) ![GitHub Repo stars](https://img.shields.io/github/stars/agentset-ai/agentset?style=social) - Agentset is an open-source RAG platform with built-in citations, deep research, 22+ file formats, partitions, and an MCP server.
- [Airbyte](https://airbyte.com) ![GitHub Repo stars](https://img.shields.io/github/stars/airbytehq/airbyte?style=social) - Airbyte supports data ingestion, pipelines, or MLOps workflows adjacent to agent systems.
- [Apache Airflow](https://airflow.apache.org) ![GitHub Repo stars](https://img.shields.io/github/stars/apache/airflow?style=social) - Airflow is the dominant workflow orchestration platform widely used for AI/ML data pipelines.
- [Builder.io](https://www.builder.io) ![GitHub Repo stars](https://img.shields.io/github/stars/BuilderIO/builder?style=social) - Visual development platform for building AI-assisted web apps.
- [CocoIndex](https://cocoindex.io) ![GitHub Repo stars](https://img.shields.io/github/stars/cocoindex-io/cocoindex?style=social) - CocoIndex - incremental engine for long-horizon agents and data framework for AI.
- [Coral](https://withcoral.com) ![GitHub Repo stars](https://img.shields.io/github/stars/withcoral/coral?style=social) - Published benchmarks claim agents are ~20% more accurate and 2x more cost-efficient with Coral vs. direct provider MCPs across 82 real-world tasks.
- [Dagster](https://dagster.io) ![GitHub Repo stars](https://img.shields.io/github/stars/dagster-io/dagster?style=social) - Data orchestration platform for development, production, and observation of data assets.
- [dlt (data load tool)](https://dlthub.com) ![GitHub Repo stars](https://img.shields.io/github/stars/dlt-hub/dlt?style=social) - Dlt is a lightweight Python-native data loading library gaining traction as the dbt for ingestion in AI pipelines.
- [Feast](https://feast.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/feast-dev/feast?style=social) - Feast is the leading open-source feature store for ML/AI.
- [Firecrawl](https://firecrawl.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/firecrawl/firecrawl?style=social) - Firecrawl has grown to become one of the primary web data ingestion tools for AI pipelines, with a clean REST API and SDK that converts any website to clean, LLM-ready markdown.
- [Flyte](https://flyte.org) ![GitHub Repo stars](https://img.shields.io/github/stars/flyteorg/flyte?style=social) - Mature production-grade ML/AI workflow orchestration platform.
- [Leon](https://getleon.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/leon-ai/leon?style=social) - Leon is an open-source personal AI assistant built around tools, context, memory, and agentic execution.
- [MegaParse](https://megaparse.com) ![GitHub Repo stars](https://img.shields.io/github/stars/QuivrHQ/MegaParse?style=social) - MegaParse is a file parser optimised for LLM ingestion - it converts PDFs, DOCX, PPTX, and other document formats into clean, structured text with minimal information loss.
- [MindsDB](https://mindsdb.com) ![GitHub Repo stars](https://img.shields.io/github/stars/mindsdb/minds?style=social) - MindsDB is a high-visibility AI query engine that federates ML and AI reasoning across live data sources.
- [OmniParse](https://omniparse.cognitivelab.in/) ![GitHub Repo stars](https://img.shields.io/github/stars/adithya-s-k/omniparse?style=social) - OmniParse is a multimodal data ingestion and parsing platform that converts documents, images, audio, video, and web pages into structured, LLM-ready formats.
- [Pandas AI](https://pandas-ai.com) ![GitHub Repo stars](https://img.shields.io/github/stars/sinaptik-ai/pandas-ai?style=social) - Pandas AI enables conversational data analysis over SQL, CSV, and parquet sources via LLMs and RAG.
- [Pathway](https://pathway.com) ![GitHub Repo stars](https://img.shields.io/github/stars/pathwaycom/pathway?style=social) - Founded in Paris/France; backed with $14.5M raised.
- [Prefect](https://www.prefect.io) ![GitHub Repo stars](https://img.shields.io/github/stars/PrefectHQ/prefect?style=social) - Workflow orchestration framework for resilient data pipelines.
- [R2R](https://r2r-docs.sciphi.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/SciPhi-AI/R2R?style=social) - Production-ready RAG harness with multimodal ingestion, hybrid search, and knowledge graph support.
- [Unstructured](https://unstructured.io) ![GitHub Repo stars](https://img.shields.io/github/stars/Unstructured-IO/unstructured?style=social) - Unstructured is a widely-used document parsing and preprocessing library that feeds chunked, enriched content into RAG pipelines.
- [Zerox](https://github.com/getomni-ai/zerox) ![GitHub Repo stars](https://img.shields.io/github/stars/getomni-ai/zerox?style=social) - The integration is primarily as a Document Store target downstream of the parsing pipeline.

<a id="observability-evals"></a>
## Observability / evals

Tracing, evaluation, monitoring, audit, or runtime-ops tool.

- [Agenta](https://agenta.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/Agenta-AI/agenta?style=social) - Open-source LLMOps platform covering prompt playground, prompt management, LLM evaluation, and LLM observability.
- [AgentOps](https://agentops.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/AgentOps-AI/agentops?style=social) - Framework-agnostic observability and DevTool platform for AI agents.
- [Arize Phoenix](https://phoenix.arize.com) ![GitHub Repo stars](https://img.shields.io/github/stars/Arize-ai/phoenix?style=social) - Arize Phoenix - AI Observability & Evaluation.
- [AxonHub](https://axonhub.onrender.com/) ![GitHub Repo stars](https://img.shields.io/github/stars/looplj/axonhub?style=social) - AxonHub is an open-source AI gateway (Go) that routes any SDK (OpenAI, Anthropic, etc.) to 100+ LLMs transparently.
- [fast-agent](https://github.com/evalstate/fast-agent) ![GitHub Repo stars](https://img.shields.io/github/stars/evalstate/fast-agent?style=social) - Python agent framework emphasizing strong MCP (Model Context Protocol) and ACP (Agent Communication Protocol) support.
- [Guardrails](https://www.guardrailsai.com/docs) ![GitHub Repo stars](https://img.shields.io/github/stars/guardrails-ai/guardrails?style=social) - Guardrails provides tracing, evaluation, monitoring, or operational insight for agent systems.
- [Helicone](https://www.helicone.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/Helicone/helicone?style=social) - Open-source LLM observability platform (YC W23) providing monitoring, evaluation, and experimentation with a one-line integration.
- [HumanLayer](https://humanlayer.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/humanlayer/humanlayer?style=social) - SDK for human-in-the-loop AI agent workflows.
- [Langfuse](https://langfuse.com) ![GitHub Repo stars](https://img.shields.io/github/stars/langfuse/langfuse?style=social) - Open source LLM engineering platform providing observability, metrics, evals, prompt management, playground, and datasets.
- [LangSmith](https://smith.langchain.com) ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langsmith-sdk?style=social) - LangSmith provides tracing, evaluation, monitoring, or operational insight for agent systems.
- [Langtrace](https://langtrace.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/Scale3-Labs/langtrace?style=social) - Langtrace is an open-source, OpenTelemetry-based end-to-end observability tool for LLM applications.
- [LangWatch](https://langwatch.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/langwatch/langwatch?style=social) - LLM monitoring and analytics platform with tracing, evaluation, and optimization features.
- [Monocle](https://monocle2ai.org) ![GitHub Repo stars](https://img.shields.io/github/stars/monocle2ai/monocle?style=social) - Monocle is an open-source (Apache 2.0) library for tracing and testing GenAI apps and agents, governed as a Linux Foundation AI & Data project (LF sandbox).
- [OpenLLMetry](https://github.com/traceloop/openllmetry) ![GitHub Repo stars](https://img.shields.io/github/stars/traceloop/openllmetry?style=social) - OpenLLMetry provides OpenTelemetry-compatible instrumentation for LLM applications.
- [Opik](https://github.com/comet-ml/opik) ![GitHub Repo stars](https://img.shields.io/github/stars/comet-ml/opik?style=social) - Open-source LLM observability and evaluation platform by Comet ML.
- [Oumi](https://oumi.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/oumi-ai/oumi?style=social) - End-to-end platform for building, training, fine-tuning, and deploying AI models.
- [Promptfoo](https://promptfoo.dev) ![GitHub Repo stars](https://img.shields.io/github/stars/promptfoo/promptfoo?style=social) - LLM testing and evaluation framework for red-teaming, regression testing, and prompt comparison.
- [RagaAI Catalyst](https://raga.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/raga-ai-hub/ragaai-catalyst?style=social) - Open-source LLM evaluation and observability platform.
- [Superagent](https://superagent.sh) ![GitHub Repo stars](https://img.shields.io/github/stars/superagent-ai/superagent?style=social) - Superagent - open-source SDK for AI agent safety.
- [TruLens](https://www.trulens.org) ![GitHub Repo stars](https://img.shields.io/github/stars/truera/trulens?style=social) - TruLens provides tracing, evaluation, monitoring, or operational insight for agent systems.

<a id="model-serving-gateway"></a>
## Model serving / gateway

Inference runtime, model gateway, model router, local model shell, or LLM API proxy.

- [Bifrost](https://github.com/maximhq/bifrost) ![GitHub Repo stars](https://img.shields.io/github/stars/maximhq/bifrost?style=social) - Enterprise AI gateway written in Go.
- [exo](https://github.com/exo-explore/exo) ![GitHub Repo stars](https://img.shields.io/github/stars/exo-explore/exo?style=social) - exo provides model serving, routing, gateway, or inference infrastructure.
- [GPT4All](https://gpt4all.io) ![GitHub Repo stars](https://img.shields.io/github/stars/nomic-ai/gpt4all?style=social) - Open-source local LLM ecosystem by Nomic AI.
- [Jan](https://jan.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/janhq/jan?style=social) - Jan provides model serving, routing, gateway, or inference infrastructure.
- [LazyLLM](https://lazyllm.readthedocs.io) ![GitHub Repo stars](https://img.shields.io/github/stars/LazyAGI/LazyLLM?style=social) - Chinese multi-agent framework with RAG pipeline support, easy tool integration, and model fine-tuning capabilities.
- [LiteLLM](https://litellm.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/BerriAI/litellm?style=social) - Universal LLM API gateway/proxy supporting 100+ providers.
- [LLMStack](https://llmstack.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/trypromptly/LLMStack?style=social) - LLMStack provides a self-hosted platform for building AI assistants, agents, and automations without code.
- [LLMWare](https://llmware.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/llmware-ai/llmware?style=social) - Enterprise RAG framework with purpose-built small language models (SLMs), document parsing, integrated vector stores, and multi-step agent pipelines.
- [LocalAI](https://localai.io) ![GitHub Repo stars](https://img.shields.io/github/stars/mudler/LocalAI?style=social) - LocalAI provides model serving, routing, gateway, or inference infrastructure.
- [Manifest](https://github.com/mnfst/manifest) ![GitHub Repo stars](https://img.shields.io/github/stars/mnfst/manifest?style=social) - Sits at the control/routing layer, selecting between LLM providers based on cost/latency/quality policy.
- [MCP Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) ![GitHub Repo stars](https://img.shields.io/github/stars/modelcontextprotocol/rust-sdk?style=social) - MCP Rust SDK - the official Rust SDK for the Model Context Protocol, maintained in the modelcontextprotocol org alongside the TypeScript, Python, and other language SDKs.
- [New API](https://github.com/QuantumNous/new-api) ![GitHub Repo stars](https://img.shields.io/github/stars/QuantumNous/new-api?style=social) - Unified LLM API hub supporting cross-conversion between OpenAI, Claude, Gemini, and other LLM API formats with token management, routing, and load balancing.
- [Nexent](https://nexent.tech) ![GitHub Repo stars](https://img.shields.io/github/stars/ModelEngine-Group/nexent?style=social) - Nexent provides model serving, routing, gateway, or inference infrastructure.
- [Ollama](https://ollama.com) ![GitHub Repo stars](https://img.shields.io/github/stars/ollama/ollama?style=social) - Ollama exposes an OpenAI-compatible REST API and supports 100+ models.
- [OpenLLM](https://bentoml.com) ![GitHub Repo stars](https://img.shields.io/github/stars/bentoml/OpenLLM?style=social) - Open-source LLM serving framework by BentoML.
- [Portkey AI Gateway](https://portkey.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/Portkey-AI/gateway?style=social) - Open-source AI gateway supporting 250+ LLMs with caching, routing, and observability.
- [RubyLLM](https://rubyllm.com) ![GitHub Repo stars](https://img.shields.io/github/stars/crmne/ruby_llm?style=social) - Ruby LLM provider abstraction layer - one unified API for OpenAI, Anthropic, Gemini, Bedrock, DeepSeek, Mistral, Ollama, and 10+ other providers.
- [Semantic Router](https://github.com/aurelio-labs/semantic-router) ![GitHub Repo stars](https://img.shields.io/github/stars/aurelio-labs/semantic-router?style=social) - Semantic Router performs fast semantic intent classification using vector similarity over a route index and supports pluggable index backends.
- [SGLang](https://sglang.io) ![GitHub Repo stars](https://img.shields.io/github/stars/sgl-project/sglang?style=social) - SGLang is a high-performance serving framework for large language models and multimodal models - similar surface to vLLM (inference serving / structured output).
- [vLLM](https://docs.vllm.ai) ![GitHub Repo stars](https://img.shields.io/github/stars/vllm-project/vllm?style=social) - High-throughput and memory-efficient LLM inference engine from UC Berkeley.

<a id="database-infrastructure-product"></a>
## Database / infrastructure product

Data substrate, vector/graph/memory DB, deployment platform, or infrastructure product.

- [HydraDB](https://hydradb.com) ![GitHub Repo stars](https://img.shields.io/github/stars/usecortex/hydradb-mcp?style=social) - HydraDB provides data or infrastructure primitives for agent systems.

<a id="protocol-standard-only"></a>
## Protocol / standard only

Specification with no direct implementation-owned storage surface.

- [Agent Client Protocol (ACP)](https://agentclientprotocol.com) ![GitHub Repo stars](https://img.shields.io/github/stars/agentclientprotocol/agent-client-protocol?style=social) - Sits alongside MCP in the emerging protocol layer of the agentic stack - MCP connects agents to tools; ACP connects editor UIs to agents.

## Related Awesome Lists

- [Awesome AI Infrastructure](https://github.com/brandonhimpfen/awesome-ai-infrastructure) - Curated resources for AI infrastructure, platforms, and operational tooling.
- [Awesome Lists](https://github.com/brandonhimpfen/awesome-lists) - A collection of curated awesome lists.

## Contribute

Contributions are welcome. Please follow [`CONTRIBUTING.md`](CONTRIBUTING.md), including the required entry format, stars badge, category placement, and alphabetical sorting.

## License

[Creative Commons Attribution-ShareAlike 4.0 International](LICENSE).

## Maintenance

Generated from 418 private research records; 386 GitHub-backed entries are currently listed.
