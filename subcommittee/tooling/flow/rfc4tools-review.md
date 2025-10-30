```mermaid
flowchart TD
    %% Assigning Phase
    A1[Anyone] --> A2[Creates new issue for a tool related change<br/>new, change, delete]
    A2 --> A3[Tooling Committee]
    A3 --> A4[Tools Taskforce/Author present<br/>overview of unassigned issues with `submit tooling` or `tooling` label]
    A4 --> A5[Issue is assigned for review<br/>to Tools Committee Volunteer]
    A5 --> A6[In case of no volunteer<br/>Taskforce takes over the review]

    %% Review New Issues Phase
    B1{Issue Type} --> |New/Change| B2[Up to 15 days]
    B1 --> |Delete| B3[Up to 15 days]
    
    %% New/Change Path
    B2 --> B4[Check Tools information]
    B4 --> B5[Fill up new entry in<br/>available.tools.yaml]
    B5 --> B6[Optional:<br/>Contact vendor]
    B6 --> B7[Optional:<br/>Test/Present tool]
    B7 --> B8[Optional:<br/>Collect user feedback]
    B8 --> B19{Valid change or<br/>new tool for<br/>safety-critical<br/>Rust projects}
    B19 --> |No| B11[Close Issue with justification]
    B19 --> |Yes| B13
    
    %% Delete Path
    B3 --> B10[Check reason for deletion]
    B10 --> B9{Valid?}
    B9 --> |No| B11
    B9 --> |Yes| B12[Delete entry from<br/>available.tools.yaml]
    
    %% Common Decision Point
    B8 --> B13[Create PR]
    B12 --> B13
    B13 --> B14[In up to 15 days]
    B14 --> B15{Open Remarks?}
    B15 --> |Yes| B16[Resolve Remarks]
    B16 --> B17((Return))
    B17 --> B14
    B15 --> |No| B18[Taskfore Member<br/>Merge PR]

    %% Review Complete List Phase - Once a year
    C1[Task Force Member] --> C2[Create an issue with a check list<br/>of the tools to review.<br/>Distribute the tools evenly<br/>among assessors]
    C2 --> C3[Each assignee evaluates<br/>their assigned tools]
    C3 --> C4[Evaluation Criteria:<br/>- Tool maintenance status<br/>- License update<br/>- Vendor status]
    C4 --> C5{Changes?}
    C5 --> |Yes| B13
    C5 --> |No| C6[Mark tool as reviewed<br/>in corresponding issue]

    %% Styling
    classDef actor fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef process fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef optional fill:#f5f5f5,stroke:#666666,stroke-width:2px
    
    class A1,A3,C1 actor
    class B6,B7,B8 optional
    class B1,B9,B15,C5 decision
    class A2,A4,A5,A6,B2,B3,B4,B5,B10,B11,B12,B13,B14,B16,B18,B19,C2,C3,C4,C6 process

    %% Section Labels
    subgraph "Assigning Phase"
        A1
        A2
        A3
        A4
        A5
        A6
    end
    
    subgraph "Review New Issues"
        B1
        B2
        B3
        B4
        B5
        B6
        B7
        B8
        B9
        B10
        B11
        B12
        B13
        B14
        B15
        B16
        B17
        B18
        B19
    end
    
    subgraph "Review Complete List (Once a year)"
        C1
        C2
        C3
        C4
        C5
        C6
    end
```

## RFC4Tools Review Process

This Mermaid diagram represents the RFC4Tools review workflow with three main phases:

### 1. **Assigning Phase**
- Anyone can create issues for tool changes (new, change, delete)
- Tooling Committee manages the process
- Tools Taskforce presents unassigned issues marked with a `submit tooling` or `tooling` label
- Issues are assigned to volunteers or taken over by the Taskforce

### 2. **Review New Issues**
- **New/Change Path**: 15-day review period including:
  - Tool information checking
  - Entry creation in available.tools.yaml
  - Optional: vendor contact, testing, and user feedback collection
- **Delete Path**: Review deletion reasoning
- **Common validation**: Valid requests proceed to PR creation and merge process
- **PR Process**: Includes remark resolution cycle if needed

### 3. **Review Complete List (Annual)**
- Task Force Member initiates annual review
- Tools to review distributed evenly among assessors
- Evaluation based on:
  - Tool maintenance status
  - License updates
  - Vendor status
- Changes feed back into the PR creation process
