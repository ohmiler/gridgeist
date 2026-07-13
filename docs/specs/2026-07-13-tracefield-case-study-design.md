# Tracefield Case Study Design

## Purpose

Build Tracefield as a standalone developer-observability dashboard and use it as Gridgeist's first flagship case study. The experiment must show whether the skill can turn operational data into a distinctive, responsive product interface rather than a generic dashboard-card composition.

## Product

Tracefield serves backend engineers and SRE teams investigating API latency and failures. Users can scan system health, filter request traces, search by trace ID or endpoint, open a trace, and inspect the duration of each span.

## Visual direction

The visual thesis is “a live incident record.” The interface uses a dark technical surface, precise typography, visible structural lines, and acid green only for important state and focus. Product evidence—trace IDs, endpoints, durations, status, and waterfall spans—carries the visual identity. The application opens directly into the working surface and does not use a marketing hero.

## Information architecture

- Sidebar: Overview, Live Traces, Services, and Alerts.
- Top bar: environment, time range, and trace search.
- Health strip: request volume, error rate, P95 latency, and active incidents.
- Trace table: endpoint, service, HTTP status, duration, and timestamp.
- Trace inspector: selected request metadata and a span waterfall for gateway, authentication, database, and external services.

## Interaction and state

- Filter traces by service and status.
- Search by trace ID or endpoint.
- Open a table row to inspect its trace.
- Support keyboard navigation, visible focus, and reduced motion.
- Include populated, loading, empty, and error states using deterministic local mock data.
- On mobile, replace the persistent multi-column inspector with a focused list and dismissible detail drawer.

## Technical approach

- Create a standalone public repository at `ohmiler/tracefield`.
- Use Next.js and TypeScript with a static-export configuration compatible with GitHub Pages.
- Keep data local and deterministic; the case study does not require a backend or authentication.
- Use a restrained styling system and avoid adding a component library unless implementation evidence justifies it.
- Use Playwright for representative desktop and mobile interaction checks.

## Experiment record

The case study records three artifacts:

1. A generic dashboard baseline using the same product requirements and data.
2. The Gridgeist prompt and the design decisions produced from it.
3. The final interface, scored against hierarchy, product specificity, originality, responsive composition, accessibility, and implementation quality.

The final result will be referenced from Gridgeist only after the standalone project builds, deploys, and passes its verification checks.

## Success criteria

- A user can locate a failing or slow trace and understand its bottleneck without instruction.
- Operational evidence dominates the interface; generic cards and decorative dashboard chrome do not.
- Core workflows work at desktop and mobile sizes without horizontal overflow.
- Keyboard focus and reduced-motion behavior are usable.
- Static export succeeds and GitHub Pages serves the project correctly.
- The repository contains enough experiment evidence for another person to understand what Gridgeist changed.
