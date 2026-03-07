import React from "react";
import Link from "@docusaurus/Link";
import styles from "./styles.module.css";
import raw_tools_list from "./available-tools.json";

type ToolType =
  | "package-manager"
  | "compiler"
  | "test-runner"
  | "formal-verification"
  | "profiler"
  | "debugger"
  | "requirements-traceability"
  | "static-analysis"
  | "code-coverage"
  | "other";

type StandardInfo = {
  name: string;
  levels: string[];
  description: string;
};

type QualifiedInfo = {
  name: string;
  "up-to": string;
  info?: string | null;
};

type ToolEntry = {
  name: string;
  type: ToolType;
  url: string;
  description: string;
  license: string;
  vendor?: string | null;
  liability?: string | null;
  qualified?: QualifiedInfo[] | null;
};

type ToolsList = {
  metadata: {
    title: string;
    version: string;
    date: string;
    "tracked-standards": StandardInfo[];
  };
  tools: ToolEntry[];
};

const TOOL_TYPE_LABEL: Record<ToolType, string> = {
  "package-manager": "Package Managers",
  compiler: "Compilers",
  "test-runner": "Test Runners",
  "formal-verification": "Formal Verification",
  profiler: "Profilers",
  debugger: "Debuggers",
  "requirements-traceability": "Requirements Traceability",
  "static-analysis": "Static Analysis",
  "code-coverage": "Code Coverage",
  other: "Other",
};

const TOOL_TYPE_ORDER: ToolType[] = [
  "package-manager",
  "compiler",
  "static-analysis",
  "formal-verification",
  "test-runner",
  "code-coverage",
  "debugger",
  "profiler",
  "requirements-traceability",
  "other",
];

function groupToolsByType(tools: ToolEntry[]): Map<ToolType, ToolEntry[]> {
  const grouped = new Map<ToolType, ToolEntry[]>();

  for (const tool of tools) {
    const existing = grouped.get(tool.type) ?? [];
    existing.push(tool);
    grouped.set(tool.type, existing);
  }

  for (const [_type, toolsOfType] of grouped) {
    toolsOfType.sort((a, b) => a.name.localeCompare(b.name));
  }

  return grouped;
}

function renderQualifiedBadges(qualified: QualifiedInfo[]) {
  return (
    <div className={styles.badges}>
      {qualified.map((q) => (
        <span
          key={`${q.name}:${q["up-to"]}`}
          className="badge badge--secondary"
        >
          {q.name} (up to {q["up-to"]})
        </span>
      ))}
    </div>
  );
}

function renderExtraDetails(tool: ToolEntry) {
  const hasLiability = Boolean(tool.liability);
  const qualified = tool.qualified ?? [];
  const hasQualifiedInfo = qualified.some((q) => Boolean(q.info));

  if (!hasLiability && !hasQualifiedInfo) {
    return null;
  }

  return (
    <details className={styles.details}>
      <summary>Details</summary>
      {hasLiability && (
        <div>
          <strong>Liability / notes:</strong>
          <div>{tool.liability}</div>
        </div>
      )}
      {hasQualifiedInfo && (
        <div className={hasLiability ? styles.spacedSection : undefined}>
          <strong>Qualification info:</strong>
          {qualified
            .filter((q) => q.info)
            .map((q) => (
              <div
                key={`${q.name}:${q["up-to"]}:info`}
                className={styles.infoBlock}
              >
                <div>
                  <strong>{q.name}</strong> (up to {q["up-to"]})
                </div>
                <div className={styles.infoText}>{q.info}</div>
              </div>
            ))}
        </div>
      )}
    </details>
  );
}

export default function ToolsList(): React.ReactElement {
  const tools_list = raw_tools_list as ToolsList;
  const grouped_tools = groupToolsByType(tools_list.tools);

  return (
    <div>
      <h2 className={styles.metaTitle}>{tools_list.metadata.title}</h2>
      <p className={styles.metaSubtitle}>
        Version {tools_list.metadata.version} · Last checked{" "}
        {tools_list.metadata.date}
      </p>

      <div className="row">
        <div className="col col--7">
          <div className="card">
            <div className="card__header">
              <strong>Tracked standards</strong>
            </div>
            <div className="card__body">
              <table className="table table--striped table--compact">
                <thead>
                  <tr>
                    <th>Standard</th>
                    <th>Levels</th>
                    <th>Description</th>
                  </tr>
                </thead>
                <tbody>
                  {tools_list.metadata["tracked-standards"].map((s) => (
                    <tr key={s.name}>
                      <td style={{ "white-space": "nowrap" }}>{s.name}</td>
                      <td>{s.levels.join(", ")}</td>
                      <td>{s.description}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      {TOOL_TYPE_ORDER.filter(
        (type) => (grouped_tools.get(type) ?? []).length > 0,
      ).map((type) => {
        const toolsOfType = grouped_tools.get(type) ?? [];

        return (
          <section key={type}>
            <h2 className={styles.typeHeading}>{TOOL_TYPE_LABEL[type]}</h2>
            <table className="table table--striped table--compact">
              <thead>
                <tr>
                  <th style={{ width: "22%" }}>Tool</th>
                  <th>Description</th>
                  <th style={{ width: "12%" }}>License</th>
                  <th style={{ width: "26%" }}>Qualification / notes</th>
                </tr>
              </thead>
              <tbody>
                {toolsOfType.map((tool) => {
                  const qualified = tool.qualified ?? [];
                  return (
                    <tr key={tool.name}>
                      <td>
                        <div className={styles.toolName}>
                          <Link to={tool.url}>{tool.name}</Link>
                          {tool.vendor && (
                            <div className={styles.secondaryLine}>
                              Vendor: {tool.vendor}
                            </div>
                          )}
                        </div>
                      </td>
                      <td>{tool.description}</td>
                      <td>
                        <span className="badge badge--primary">
                          {tool.license}
                        </span>
                      </td>
                      <td>
                        {qualified.length > 0 ? (
                          renderQualifiedBadges(qualified)
                        ) : (
                          <span>—</span>
                        )}
                        {renderExtraDetails(tool)}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </section>
        );
      })}
    </div>
  );
}
