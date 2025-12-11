# Tools List Maintenance Flows

This section defines how the tools list is managed by the tooling subcommittee.

## TLDR

The tool proposal consists of three main phases:

### 1. **Assigning Phase**

- Anyone can create issues to request changes related to the tools list (add, change, delete)
- Tooling Committee manages the process
- Tools Taskforce presents unassigned issues marked with a `submit tooling` or `tooling` label
- Issues are assigned to volunteers or taken over by the Taskforce

### 2. **Review New Issues**

- **New/Change Path**: 15-day review period including:
  - Tool information checking
  - Entry creation in [available-tools.yaml]
  - Optional: vendor contact, testing, and user feedback collection
- **Delete Path**: Review deletion reasoning
- **Common validation**: Valid requests proceed to PR creation and merge process
- **PR Process**: Includes remark resolution cycle if needed

### 3. **Review Complete List (Annually)**

- Task Force Member initiates annual review of tools listed in available.tools.yaml
- Tools to review distributed evenly among assessors
- Evaluation based on:
  - Tool maintenance status
  - License updates
  - Vendor status
- Changes feed back into the PR creation process

## Assigning New Issues Related to the Tools List

This flowchart defines how new tools list related issues are assigned to subcommittee members:

```mermaid
flowchart TD
    %% Assigning Phase
    A1[Anyone] --> A2["Creates new issue for a tool related change<br/>(new, change, delete)"]
    A2 --> A3[Tooling Subcommittee]
    A3 --> A4[Tools Taskforce/Author present<br/>overview of unassigned issues with <em>submit tooling</em> or <em>tooling</em> label]
    A4 --> A5[Issue is assigned for review<br/>to Tools Committee Volunteer]
    A5 --> A6[In case of no volunteer<br/>Taskforce takes over the review]

    %% Styling
    classDef actor fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:2px

    class A1,A3 actor
    class A2,A4,A5,A6 process
```

## Review New Issues

This flowchart defines how issues are reviewed by assignees:

```mermaid
flowchart TD
    %% Review New Issues Phase
    B0[Assigned Issue] --> B1[Up to 15 days]
    B1 --> B2{Issue Type}
    B2 --> |New/Change| B4[Check Tools information]
    B2 --> |Delete| B3[Check reason for deletion]
    
    %% New/Change Path
    B4 --> B5{Valid change/<br/>new tool for<br/>safety-critical<br/>Rust projects}
    B5 --> |No| B6[Close Issue with justification]
    B5 --> |Yes| B7[Fill up new entry in<br/>available.tools.yaml]
    B7 --> B8[<strong>Optional:</strong><br/><ul><li>Contact vendor</li><li>Test/Present tool</li><li>Collect user feedback</li></ul>]
    
    %% Delete Path
    B3 --> B12{Valid?}
    B12 --> |No| B6
    B12 --> |Yes| B13[Delete entry from<br/>available-tools.yaml]

    %% PR
    B8 --> B14[See section:<br/>Changes to the Tools List]
    B13 --> B14

    %% Styling
    classDef actor fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef optional fill:#f5f5f5,stroke:#666666,stroke-width:2px
    classDef time fill:#f5e3e3,stroke:#666666,stroke-width:1px
    
    class B0 actor
    class B8 optional
    class B2,B5,B12 decision
    class B3,B4,B6,B7,B13 process
    class B1 time
```

## "Once a Year" Review

This flowchart defines how the "Once a Year" review of the tools list is handled:

```mermaid
flowchart TD
    %% Review Complete List Phase - Once a year
    C1[Task Force Member] --> C2[Create an issue with a check list<br/>of the tools to review.<br/>Distribute the tools evenly<br/>among task force members]
    C2 --> C3[Each assignee evaluates<br/>their assigned tools]
    C3 --> C4[<strong>Evaluation Criteria:</strong><ul><li>Tool maintenance status</li><li>License update</li><li>Vendor status</li></ul>]
    C4 --> C5{Changes?}
    C5 --> |Yes| C7[See section:<br/>Changes to the Tools List]
    C5 --> |No| C6[Mark tool as reviewed<br/>in corresponding issue]
    C7 --> |Merged| C6

    %% Styling
    classDef actor fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:2px
    
    class C1 actor
    class C5 decision
    class C2,C3,C4,C6 process
```


## Changes to the Tools List

This flowchart defines how changes to the tools list are handled:

```mermaid
flowchart TD
    %% Common Decision Point
    B1[Create PR] --> B2[In up to 15 days]
    B2 --> B3{Open Remarks?}
    B3 --> |Yes| B4[Resolve Remarks]
    B4 --> B5((Return))
    B5 --> B2
    B3 --> |No| B6[Taskfore Member<br/>merges PR]

    %% Styling
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef time fill:#f5e3e3,stroke:#666666,stroke-width:1px
    
    class B3 decision
    class B1,B4,B6 process
    class B2 time
```
