/// This struct represents the base for the tool list YAML file schema.
#[derive(
    Debug, Clone, PartialEq, Eq, serde::Serialize, serde::Deserialize, schemars::JsonSchema,
)]
#[serde(rename_all = "kebab-case")]
pub struct ToolsList {
    /// Contains general metadata related to the tool list.
    pub metadata: ToolsListMetadata,
    /// The actual tool list.
    pub tools: Vec<ToolEntry>,
    /// List of open topics where tools are missing or are lacking support and stability.
    pub open_topics: Vec<OpenToolTopic>,
}

#[derive(
    Debug, Clone, PartialEq, Eq, serde::Serialize, serde::Deserialize, schemars::JsonSchema,
)]
#[serde(rename_all = "kebab-case")]
pub struct ToolsListMetadata {
    /// The title of the tool list.
    pub title: String,
    /// The version of the tool list.
    pub version: String,
    /// The date the tool list was last checked.
    ///
    /// **Note:** This is used to show that the list has been reviewed even if no changes to the list were made.
    pub date: String,
    /// A list of safety-critical standards that are considered for the listed tools.
    pub tracked_standards: Vec<StandardInfo>,
}

/// Represents a safety-critical standard.
#[derive(
    Debug, Clone, PartialEq, Eq, serde::Serialize, serde::Deserialize, schemars::JsonSchema,
)]
pub struct StandardInfo {
    /// The name of the safety-critical standard.
    /// e.g. ISO-26262
    pub name: String,
    /// The safety levels of the standard.
    /// e.g. ASIL-B
    pub levels: Vec<String>,
    /// The short description of the standard.
    pub description: String,
}

/// The representation of a tool entry in the list.
#[derive(
    Debug, Clone, PartialEq, Eq, serde::Serialize, serde::Deserialize, schemars::JsonSchema,
)]
pub struct ToolEntry {
    /// The tool name.
    pub name: String,
    /// The type of tool.
    /// e.g. debugger, compiler, ...
    #[serde(rename = "type")]
    pub r#type: ToolType,
    /// URL to the tool homepage.
    pub url: String,
    /// Short description of the tool.
    pub description: String,
    /// The license of the tool.
    pub license: String,
    /// Optional name of the tool vendor.
    pub vendor: Option<String>,
    /// Optional liability statement for the tool.
    pub liability: Option<String>,
}

/// Represents the possible types tools are grouped by in the list.
#[derive(
    Debug, Clone, PartialEq, Eq, serde::Serialize, serde::Deserialize, schemars::JsonSchema,
)]
#[serde(rename_all = "kebab-case")]
pub enum ToolType {
    PackageManager,
    Compiler,
    TestRunner,
    FormalVerification,
    Profiler,
    Debugger,
    RequirementsTraceability,
    StaticAnalysis,
    CodeCoverage,
    Other,
}

/// Represents an open topic that is lacking tooling support.
#[derive(
    Debug, Clone, PartialEq, Eq, serde::Serialize, serde::Deserialize, schemars::JsonSchema,
)]
pub struct OpenToolTopic {
    /// Name of the open topic.
    pub name: String,
    /// Short description of the open topic.
    pub description: String,
}
