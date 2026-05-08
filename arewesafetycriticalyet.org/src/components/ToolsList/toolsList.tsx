import React from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import Link from "@docusaurus/Link";
import styles from "./styles.module.css";
import raw_tools_list from "./available-tools.json";

type ToolType =
  | "package-manager"
  | "compiler"
  | "testing"
  | "formal-verification"
  | "profiling"
  | "debugging"
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

type ToolCategory = {
  title: string,
  description: string,
}

const TOOL_TYPE_LABEL: Record<ToolType, ToolCategory> = {
  "package-manager": { title: "Package Managers", description: "Tools for automating the management of a project's dependencies, its compilation and linking." },
  compiler: { title: "Compilers", description: "Tools for transforming source code into either executable binaries or dynamic libraries." },
  testing: { title: "Testing", description: "Tools for evaluating the correctness of a program under a finite set of scenarios through its execution." },
  "formal-verification": { title: "Formal Verification", description: "Tools for obtaining mathematical assurance of the behavior of the program. Such as, for example, its required level of functional safety." },
  profiling: { title: "Profiling", description: "Tools for measurement of program performance along different types of resources." },
  debugging: { title: "Debugging", description: "Tools for interactively inspecting the dynamic behavior of a program." },
  "requirements-traceability": { title: "Requirements Traceability", description: "Tools to manage traces between requirements and related source and/or object code." },
  "static-analysis": { title: "Static Analysis", description: "Tools for analyzing source code without executing it." },
  "code-coverage": { title: "Code Coverage", description: "Tools for calculating the quality of a test suite, under the metric of code coverage." },
  other: { title: "Other", description: "Tools that fall under none of the other categories." },
};

const TOOL_TYPE_ORDER: ToolType[] = [
  "package-manager",
  "compiler",
  "static-analysis",
  "formal-verification",
  "testing",
  "code-coverage",
  "debugging",
  "profiling",
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

function renderDetailsRow(tool: ToolEntry) {
  const hasLiability = Boolean(tool.liability);
  const qualified = tool.qualified ?? [];
  const hasQualifiedInfo = qualified.some((q) => Boolean(q.info));

  if (!hasLiability && !hasQualifiedInfo) return null;

  return (
    <div className={styles.detailsRow}>
      <details>
        <summary>Details</summary>
        {hasLiability && (
          <div>
            <strong>Liability:</strong>{" "}
            <ReactMarkdown remarkPlugins={[remarkGfm]}>
              {tool.liability ?? ""}
            </ReactMarkdown>
          </div>
        )}
        {hasQualifiedInfo && (
          <div className={hasLiability ? styles.spacedSection : undefined}>
            <strong>Qualification Info:</strong>
            <ul>
              {qualified
                .filter((q) => q.info)
                .map((q) => (
                  <li
                    key={`${q.name}:${q["up-to"]}:info`}
                    className={styles.infoBlock}
                  >
                    <div>
                      <strong>{q.name}</strong> (up to {q["up-to"]})
                    </div>
                    <div className={styles.infoText}>
                      <ReactMarkdown remarkPlugins={[remarkGfm]}>
                        {q.info ?? ""}
                      </ReactMarkdown>
                    </div>
                  </li>
                ))}
            </ul>
          </div>
        )}
      </details>
    </div>
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

      <h3>Tool Categories</h3>
      <ul>
        {TOOL_TYPE_ORDER.filter(
          (type) => (grouped_tools.get(type) ?? []).length > 0,
        ).map((type) => {
          const anchor = "#" + TOOL_TYPE_LABEL[type].title
          return (
            <li><a href={anchor} >{TOOL_TYPE_LABEL[type].title}</a></li>
          )
        })}
      </ul>

      <h3>Tracked standards</h3>
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
              <td style={{ whiteSpace: "nowrap" }}>{s.name}</td>
              <td>
                {s.levels.map((level, index) => (
                  <>
                    <span key={index} style={{ whiteSpace: "nowrap" }}>{level}</span>
                    <br />
                  </>
                ))}
              </td >
              <td>{s.description}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {TOOL_TYPE_ORDER.filter(
        (type) => (grouped_tools.get(type) ?? []).length > 0,
      ).map((type) => {
        const toolsOfType = grouped_tools.get(type) ?? [];

        return (
          <section id={TOOL_TYPE_LABEL[type].title} key={type}>
            <h2 className={styles.typeHeading}>{TOOL_TYPE_LABEL[type].title}</h2>

            <p>{TOOL_TYPE_LABEL[type].description}</p>

            <div className={styles.gridContainer}>
              <div className={styles.gridHeaderRow}>
                <div className={styles.gridHeader}>Tool</div>
                <div className={styles.gridHeader}>Description</div>
                <div className={styles.gridHeader}>License</div>
                <div className={styles.gridHeader}>Qualification</div>
              </div>

              {toolsOfType.map((tool) => {
                const qualified = tool.qualified ?? [];
                return (
                  <React.Fragment key={tool.name}>
                    <div className={styles.toolRow}>
                      <div className={styles.toolRowContent}>
                        <div className={styles.gridCell}>
                          <div className={styles.toolName}>
                            <Link to={tool.url}>{tool.name}</Link>
                            {tool.vendor && (
                              <div className={styles.secondaryLine}>
                                Vendor: {tool.vendor}
                              </div>
                            )}
                          </div>
                        </div>

                        <div className={styles.gridCell}>
                          <ReactMarkdown remarkPlugins={[remarkGfm]}>
                            {tool.description}
                          </ReactMarkdown>
                        </div>

                        <div className={styles.gridCell}>
                          <span className="badge badge--primary">
                            {tool.license}
                          </span>
                        </div>

                        <div className={styles.gridCell}>
                          {qualified.length > 0 ? (
                            renderQualifiedBadges(qualified)
                          ) : (
                            <span>—</span>
                          )}
                        </div>
                      </div>
                      {renderDetailsRow(tool)}
                    </div>
                  </React.Fragment>
                );
              })}
            </div>
          </section>
        );
      })}
    </div>
  );
}
